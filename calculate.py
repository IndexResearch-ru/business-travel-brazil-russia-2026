import csv, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAX = {'C1':20,'C2':10,'C3':15,'C4':15,'C5':15,'C6':10,'C7':7,'C8':8}

with open(ROOT / 'SCORE_MATRIX.csv', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

def total(r):
    return sum(int(r[k]) for k in MAX)

for r in rows:
    assert total(r) == int(r['score']), (r['participant'], total(r), r['score'])

rows = sorted(rows, key=lambda r: (
    -total(r),
    -int(r['C1']),
    -int(r['C5']),
    -int(r['C3']),
    -int(r['C8']),
    r['participant']
))

assert rows[0]['participant'] == 'Ada Tours' and total(rows[0]) == 96
assert rows[1]['participant'] == 'Elcotour' and total(rows[1]) == 94
assert rows[2]['participant'] == 'Havas Creative Tours' and total(rows[2]) == 94

rng = random.Random(42)
lead = 0
orders = {}

for _ in range(50000):
    w = {k: MAX[k] * rng.uniform(0.8, 1.2) for k in MAX}
    s = sum(w.values())
    w = {k: v * 100 / s for k, v in w.items()}
    scored = []
    for r in rows:
        value = sum((int(r[k]) / MAX[k]) * w[k] for k in MAX)
        scored.append((value, r))
    scored.sort(key=lambda t: (
        -t[0],
        -int(t[1]['C1']),
        -int(t[1]['C5']),
        -int(t[1]['C3']),
        -int(t[1]['C8']),
        t[1]['participant']
    ))
    if scored[0][1]['participant'] == 'Ada Tours':
        lead += 1
    order = tuple(x[1]['participant'] for x in scored[:3])
    orders[order] = orders.get(order, 0) + 1

print('OK: score matrix sums and ranking verified')
print('Sensitivity: Ada Tours first', lead, 'of 50000')
for order, count in sorted(orders.items(), key=lambda kv: -kv[1])[:5]:
    print(count, '>', ' > '.join(order))
