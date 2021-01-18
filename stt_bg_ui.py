import time
import speech_recognition as sr
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore  import QObject, pyqtSignal, Qt


# this is called from the background threa]d
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    global recognized_text
    try:
        recog = recognizer.recognize_google(audio, language='zh-tw')
        recognized_text =  recog + '\n'
        updater.updateText.emit(recognized_text)
        print("Google Speech Recognition thinks you said " + recog )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def go():
    global isStart
    global stop_listening
    if isStart :
        #w.plainTextEdit.setPlainText ('start.....')
        w.pushButton.setText('停止')
        #w.plainTextEdit.placeholderText = '...start.....' 
        r = sr.Recognizer()
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)   
        print ('start')
        #m = sr.Microphone()
        stop_listening = r.listen_in_background(m, callback)
        print (f'{r.energy_threshold} : {r.dynamic_energy_threshold} : {r.pause_threshold} : {r.operation_timeout}')
        isStart = False
    else :
        w.pushButton.setText('開始')
        stop_listening()
        isStart = True


class Updater(QObject):                                                                                           
    updateText = pyqtSignal(str)   


updater = Updater()


isStart = True 

app = QApplication(sys.argv)
w = loadUi('main.ui')

recognized_text = ''

w.pushButton.clicked.connect(go)
updater.updateText.connect(w.plainTextEdit.setPlainText, Qt.QueuedConnection)

w.show()


# do other things on the main thread
#while True: time.sleep(0.1)


app.exec_()