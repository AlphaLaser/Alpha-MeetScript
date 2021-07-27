
# Alpha Meet Script

<br/>

## What it does :

- Takes the path of a .mp4 file as input

- Returns the full transcript (Using the Video method of the Async API - Python SDK by Symbl.ai)

- Generates a summary of the whole paragraph in case you are low on time (Basically, it uses NLP (Spacy) to perform lemmatization and tokenization and then uses a simple algorithm to sort out 30% of the most important stuff from the paragraph)

- I also made a Python script to ask for a word input and return basically every sentence where the word is asked in a numbered list

- I locally hosted it using Flask and created an HTML form for the input and a static webpage to show the output

<br/>

## Real life use cases

You missed your zoom meeting and are too lazy to go through the whole recording to see what all was done and what tasks were assigned to you.

1. You can use the summary function to checkout the most important stuff that happened during the meeting

2. You can enter your name as the input in the form and it will return a numbered list of all the sentences where your name was called during the meeting

BOOM ! No need to go through a 1 hr recording. You have all the stuff you need which you can go through in under 2 minutes

<br/>

## Preview

1. Filling the form 

2. The output Analytics

<br/>

## Installation

Run these three commands in your terminal

### 1. Install the required libraries 

- Install symbl.ai API

```bash
pip install symbl
```

- Install Spacy (Python NLP Library)

```bash
pip install spacy
```

- Install this spacy pipeline

```bash
python -m spacy download en_core_web_sm
```

- Install Flask for deployment

```bash
pip install flask
```

### 2. Sign Up on the symbl.ai platform

- Signing up on symbl.ai platform will provide you with a unique app id and app_secret that you can use for your symbl transcriptions

### 3. Changing credintials in the file

- Open the symbl.config file

- Change the demo text to to the app_id and app_secret you obtained on the website

<br/>

## Hosting on a local server 

- Open the folder in your favourite IDE / Code Editor

- Open app.py

- Run the file

- The terminal will show you a local web address you need to go to. Click on it and it will take you to the locally deployed website

<br/>

## Acknowledgements

 - [Symbl.ai Documenmtation](https://docs.symbl.ai/docs/?_ga=2.94379868.1912898433.1627359827-1705200869.1626662338)
 - [Spacy documentation](https://spacy.io/usage/spacy-101/)

  
