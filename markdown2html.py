#!/usr/bin/python3
"""
Markdown to HTML converter
"""
import sys
import os
import re
import hashlib

def replace_inline_syntax(line):
    """Replaces inline Markdown syntax with HTML tags."""
    # Replace **text** with <b>text</b>
    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
    # Replace __text__ with <em>text</em>
    line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)
    # Replace [[text]] with MD5 hash of text
    line = re.sub(r'\[\[(.+?)\]\]', lambda m: hashlib.md5(m.group(1).encode()).hexdigest(), line)
    # Replace ((text)) with text with all 'c' and 'C' removed
    line = re.sub(r'\(\((.+?)\)\)', lambda m: re.sub(r'[cC]', '', m.group(1)), line)
    return line

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print("Missing {}".format(input_file), file=sys.stderr)
        exit(1)

    with open(input_file, 'r') as f:
        lines = f.readlines()

    output_lines = []
    in_unordered_list = False
    in_ordered_list = False
    in_paragraph = False

    for line in lines:
        line = line.rstrip('\n')
        if line.strip() == '':
            # Empty line indicates end of paragraph or list
            if in_unordered_list:
                output_lines.append('</ul>')
                in_unordered_list = False
            if in_ordered_list:
                output_lines.append('</ol>')
                in_ordered_list = False
            if in_paragraph:
                output_lines.append('</p>')
                in_paragraph = False
            continue

        # Apply inline replacements
        line = replace_inline_syntax(line)

        if line.startswith('#'):
            # Close any open tags
            if in_unordered_list:
                output_lines.append('</ul>')
                in_unordered_list = False
            if in_ordered_list:
                output_lines.append('</ol>')
                in_ordered_list = False
            if in_paragraph:
                output_lines.append('</p>')
                in_paragraph = False

            # Process heading
            heading_level = len(line) - len(line.lstrip('#'))
            content = line.strip('#').strip()
            content = replace_inline_syntax(content)
            output_lines.append('<h{}>{}</h{}>'.format(heading_level, content, heading_level))
        elif line.startswith('- '):
            # Process unordered list item
            if in_ordered_list:
                output_lines.append('</ol>')
                in_ordered_list = False
            if in_paragraph:
                output_lines.append('</p>')
                in_paragraph = False
            if not in_unordered_list:
                output_lines.append('<ul>')
                in_unordered_list = True
            content = line[2:].strip()
            content = replace_inline_syntax(content)
            output_lines.append('<li>{}</li>'.format(content))
        elif line.startswith('* '):
            # Process ordered list item
            if in_unordered_list:
                output_lines.append('</ul>')
                in_unordered_list = False
            if in_paragraph:
                output_lines.append('</p>')
                in_paragraph = False
            if not in_ordered_list:
                output_lines.append('<ol>')
                in_ordered_list = True
            content = line[2:].strip()
            content = replace_inline_syntax(content)
            output_lines.append('<li>{}</li>'.format(content))
        else:
            # Process paragraph
            if in_unordered_list:
                output_lines.append('</ul>')
                in_unordered_list = False
            if in_ordered_list:
                output_lines.append('</ol>')
                in_ordered_list = False
            if not in_paragraph:
                output_lines.append('<p>')
                in_paragraph = True
                output_lines.append(line)
            else:
                output_lines.append('<br/>')
                output_lines.append(line)

    # Close any open tags at the end
    if in_unordered_list:
        output_lines.append('</ul>')
    if in_ordered_list:
        output_lines.append('</ol>')
    if in_paragraph:
        output_lines.append('</p>')

    with open(output_file, 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

    exit(0)
