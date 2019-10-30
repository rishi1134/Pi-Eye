from File_Importer import *
import subprocess

def my_callback(pin):
    print("Called")
    global active_process
    if active_process:
        print('killeed',active_process)
        active_process.terminate()
        active_process.kill()
        print('min')
        active_process=subprocess.Popen(["python3","embed_min.py"])
        inter1=inter
        inter=0
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime=500)

#c=int(input('Press 0 for non-power saving mode, 1 for power saving mode: '))


#from embed_min import *

#from embed_max import *

if __name__ == '__main__':
    active_process = None
    inter1=0
    inter=1
    while True:
        #print(inter1,inter)
        if inter1==inter:
            continue
        else:
            print('max')
            active_process=subprocess.Popen(["python3","embed_max.py"])
            print(active_process)
            inter1=inter
            inter=1
    
