import os
LINE = "This morning the warung lady remembered my order, slipped in an extra krupuk, and still charged yesterday's price."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
