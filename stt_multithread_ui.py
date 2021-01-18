import speech_recognition as sr
import time
import threading

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore  import QObject, pyqtSignal, Qt

stop = False
voices = [] 

r = sr.Recognizer()

def bot_listen():
    global stop
    print ('ear start')
    try:
        while (not stop):
            try:
                with sr.Microphone() as source:
                    #r = sr.Recognizer()
                    r.adjust_for_ambient_noise(source)   
                    print (f'{r.energy_threshold} : {r.dynamic_energy_threshold} : {r.pause_threshold} : {r.operation_timeout}')
                    
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
    print ('ear stop')

def bot_translate():
    print ('brain start')
    global stop 
    while (not stop):
        if len(voices) > 0:
            print ('Pop Voice Data out')
            data = voices.pop(0)
            try:
                global recognized_text
                text = r.recognize_google (data, language='zh-tw')
                recognized_text = recognized_text + text + "\n"
                updater.updateText.emit(recognized_text)
            except BaseException as e:
                text =  '講三小?'
                print (e)
                print (data)
            print (text)
        else:
            time.sleep(1)
    print ('brain stop')
 
def go():
    global stop 
    global isStart
    if isStart:
        w.pushButton.setText('停止')
        isStart = False
        ear = threading.Thread(target = bot_listen)  
        ear.start()
        brain = threading.Thread(target = bot_translate)
        brain.start()
        print ("Starting Services........")
    else:
        w.pushButton.setText('開始')
        isStart = True
        stop = True

class Updater(QObject):                                                                                           
    updateText = pyqtSignal(str)   


updater = Updater()

isStart = True 
app = QApplication(sys.argv)
w = loadUi('main.ui')

recognized_text = ''
#w.plainTextEdit.setPlainText(recognized_text)

w.pushButton.clicked.connect(go)
updater.updateText.connect(w.plainTextEdit.setPlainText, Qt.QueuedConnection)
w.show()


# do other things on the main thread
#while True: time.sleep(0.1)


app.exec_()


