print("Invisible Style Defense")
# read html: webpage.html
web_content = open("webpage.html", "r").read()
# count how many "ExpShield" are present
org_count = web_content.count("ExpShield")
print("\tOriginal ExpShield count: ", org_count)

for tool in ["beautiful-soup", "goose3", "trafilatura", "newspaper"]:
    text = open(f"output-{tool}.txt", "r").read()
    count = text.count("ExpShield")
    print(f"\t{tool} ExpShield count: ", count)

print("================================================")
print("Invisible Character Defense")

org_count = 0
html_invisible_characters = ["&ZeroWidthSpace;", "&NoBreak;", "&ic;"]
for char in html_invisible_characters:
    count = web_content.count(char)
    org_count += count

print("\tOriginal invisible-character count: ", org_count)

invisible_characters = ["\u200B", "\u2060", "\u2063"]
for tool in ["beautiful-soup", "goose3", "trafilatura", "newspaper"]:
    text = open(f"output-{tool}.txt", "r").read()
    count = 0
    for char in invisible_characters:
        count += text.count(char)
    print(f"\t{tool} invisible-character count: ", count)