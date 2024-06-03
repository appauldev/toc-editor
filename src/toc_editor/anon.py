import re

RAW_TOC = "../../files/anon/raw_toc.txt"
NEW_TOC = "../../files/anon/new_toc.txt"

with open(RAW_TOC) as f:
    raw_toc = f.readlines()

new_toc = []

pattern_chapterN = r"^\"CHAPTER \d"

for line in raw_toc:
    # print(line)
    if line.startswith('"CHAPTER'):
        match = re.match(pattern_chapterN, line)
        line = line.replace(match.group(), f"{match.group()}:")

    new_toc.append(line)

with open(NEW_TOC, "w") as f:
    f.writelines(new_toc)
