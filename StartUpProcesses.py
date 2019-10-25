from File_Importer import *

pygame.init()
pygame.mixer.init()
camera=PiCamera()
camera.resolution=(320,240)
camera.framerate=32
rawCapture=PiRGBArray(camera,size=(320,240))
time.sleep(0.1)
p=[]
language="en"
fcount=1
ccount=1
queue=[]
list=["Blue.wav","msg.mp3","White.wav"]
c=0
lab=44
