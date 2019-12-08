import os
from bs4 import BeautifulSoup
text = []
for filename in os.listdir("html"):
    html = open("html/{}".format(filename)).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.decompose()
    text.append(soup.get_text())
with open('processed/text.txt', 'w') as file:
    file.write(" ".join(text))
