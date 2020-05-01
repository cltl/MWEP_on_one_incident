#!/usr/bin/env bash

python -m spacy download en_core_web_sm
python -m spacy download nl_core_news_sm

rm -rf dep
mkdir dep
cd dep

git clone https://github.com/cltl/multilingual-wiki-event-pipeline
cd multilingual-wiki-event-pipeline
pip install -r requirements.txt
cd ..

git clone https://github.com/cltl/SpaCy-to-NAF
cd SpaCy-to-NAF
pip install -r requirements.txt
