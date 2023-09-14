import text2emotion as te
import nltk
import random

text = "I love coding and it makes me feel so happy!"

class TextToEmotion:

  def __init__(self, text):
    self.text = text
    self.emo = te.get_emotion(text)

  def setText(self, text):
    self.text = text
    self.emo = te.get_emotion(text)

  def getEmotions(self):
    return self.emo

  def getTopEmotion(self):
    # Create a list of random 10 random emotions or feelings
    emotions = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear', 'Majestic', 'Disgust']
    maxEmotion = max(self.emo, key=self.emo.get)
    if self.emo[maxEmotion] < 0.05:
      return emotions[random.randint(0, len(emotions) - 1)]
    return max(self.emo, key=self.emo.get)