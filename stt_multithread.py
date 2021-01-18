import speech_recognition as sr
import time
import threading

stop = False
voices = [] 
r = sr.Recognizer()

def bot_listen():
    global stop
    print ('ear start')
    print (f'{r.energy_threshold} : {r.dynamic_energy_threshold} : {r.pause_threshold} : {r.operation_timeout}')
    
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)   
            print (f'{r.energy_threshold} : {r.dynamic_energy_threshold} : {r.pause_threshold} : {r.operation_timeout}')
            while (not stop):
                try:
                    print ('now you can say:')
                    audioData = r.listen (source) 
                    #print (audioData)
                    voices.append(audioData)
                    print ('Push Voice Data in')
                    #print (f'[EAR] 要結束嘛 ? {stop}' )
                except BaseException as e:
                    print (f'[EAR] Exception : {e}')
    except BaseException as e1:
        print (f'[EAR] E1 {e1}')
        stop = True

def bot_translate():
    print ('brain start')
    global stop 
    while (not stop):
        if len(voices) > 0:
            print ('Pop Voice Data out')
            data = voices.pop(0)
            text = ''
            try:
                text = r.recognize_google (data, language='zh-tw')
                #text = r.recognize_google (audioData)
                #print ('')
                stop = text == '結束'
                #print (f'[BRA] 要結束嘛 ? {stop}' )
            except BaseException as e:
                text =  '講三小?'
                print (e)
                print (data)
            print (text)
        else:
            time.sleep(2)
 


ear = threading.Thread(target = bot_listen)  
brain = threading.Thread(target = bot_translate)


ear.start()
print ("here 1")
brain.start()
print ("here 2")

ear.join()
#brain.join()
print ("結束主程式")

exit() 