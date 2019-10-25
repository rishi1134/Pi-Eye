from File_Importer import *
from objinit import *
from StartUpProcesses import *
from Functions import *

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image=frame.array
    if(fcount<20):
        copy=np.copy(image)
    grey = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur = cv2.blur(grey,(5,5))
    circles = cv2.HoughCircles(blur,method=cv2.HOUGH_GRADIENT,dp=1,minDist=200,param1=100,param2=30,minRadius=20,maxRadius=100)
    if circles is not None:
        #print(circles)
        for i in circles [0,:]:
            if(i[2]==0):
                continue
            p.append(i)
            print("okay")
            cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
            #cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
    if(len(p)>4):
        frame=np.copy(copy)
        frame.setflags(write=1)
        frame_expanded = np.expand_dims(frame, axis=0)

                # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})
        closest_name="red"
        class_name="something"
        print(classes[0])
        #if classes[i] in six.viewkeys(category_index):
        #      class_name = category_index[classes[i]]['name']
        flag,idx,[ymin,ymax,xmin,xmax]=isIn(p,boxes)
        print(flag)
        if flag:
        #if lab in classes[0]:
            #idx=np.where(classes[0]==lab)
            #box=boxes[0][idx].astype(np.float64).tolist()
            lab=classes[0][idx]
            class_name = category_index[lab]['name']
            print(class_name)
            #print(int(240*box[0][0]),int(240*box[0][2]),int(320*box[0][1]),int(320*box[0][3]))
            #crop=frame[int(240*box[0][0]):int(240*box[0][2]),int(320*box[0][1]):int(320*box[0][3])]
            crop=frame[ymin:ymax,xmin:xmax]
            h,w,_=crop.shape
            b,g,r=crop[int(h/2),int(w/2)]
            requested_colour = (r, g, b)
            actual_name, closest_name = get_colour_name(requested_colour)
            print(closest_name)
            mytext=class_name+" is in "+closest_name+" color"
            myobj=gTTS(text=mytext,lang=language,slow=False) 
            myobj.save("msg.mp3")
            #cv2.imwrite("crop.jpg",crop)
            #cv2.imwrite("crop1.jpg",frame)
            #break
            '''vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=2,
                min_score_thresh=0.40)'''
            print(threading.activeCount())
            if(threading.activeCount()==1):
                queue=["msg.mp3"]
                s=threading.Thread(target=play_sounds,args=(queue,))
                s.deamon=True
                s.start()
                queue=[]
        p=[]
    if(abs(fcount-ccount)==20):
        copy=np.copy(image)
        fcount=ccount
    ccount+=1
    cv2.imshow('Objectdetector.jpg', image)
    key=cv2.waitKey(1) & 0XFF
    rawCapture.truncate(0)
    if key == ord('q'):
        break
camera.close()
cv2.destroyAllWindows()

