# Multilingual Chatbot for Admission Process in Colleges
# Team Name : NTH.exe

This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Chatbot Positon in our mock website:
[Click This ](https://app.uizard.io/p/95868840)

## For our Presentation and Demo Video for the Chatbot:
[Click This Drive Link](https://drive.google.com/drive/folders/1sBY8gFAOlGGJR_R_AmyKaIRwj-dpV2LW?usp=sharing)

## Basic Commands:
- 50+ commands
- Multilingual
```
hi

आपका नाम क्या है

கல்லூரி கட்டண விவரம்
```

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ gh repo clone Paari1263/team_NTH.exe
$ cd team_NTH.exe
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
`intents.json`contains our different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py`.

## Done By:
Paari.A , Mona Abishek.A, Muralikrishna.S
