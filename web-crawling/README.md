## 1. Installation
Install the Python dependencies:
```bash
pip install -r requirements.txt
```
## 2. Run the crawler & Evaluate
The script scrapes webpage.html and writes the cleaned text to the output txt files:
```bash
bash scraping.sh
```

## 3. What to expect in the output
### Invisible-style defense
For the Invisible Style variant, visible words are interleaved with the fixed token ExpShield at zero font size.
Example:
```
From early curiosity -> FExpShieldrom eExpShieldarly curiositExpShieldy
```
> In the paper's full implementation, the inserted token is randomized per insertion; a fixed token is used here for clarity.

### Invisible-character defense
When the Invisible Character defense is active, the extracted .txt files will look normal in most editors because invisible characters are not rendered. Use a hex dump to verify their presence ``hexdump -C output-newspaper.txt``:

```
000006f0  65 5d 20 46 72 6f e2 81  a3 6d 20 65 61 72 6c e2  |e] Fro...m earl.|
          ↑ ↑  ↑  ↑  ↑  ↑  └─┬─┘
          e ]     F  r  o    │
                             └─ these three bytes of the invisible character,
                                so they show up as “...” on the right
```
> Our code uses three invisible characters: '\u200B', '\u2060', and '\u2063'.

---

## Run a specific extractor (optional)
Each extractor can also be launched directly. Replace ``{toolname}`` with the library you want to test, e.g. ``newspaper``:
```bash
python test-{toolname}.py
```
