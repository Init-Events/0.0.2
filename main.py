from flask import Flask, request, render_template
import sys
import html
sys.path.insert(0, 'src/')
from tools import generateFrames
from textToEmotion import Emotion

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("form.html")

@app.route('/submit-starter-form', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        #Get the sentence from the user
        user_sentence = request.form.get("user-sentence")
        #Get the emotions from text2emoton
        emotionObj = Emotion(user_sentence)
        emotion = emotionObj.getTopEmotion()
        #Use this function to actually generate pics and return array of files
        avatarImageName = generateFrames(emotion)
    return render_template("received.html", links=avatarImageName)

app.run()