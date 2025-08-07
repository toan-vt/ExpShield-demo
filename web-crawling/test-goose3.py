from goose3 import Goose

# Path to local HTML file
html_file_path = "webpage.html"

# Read the local HTML file
with open(html_file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Initialize Goose
g = Goose()

# Extract article
article = g.extract(raw_html=html)

# Print the main text content
text = article.cleaned_text

# Save to file
with open("output-goose3.txt", "w", encoding="utf-8") as f:
    f.write(text)
