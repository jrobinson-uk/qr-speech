from io import BytesIO
from time import sleep
from PIL import Image
from picamera import PiCamera
import zbarlight
from gtts import gTTS
import os

stream = BytesIO()

with PiCamera() as cam:
    cam.start_preview(alpha=192)
    while True:
        sleep(0.5)
        cam.capture(stream, 'jpeg')
        stream.seek(0)
        bytecode = zbarlight.scan_codes('',Image.open(stream))
        stream.seek(0)
        stream.truncate()
        #print(bytecode)
        if bytecode != None:
            code = bytecode[0].decode()
            print (code)
            tts = gTTS(text=code,lang='en')
            tts.save("speech.mp3")
            os.system("omxplayer speech.mp3")
        
