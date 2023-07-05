from gtts import gTTS
import os

# text = "Today is a good day"
# output = gTTS(text=text, lang='en', slow=False)
# output.save('output.mp3')
#
# os.system("start output.mp3")


text = open('demo.txt', 'r').read()

language = 'en'

output = gTTS(text=text, lang=language, slow=False)
output.save('file_output.mp3')
os.system("start file_output.mp3")

