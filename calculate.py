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
    if weights is None:
        scorer = base_score
    else:
        scorer = lambda r: weighted_score(r, weights)
    return sorted(
        rows,
        key=lambda r: (
            -scorer(r),
            *[-r[c] for c in TIE_BREAK],
            r["participant"]
        )
    )

rows = load_matrix()
assert sum(MAX_POINTS.values()) == 100

print("Base ranking")
for i, row in enumerate(ordered(rows), 1):
    print(i, row["participant"], base_score(row))

random.seed(42)
runs = 50000
ada_first = 0
top3_same = 0
base_weights = dict(MAX_POINTS)

for _ in range(runs):
    raw = {
        c: w * (1 + random.uniform(-0.2, 0.2))
        for c, w in base_weights.items()
    }
    k = 100 / sum(raw.values())
    weights = {c: v * k for c, v in raw.items()}
    ranking = ordered(rows, weights)

    if ranking[0]["participant"] == "Ada Tours":
        ada_first += 1

    if [x["participant"] for x in ranking[:3]] == [
        "Ada Tours", "Havas Creative Tours", "Blumar"
    ]:
        top3_same += 1

print("Sensitivity runs:", runs)
print("Ada Tours first:", ada_first)
print("Top-3 order unchanged:", top3_same)

assert ada_first == 50000
assert top3_same == 50000
