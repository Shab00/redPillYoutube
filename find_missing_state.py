import json

notebook_file = "5.commentsSection.ipynb"

with open(notebook_file, encoding="utf-8") as f:
    nb = json.load(f)

notebook_metadata = nb.get("metadata", {})
if "widgets" in notebook_metadata:
    del notebook_metadata["widgets"]
    print("Removed notebook-level widgets metadata.")

removed_count = 0
for i, cell in enumerate(nb.get("cells", [])):
    if "metadata" in cell and "widgets" in cell["metadata"]:
        del cell["metadata"]["widgets"]
        removed_count += 1

print(f"Removed widgets metadata from {removed_count} cell(s).")

with open(notebook_file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook has been cleaned. You can open it in Jupyter now.")
