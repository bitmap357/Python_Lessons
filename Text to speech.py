from gtts import gTTS

text = "LOL this is really funny"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')
