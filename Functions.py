from File_Importer import *

def isIn(p,boxes):
    boxes=boxes[0]
    for i in p:
        c=0
        for box in boxes:
            box=box.astype(np.float64).tolist()
            ymin=int(240*box[0])
            ymax=int(240*box[2])
            xmin=int(320*box[1])
            xmax=int(320*box[3])
            print(xmin,xmax,ymin,ymax)
            if(xmin<=i[0] and i[0]<=xmax and ymin<=i[1] and i[1]<=ymax):
                idx=c
                return True,idx,[ymin,ymax,xmin,xmax]
            else:
                return False,0,[0,0,0,0]
            c+=1


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def play_sounds(queue):
    for sound in queue:
        print(sound)
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        os.remove(sound)
        #print("deleted")

def CourtColorExtractor(cropped_img):
    color = ('b','g','r')
    c=[]
    for i,col in enumerate(color):
        histr = cv2.calcHist([cropped_img],[i],None,[256],[0,256])
        i,j=np.where(histr==np.amax(histr))
        c.append(int(i[0]))
    return c
