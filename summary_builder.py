import os
from glob import glob

lst = glob("./*.py", root_dir=None)
lst = [i for i in lst if "leets_summary" not in i]
with open("leets_summary.py", "w") as f2:
    for i in lst:
        with open(i, "r") as f:
            content = f.read()
            f2.write("#-----------------------------------------------\n")
            f2.write(f"# {os.path.basename(i).rsplit('.',1)[0]}\n")
            f2.write(content)
            f2.write("#-----------------------------------------------\n")
            f2.write("\n\n\n")
with open("leets_summary.py", "r") as f2:
    print(f2.read())
