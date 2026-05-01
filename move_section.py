import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# The WHY CHOOSE US section starts with <!-- WHY CHOOSE US --> and ends with </section> before <!-- PROCESS SECTION -->
pattern_why_choose = r'([ \t]*<!-- WHY CHOOSE US -->.*?</section>\n)'
m = re.search(pattern_why_choose, content, re.DOTALL)
if not m:
    print("Could not find WHY CHOOSE US section")
    exit(1)

why_choose_block = m.group(1)

# Remove it from the current position
content = content.replace(why_choose_block, "")

# Insert it after the services section
# The services section ends right before <!-- PORTFOLIO - MASONRY -->
pattern_services_end = r'([ \t]*<!-- PORTFOLIO - MASONRY -->)'
content = re.sub(pattern_services_end, why_choose_block + r'\n\1', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Moved WHY CHOOSE US section.")
