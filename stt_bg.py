import time
import speech_recognition as sr

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    print ('inside callback')
    try:
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, language='zh-tw'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
with sr.Microphone() as m:
    r.adjust_for_ambient_noise(m)   
print ('start')
#m = sr.Microphone()
stop_listening = r.listen_in_background(m, callback)
print (f'{r.energy_threshold} : {r.dynamic_energy_threshold} : {r.pause_threshold} : {r.operation_timeout}')

# stop listening, wait for 5 seconds, then restart listening
#stop_listening()
#time.sleep(5)
print ('start again')
#stop_listening = r.listen_in_background(m, callback)

# do other things on the main thread
while True: time.sleep(0.1)

print ('end')