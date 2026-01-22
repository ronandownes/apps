import os

BASE_PATH = r"E:\Apps"

projects = [
    "algebra",
    "functions",
    "coordinate-geometry",
    "geometry",
    "trigonometry",
    "calculus",
    "probability",
    "statistics",
    "complex-numbers",
    "number-systems",
    "vectors",
    "discrete-financial-maths"
]

for project in projects:
    path = os.path.join(BASE_PATH, project)
    os.makedirs(path, exist_ok=True)
    print(f"Ensured: {path}")

print("All project folders created or already exist.")
