## Word Frequencies Counting for UberText corpus

UberText corpus: https://lang.org.ua/en/corpora/#anchor5

- License of the corpus: **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.**
- License URL: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

## Installation

Install all dependencies by **pip**:

```shell
pip install -r requirements.txt
```

or install all dependencies by **pipenv**:

```shell
pipenv install

# and then activate virtual environment
pipenv shell
```

## How to run

1) Download the corpus

```shell
mkdir data
cd data

wget https://lang.org.ua/static/downloads/corpora/news.lemmatized.shuffled.txt.bz2
bzip2 -d news.lemmatized.shuffled.txt.bz2

wget https://lang.org.ua/static/downloads/corpora/wiki_dump.lemmatized.txt.bz2
bzip2 -d wiki_dump.lemmatized.txt.bz2

wget https://lang.org.ua/static/downloads/corpora/fiction.lemmatized.shuffled.txt.bz2
bzip2 -d fiction.lemmatized.shuffled.txt.bz2
```

2) Open the notebook in Jupyter

```shell
jupyter notebook ubercorpus-counting.ipynb
```

3) Or just use the `counter.py` script

```shell
python counter.py
```
