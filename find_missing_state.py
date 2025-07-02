import json

notebook_file = "5.commentsSecton.ipynb"  # Change this if needed

with open(notebook_file, encoding="utf-8") as f:
    nb = json.load(f)

widgets = nb.get("metadata", {}).get("widgets")
if widgets is not None and "state" not in widgets:
    widgets["state"] = {}

with open(notebook_file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Fixed: Added empty 'state' key to notebook-level metadata.widgets.")
