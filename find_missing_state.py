import json

notebook_file = "5.commentsSecton.ipynb"  # Change if needed

with open(notebook_file, encoding="utf-8") as f:
    nb = json.load(f)

# Remove notebook-level widgets metadata
notebook_metadata = nb.get("metadata", {})
if "widgets" in notebook_metadata:
    del notebook_metadata["widgets"]
    print("Removed notebook-level widgets metadata.")

# Remove widgets metadata from all cells
removed_count = 0
for i, cell in enumerate(nb.get("cells", [])):
    if "metadata" in cell and "widgets" in cell["metadata"]:
        del cell["metadata"]["widgets"]
        removed_count += 1

print(f"Removed widgets metadata from {removed_count} cell(s).")

# Save the fixed notebook
with open(notebook_file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook has been cleaned. You can open it in Jupyter now.")
