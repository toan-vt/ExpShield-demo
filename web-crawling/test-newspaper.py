from newspaper import Article

# local html file
html_file = 'webpage.html'

# Create Article object with dummy URL (required)
article = Article(url='https://dummy.com/')


# Set the HTML content manually
article.set_html(open(html_file, 'r').read())
# article.download()

# Parse the article
article.parse()

# Now you can access article.title, article.text, etc.
text = article.text

# save text to file
with open('output-newspaper.txt', 'w', encoding='utf-8') as f:
    f.write(text)