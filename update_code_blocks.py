import os
import re
import argparse
from pathlib import Path

def replace_playpen_code_blocks(files):
    for file_path in files:
        print(f'Processing {file_path}')
        with open(file_path, 'r') as file:
            content = file.read()

        parent = Path(file_path).parent
        new_content = re.sub(r'{{#playpen\s+(.*?)}}', lambda match: f'```rust,editable\n{open(parent / match.group(1)).read()}\n```', content)

        with open(file_path, 'w') as file:
            file.write(new_content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='List of file paths')
    args = parser.parse_args()

    replace_playpen_code_blocks(args.files)


if __name__ == '__main__':
    main()
