def add_pi_to_words(lines):
    new_lines = []
    for line in lines:
        words = line.split()
        new_words =["pi" + word for word in words]
        new_lines.append(" ".join(new_words))
    return new_lines

with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    new_lines = add_pi_to_words(lines)

    with open("output.txt", "w" , encoding="utf-8") as out_file:
        out_file.writelines("\n".join(new_lines))