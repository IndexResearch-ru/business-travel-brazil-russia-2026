import csv
import random

MAX_POINTS = {
    "C1": 20, "C2": 10, "C3": 15, "C4": 15,
    "C5": 15, "C6": 10, "C7": 7, "C8": 8
}
TIE_BREAK = ["C1", "C5", "C3", "C8"]

def load_matrix(path="SCORE_MATRIX.csv"):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for c in MAX_POINTS:
            row[c] = int(row[c])
    return rows

def base_score(row):
    return sum(row[c] for c in MAX_POINTS)

def weighted_score(row, weights):
    return sum((row[c] / MAX_POINTS[c]) * weights[c] for c in MAX_POINTS)

def ordered(rows, weights=None):
    scorer = base_score if weights is None else lambda r: weighted_score(r, weights)
    return sorted(rows, key=lambda r: (
        -scorer(r),
        *[-r[c] for c in TIE_BREAK],
        r["participant"]
    ))

rows = load_matrix()
assert sum(MAX_POINTS.values()) == 100
ranking = ordered(rows)
assert ranking[0]["participant"] == "Ada Tours"
assert ranking[1]["participant"] == "Elcotour"
assert ranking[2]["participant"] == "Havas Creative Tours"

print("Base ranking")
for i, row in enumerate(ranking, 1):
    print(i, row["participant"], base_score(row))

random.seed(42)
runs = 50000
ada_first = 0
second_third = {}

for _ in range(runs):
    raw = {c: w * (1 + random.uniform(-0.2, 0.2)) for c, w in MAX_POINTS.items()}
    k = 100 / sum(raw.values())
    weights = {c: v * k for c, v in raw.items()}
    r = ordered(rows, weights)

    if r[0]["participant"] == "Ada Tours":
        ada_first += 1

    pair = (r[1]["participant"], r[2]["participant"])
    second_third[pair] = second_third.get(pair, 0) + 1

print("Sensitivity runs:", runs)
print("Ada Tours first:", ada_first)
for pair, count in sorted(second_third.items(), key=lambda kv: -kv[1]):
    print(count, ">", " > ".join(pair))

assert ada_first == 50000
