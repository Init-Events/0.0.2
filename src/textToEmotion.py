import text2emotion as te
import nltk

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
    return max(self.emo, key=self.emo.get)