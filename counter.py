"""
Created by Artur Samvelyan

Email: arthur@rikkicom.io
Company: Rikkicom
"""

import re
import pickle

from collections import defaultdict
from tqdm.notebook import tqdm
from typing import List

# Functions for the task

def clean_text(text: str) -> str:
    cleaned_str = re.sub('[^а-яїіґє\\s]+', '',text,flags=re.IGNORECASE)
    cleaned_str = re.sub('(\\s+)', ' ',cleaned_str)
    cleaned_str = cleaned_str.lower()
    return cleaned_str

def preprocess_text(text: str) -> List[str]:
    cleaned = clean_text(text.lower())
    tokens = cleaned.split()
    return tokens
    
def count(tokens: List[int]) -> dict:
    dd = defaultdict(lambda: 0)
    for token in tokens:
        dd[token] += 1
    return dd

def merge(first, second):
    for k,v in first.items():
        second[k] += v
    return second

# List of datasets to process
datasets = ['data/news.lemmatized.shuffled.txt',
            'data/wiki_dump.lemmatized.txt',
            'data/fiction.lemmatized.shuffled.txt']

freqs = defaultdict(lambda: 0)

# Get words from datasets
for dataset_path in datasets:
    with open(dataset_path, 'r') as f:
        for line in tqdm(f):
            tokens = preprocess_text(line)
            d = count(tokens)
            freqs = merge(d, freqs)

# Save frequencies
with open('frequencies.txt', 'wb') as f:
    pickle.dump(dict(freqs), f)

print('First 50 words')
print(list(freqs.items())[:50])

# Sort words by their frequency
freqs_sorted = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1], reverse=True)}

print('Top 50 of words by their frequency')
print(list(freqs_sorted.items())[:50])

# Save frequencies in the pickle's format
with open('freqs_sorted.txt', 'wb') as f:
    pickle.dump(freqs_sorted, f)
