import os
import markdown2
from pathlib import Path

def convert_markdown_to_html(input_path, output_path):
    """
    Convert a markdown file to HTML and save it to the output path.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
            
        # Convert markdown to HTML using markdown2
        print(f"Converting {input_path} to HTML")
        html_content = markdown2.markdown(markdown_content)
        
        # Create a simple HTML document structure
        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{Path(input_path).stem}</title>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Write the HTML content to the output file
        with open(output_path, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html)
            
        print(f"Converted {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")

def process_directory(input_dir, output_dir):
    """
    Recursively process all markdown files in the input directory and its subdirectories.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        # Calculate the relative path from input_dir to current directory
        rel_path = os.path.relpath(root, input_dir)
        
        # Create corresponding output directory
        current_output_dir = os.path.join(output_dir, rel_path)
        os.makedirs(current_output_dir, exist_ok=True)
        
        # Process all markdown files in current directory
        for file in files:
            if file.lower().endswith(('.md', '.markdown')):
                input_file = os.path.join(root, file)
                output_file = os.path.join(
                    current_output_dir,
                    os.path.splitext(file)[0] + '.html'
                )
                convert_markdown_to_html(input_file, output_file)

def main():
    # Define input and output directories
    input_directory = "content"  # Change this to your input directory
    output_directory = "output_html"  # Change this to your desired output directory
    
    print(f"Starting conversion from {input_directory} to {output_directory}")
    process_directory(input_directory, output_directory)
    print("Conversion complete!")

if __name__ == "__main__":
    main() 