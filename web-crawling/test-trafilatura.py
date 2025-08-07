import trafilatura
from pathlib import Path

def save_clean_text_from_html_file(html_file_path, output_path="output.txt"):
    # Read local HTML file
    html_file = Path(html_file_path)
    if not html_file.exists():
        print(f"HTML file not found: {html_file_path}")
        return
    
    # Read the HTML content
    html_content = html_file.read_text(encoding='utf-8')
    
    # Extract and clean text
    cleaned_text = trafilatura.extract(html_content)
    if not cleaned_text:
        print("Failed to extract content.")
        return

    # Save to file
    output_path = Path(output_path)
    output_path.write_text(cleaned_text, encoding='utf-8')
    print(f"Content saved to {output_path.resolve()}")

# Example usage:
html_file = "webpage.html"  # Replace with your HTML file path
save_clean_text_from_html_file(html_file, "output-trafilatura.txt")
