import os
from pathlib import Path
import html

def generate_markdown_index(root_dir, output_file):
    # Get all markdown files recursively
    markdown_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                # Get relative path from root directory
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, root_dir)
                markdown_files.append(rel_path)
    
    # Sort files alphabetically
    markdown_files.sort()
    
    # Generate HTML content
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Markdown Files Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .file-list {
            list-style-type: none;
            padding: 0;
        }
        .file-list li {
            margin: 10px 0;
            padding: 5px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }
        .file-list a {
            text-decoration: none;
            color: #0066cc;
        }
        .file-list a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Markdown Files Index</h1>
    <ul class="file-list">
"""
    
    # Add links for each markdown file
    for file_path in markdown_files:
        escaped_path = html.escape(file_path)
        html_content += f'        <li><a href="{escaped_path}">{escaped_path}</a></li>\n'
    
    html_content += """    </ul>
</body>
</html>
"""
    
    # Write the HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    # Set the root directory to search for markdown files
    root_directory = "."  # Current directory, change this if needed
    output_html = "index.html"
    
    generate_markdown_index(root_directory, output_html)
    print(f"Index generated successfully: {output_html}") 