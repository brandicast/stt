import speech_recognition as sr

r = sr.Recognizer()
print ('start')
print (r.energy_threshold)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print ('now you can say:')
    audioData = r.listen (source) 
    print (audioData)
    print ('you said something')
try:
    text = r.recognize_google (audioData, language='zh-tw')
    #text = r.recognize_google (audioData)
except Exception as e:
    text =  '講三小?'
    print (e)

print (text)

