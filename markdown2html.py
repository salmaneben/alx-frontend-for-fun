#!/usr/bin/python3
import sys
import re

def parse_markdown(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    in_list_type = ''
    
    for line in lines:
        line = line.strip()
        if re.match(r'^#{1,6} ', line):
            headings = line.split(' ', 1)
            level = len(headings[0])
            html += f'<h{level}>{headings[1]}</h{level}>\n'
        elif re.match(r'^(?:(?:\*)|(?:-))\s', line):
            if not in_list:
                html += '<ul>\n'
                in_list = True
                in_list_type = 'ul'
            html += f'<li>{line[2:]}</li>\n'
        elif re.match(r'^\d+\.\s', line):
            if not in_list:
                html += '<ol>\n'
                in_list = True
                in_list_type = 'ol'
            html += f'<li>{line[2:]}</li>\n'
        else:
            if in_list:
                html += f'</{in_list_type}>\n'
                in_list = False
            html += f'<p>{line}</p>\n'
    if in_list:
        html += f'</{in_list_type}>\n'
        in_list = False
        
    html = re.sub(r'</h([1-6])>\s*<h[1-6]>', '</h\g<1>>\n<h\g<1>>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html)
    html = re.sub(r'__(.+?)__', r'<em>\1</em>', html)
    html = re.sub(r'(?<!<br>)\n', '<br />\n', html)
    html = re.sub(r'\[\[(.+?)\]\]', lambda x: hashlib.md5(x.group(1).encode()).hexdigest(), html)
    html = re.sub(r'\(\((.+?)\)\)', lambda x: re.sub(r'[cC]', '', x.group(1)), html)
    return html
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(markdown_file, 'r') as f:
            markdown = f.read()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
        
    html = parse_markdown(markdown)
    
    with open(output_file, 'w') as f:  
        f.write(html)

    sys.exit(0)