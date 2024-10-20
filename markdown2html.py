#!/usr/bin/python3
import sys

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
        
    # Here you would process the contents of the markdown file 
    # and generate the corresponding HTML.
    # For now, let's just create an empty output file.
    
    with open(output_file, 'w') as f:
        pass

    sys.exit(0)