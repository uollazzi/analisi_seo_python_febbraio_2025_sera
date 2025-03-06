import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

# nltk.download()
nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("italian")

url = "https://www.codicerisparmio.it/"

# recupero la stringa sorgente della pagina (HTML)
response = requests.get(url)

# faccio il parsing con bs4
soup = BeautifulSoup(response.content, "html.parser")

with open("pagina.html", "wt", encoding="utf8") as f:
    f.write(soup.prettify())

# recupero il title
titles = soup.find_all("title")

if len(titles) == 1:
    print(f"Titolo trovato: {titles[0].text}")
    # print(soup.title.string)
elif len(titles) == 0:
    print("ERRORE: Title non trovato")
else:
    print(f"ATTENZIONE: Trovato più di un title ({len(titles)})")

# meta title
meta_title = soup.find("meta", attrs={"name": "title"})

if not meta_title:
    print("ERRORE: Meta Title non trovato")
else:
    print(f"Meta Title trovato: {meta_title.text}")

# meta description
meta_description = soup.find("meta", attrs={"name": "description"})

if not meta_description:
    print("ERRORE: Meta Description non trovato")
else:
    print(f"Meta Description trovato: {meta_description["content"]}")

# immagini senza alt
for i in soup.find_all("img", alt=""):
    print(f"ATTENZIONE: Alt mancante {i["src"]}")

# immagini non raggiungibili
img_non_raggiungibili = []
immagini = []
for i in soup.find_all("img", src=True):
    immagini.append(i["src"])

for i in soup.find_all("img", attrs={"data-src": True}):
    immagini.append(i["data-src"])

for img_url in immagini:
    if requests.get(img_url).status_code != 200:
        img_non_raggiungibili.append(img_url)

print(img_non_raggiungibili)

# estrazione keywords
body = soup.find("body").text

# estraggo tutte le parole e le metto in una lista
words = []
for w in word_tokenize(body):
    words.append(w.lower())

# elenco stopwords
sw = nltk.corpus.stopwords.words("italian")
new_words = []

for w in words:
    if w not in sw and w.isalpha():
        new_words.append(w)

# frequenza delle parole
freq = nltk.FreqDist(new_words)
keywords = freq.most_common(5)

print(keywords)
