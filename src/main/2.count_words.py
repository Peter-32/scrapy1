import re
import nltk
import roughviz
import pandas as pd
from nltk.tokenize import word_tokenize

# Clean and Count
with open('../../data/processed/text.txt', 'r') as file:
    text = file.read()
with open('../../data/raw/programming_languages_list.txt', 'r') as file:
    programming_languages = file.read().split("\n")
text = text.replace("You have JavaScript disabled on your browser. You will not be able to apply for this position without enabling javascript. If you need assistance with enabling javascript, please click here for assistance.","")
text = text.replace("\nData Networking\n", "\n\n")
text = text.replace("\nData Science\n", "\n\n")
text = text.replace("Java Script", "JavaScript")
text = text.replace("C#", "csharp")
wnl = nltk.WordNetLemmatizer()
words = word_tokenize(text)
words = [re.sub(r'[^A-Za-z_\s\-!+*#]', '', w).lower() for w in words]
words = [wnl.lemmatize(w) for w in words if w.strip() != '']
words = ["c#" if x == "csharp" else x for x in words]
fd = nltk.FreqDist(words)
with open('../../data/processed/word_count.txt', 'w') as file:
    file.write("\n".join([str((x,y)) for (x,y) in fd.most_common(100000) if x in programming_languages]))

# Results (Jupyter Notebook only)
common_words = [(x,y) for (x,y) in fd.most_common(100000) if x in programming_languages]
df = pd.DataFrame()
df["word"] = [x for (x,y) in common_words]
df["count"] = [y for (x,y) in common_words]
roughviz.barh(df["word"].iloc[0:20], df["count"].iloc[0:20])
