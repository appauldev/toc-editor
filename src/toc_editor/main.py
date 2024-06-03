old_toc_file = "../../files/old_toc"
new_toc_file = "../../files/new_toc"


with open(old_toc_file, "r") as f:
    old_content = f.readlines()

new_toc = []
for line in old_content:
    if line.startswith('"sdarticle'):
        continue
    new_line = line.strip()

    if new_line.startswith('"Chapter '):
        new_line = f"{new_line}"
    else:
        new_line = f"    {new_line}"

    # print(new_line)
    new_toc.append(new_line)

with open(new_toc_file, "w") as f2:
    f2.write("\n".join(new_toc))
