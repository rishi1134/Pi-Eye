from File_Importer import *
from StartUpProcesses import *
from Functions import *

def my_callback(pin):
    print("Called")

def object_detect(frame):
    #cv2.imwrite("sam.jpg",frame)
    frame1=cv2.imread("sam.jpg")
    print(frame1.shape)
    frame1.setflags(write=1)
    frame_expanded=np.expand_dims(frame1,axis=0)
    (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})
    closest_name='red'
    class_name='something'
    classes=[]
    queue=[]
    c=0
    print(classes)
    for i in classes[0]:
        if(i!=1):
            class_name=category_index[i]['name']
            box=boxes[0][c].astype(np.float64).tolist()
            crop=processing_frame[int(240*box[0][0]):int(240*box[0][2]),int(320*box[0][1]):int(320*box[0][3])]
            cv2.imwrite(class_name+" .jpg",crop)
            h,w,_=crop.shape
            b,g,r=crop[int(h/2),int(w/2)]
            requested_colour = (r, g, b)
            actual_name, closest_name = get_colour_name(requested_colour)
            print(closest_name)
            mytext=class_name+" is in "+closest_name+" color"
            myobj=gTTS(text=mytext,lang=language,slow=False) 
            myobj.save(class_name+".mp3")
            queue.append(class_name+".mp3")
        c+=1
    if(threading.activeCount()==1):
        s=threading.Thread(target=play_sounds,args=(queue,))
        s.deamon=True
        s.start()
        queue=[]

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#cb = lambda channel, arg1=image: object_detect(arg1)
#GPIO.add_event_detect(23,GPIO.RISING,cb, bouncetime=200)
GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback, bouncetime=500)
print("Starting Power Saving Mode.")
from objinit import *
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    frame1=np.copy(frame.array)
    if GPIO.event_detected(23):
        print(frame1.shape)
        frame1.setflags(write=1)
        frame_expanded=np.expand_dims(frame1,axis=0)
        (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: frame_expanded})
        closest_name='red'
        class_name='something'
        queue=[]
        c=0
        print(classes)
        for i in classes[0]:
            if(i!=1):
                class_name=category_index[i]['name']
                box=boxes[0][c].astype(np.float64).tolist()
                crop=frame1[int(240*box[0]):int(240*box[2]),int(320*box[1]):int(320*box[3])]
                cv2.imwrite(class_name+" .jpg",crop)
                h,w,_=crop.shape
                b,g,r=crop[int(h/2),int(w/2)]
                requested_colour = (r, g, b)
                actual_name, closest_name = get_colour_name(requested_colour)
                print(closest_name)
                mytext=class_name+" is in "+closest_name+" color"
                myobj=gTTS(text=mytext,lang=language,slow=False) 
                myobj.save(class_name+".mp3")
                queue.append(class_name+".mp3")
            c+=1
        if(threading.activeCount()==1):
            s=threading.Thread(target=play_sounds,args=(queue,))
            s.deamon=True
            s.start()
            queue=[]
    cv2.imshow("WebCam",frame1)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    rawCapture.truncate(0)

camera.close()
GPIO.cleanup() 
cv2.destroyAllWindows()
