import requests
from bs4 import BeautifulSoup
import os

def extract_text_from_html_file(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    # Read HTML content from local file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove scripts, styles, and ads
    for tag in soup(['script', 'style', 'noscript', 'header', 'footer', 'form', 'iframe']):
        tag.decompose()

    text = soup.get_text(separator='\n')

    # Clean empty lines
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = '\n'.join(line for line in lines if line)

    return cleaned_text

def extract_text_from_url(url):
    # Download HTML content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove scripts, styles, and ads
    for tag in soup(['script', 'style', 'noscript', 'header', 'footer', 'form', 'iframe']):
        tag.decompose()

    text = soup.get_text(separator='\n')

    # Clean empty lines
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = '\n'.join(line for line in lines if line)

    return cleaned_text

# Example usage for local HTML file
html_file_path = 'webpage.html'  # Change this to your local HTML file path
text = extract_text_from_html_file(html_file_path)
if text:
    with open('output-beautiful-soup.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Text saved to beautiful-soup.txt")

