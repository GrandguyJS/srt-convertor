def process_srt(file_path, char_limit):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    buffer = ""
    for line in lines:
        stripped = line.strip()
        if not stripped or '-->' in stripped or stripped.isdigit():
            output.append(line + '\n')
            continue

        candidate = f"{buffer} {stripped}".strip()
        if len(candidate) <= char_limit:
            buffer = candidate
            output.append(buffer + '\n')
        else:
            buffer = stripped
            output.append(buffer + '\n')
    with open(file_path.replace('.srt', '_karaoke.srt'), 'w', encoding='utf-8') as f:
        f.writelines(output)
    return True

file_path = input("File path: ")
char_limit = int(input("Char limit: "))
process_srt(file_path, char_limit)