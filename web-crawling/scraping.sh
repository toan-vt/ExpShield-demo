echo "Crawling..."
python test-beautiful-soup.py
python test-goose3.py
python test-trafilatura.py
python test-newspaper.py

echo "Counting..."
python count.py

echo "Done!"