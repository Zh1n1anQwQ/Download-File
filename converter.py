import argparse

def convert_to_conversations(input_file, output_file, replace_map=None, prefix="", suffix=""):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    formatted_lines = []
    for line in lines:
        line = line.strip().replace('u8"', '').replace('"', '')  # Remove 'u8"' and '"'
        if replace_map:
            for placeholder, value in replace_map.items():
                line = line.replace(placeholder, value)
        if line.endswith(','):
            line = line[:-1]  # Remove the last comma
        if line:
            formatted_lines.append(f'{prefix}{line}{suffix}')

    converted_content = '\n'.join(formatted_lines)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(converted_content)

def main():
    parser = argparse.ArgumentParser(description='Convert text to formatted conversations.')
    parser.add_argument('--input_file', required=True, help='Input file containing text to convert.')
    parser.add_argument('--output_file', required=True, help='Output file to save the converted text.')
    parser.add_argument('--replace', nargs='+', metavar='placeholder=value', help='Replace placeholders with specific values.')
    parser.add_argument('--prefix', default="", help='Prefix to add to each line.')
    parser.add_argument('--suffix', default="", help='Suffix to add to each line.')
    args = parser.parse_args()

    replace_map = {}
    if args.replace:
        for pair in args.replace:
            pair = pair.strip()
            placeholder, value = pair.split('=')
            replace_map[placeholder] = value

    convert_to_conversations(args.input_file, args.output_file, replace_map, args.prefix, args.suffix)

if __name__ == '__main__':
    main()
