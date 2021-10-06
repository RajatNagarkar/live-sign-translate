import cv2
import numpy as np
import os
import string
# Create the directory structure
if not os.path.exists("dataset"):
    os.makedirs("dataset")
if not os.path.exists("dataset/train"):
    os.makedirs("dataset/train")
if not os.path.exists("dataset/test"):
    os.makedirs("dataset/test")
# for i in range(3):
#     if not os.path.exists("data/train/" + str(i)):
#         os.makedirs("data/train/"+str(i))
#     if not os.path.exists("data/test/" + str(i)):
#         os.makedirs("data/test/"+str(i))

for i in string.ascii_uppercase:
    if not os.path.exists("data//train//" + i):
        os.makedirs("data//train//"+i)
    if not os.path.exists("data//test//" + i):
        os.makedirs("data//test//"+i)
    


# Train or test 
mode = 'train'
directory = 'data//'+mode+'//'
minValue = 70

cap = cv2.VideoCapture(0)
interrupt = -1  

count = {
             'a': len(os.listdir(directory+"A")),
             'b': len(os.listdir(directory+"B")),
             'c': len(os.listdir(directory+"C")),
             'd': len(os.listdir(directory+"D")),
             'e': len(os.listdir(directory+"E")),
             'f': len(os.listdir(directory+"F")),
             'g': len(os.listdir(directory+"G")),
             'h': len(os.listdir(directory+"H")),
             'i': len(os.listdir(directory+"I")),
             'j': len(os.listdir(directory+"J")),
             'k': len(os.listdir(directory+"K")),
             'l': len(os.listdir(directory+"L")),
             'm': len(os.listdir(directory+"M")),
             'n': len(os.listdir(directory+"N")),
             'o': len(os.listdir(directory+"O")),
             'p': len(os.listdir(directory+"P")),
             'q': len(os.listdir(directory+"Q")),
             'r': len(os.listdir(directory+"R")),
             's': len(os.listdir(directory+"S")),
             't': len(os.listdir(directory+"T")),
             'u': len(os.listdir(directory+"U")),
             'v': len(os.listdir(directory+"V")),
             'w': len(os.listdir(directory+"W")),
             'x': len(os.listdir(directory+"X")),
             'y': len(os.listdir(directory+"Y")),
             'z': len(os.listdir(directory+"Z"))
             }


while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    
    
    # Printing the count in each set to the screen
    
    cv2.putText(frame, "A : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "B : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "C : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "D : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "E : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "F : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "G : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "H : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "I : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "K : "+str(count['k']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "L : "+str(count['l']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "M : "+str(count['m']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "N : "+str(count['n']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "O : "+str(count['o']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "P : "+str(count['p']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Q : "+str(count['q']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "R : "+str(count['r']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "S : "+str(count['s']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "T : "+str(count['t']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "U : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "V : "+str(count['v']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "W : "+str(count['w']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "X : "+str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Y : "+str(count['y']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Z : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (300-1, 9), (620+1, 319), (255,0,0) ,1)
    
    # Extracting the ROI
    roi = frame[10:310, 300:620]
    
    cv2.imshow("Main Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray,(5,5),2)
    
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    test_image = cv2.resize(test_image, (310,310))
    cv2.imshow("Data Collector", test_image)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break      
    if interrupt & 0xFF == ord('a'):
        print('A saved as', count['a'], '.jpg')
        cv2.imwrite(directory+'A//'+str(count['a'])+'.jpg', test_image)
        count['a'] += 1
    if interrupt & 0xFF == ord('b'):
        print('B saved as', count['b'], '.jpg')
        cv2.imwrite(directory+'B//'+str(count['b'])+'.jpg', test_image)
        count['b'] += 1
    if interrupt & 0xFF == ord('c'):
        print('C saved as', count['c'], '.jpg')
        cv2.imwrite(directory+'C//'+str(count['c'])+'.jpg', test_image)
        count['c'] += 1
    if interrupt & 0xFF == ord('d'):
        print('D saved as', count['d'], '.jpg')
        cv2.imwrite(directory+'D//'+str(count['d'])+'.jpg', test_image)
        count['d'] += 1
    if interrupt & 0xFF == ord('e'):
        print('E saved as', count['e'], '.jpg')
        cv2.imwrite(directory+'E//'+str(count['e'])+'.jpg', test_image)
        count['e'] += 1
    if interrupt & 0xFF == ord('f'):
        print('F saved as', count['f'], '.jpg')
        cv2.imwrite(directory+'F//'+str(count['f'])+'.jpg', test_image)
        count['f'] += 1
    if interrupt & 0xFF == ord('g'):
        print('G saved as', count['g'], '.jpg')
        cv2.imwrite(directory+'G//'+str(count['g'])+'.jpg', test_image)
        count['g'] += 1
    if interrupt & 0xFF == ord('h'):
        print('H saved as', count['h'], '.jpg')
        cv2.imwrite(directory+'H//'+str(count['h'])+'.jpg', test_image)
        count['h'] += 1
    if interrupt & 0xFF == ord('i'):
        print('I saved as', count['i'], '.jpg')
        cv2.imwrite(directory+'I//'+str(count['i'])+'.jpg', test_image)
        count['i'] += 1
    if interrupt & 0xFF == ord('j'):
        print('J saved as', count['j'], '.jpg')
        cv2.imwrite(directory+'J//'+str(count['j'])+'.jpg', test_image)
        count['j'] += 1
    if interrupt & 0xFF == ord('k'):
        print('K saved as', count['k'], '.jpg')
        cv2.imwrite(directory+'K//'+str(count['k'])+'.jpg', test_image)
        count['k'] += 1
    if interrupt & 0xFF == ord('l'):
        print('L saved as', count['l'], '.jpg')
        cv2.imwrite(directory+'L//'+str(count['l'])+'.jpg', test_image)
        count['l'] += 1
    if interrupt & 0xFF == ord('m'):
        print('M saved as', count['m'], '.jpg')
        cv2.imwrite(directory+'M//'+str(count['m'])+'.jpg', test_image)
        count['m'] += 1
    if interrupt & 0xFF == ord('n'):
        print('N saved as', count['n'], '.jpg')
        cv2.imwrite(directory+'N//'+str(count['n'])+'.jpg', test_image)
        count['n'] += 1
    if interrupt & 0xFF == ord('o'):
        print('O saved as', count['o'], '.jpg')
        cv2.imwrite(directory+'O//'+str(count['o'])+'.jpg', test_image)
        count['o'] += 1
    if interrupt & 0xFF == ord('p'):
        print('P saved as', count['p'], '.jpg')
        cv2.imwrite(directory+'P//'+str(count['p'])+'.jpg', test_image)
        count['p'] += 1
    if interrupt & 0xFF == ord('q'):
        print('Q saved as', count['q'], '.jpg')
        cv2.imwrite(directory+'Q//'+str(count['q'])+'.jpg', test_image)
        count['q'] += 1
    if interrupt & 0xFF == ord('r'):
        print('R saved as', count['r'], '.jpg')
        cv2.imwrite(directory+'R//'+str(count['r'])+'.jpg', test_image)
        count['r'] += 1
    if interrupt & 0xFF == ord('s'):
        print('S saved as', count['s'], '.jpg')
        cv2.imwrite(directory+'S//'+str(count['s'])+'.jpg', test_image)
        count['s'] += 1
    if interrupt & 0xFF == ord('t'):
        print('T saved as', count['t'], '.jpg')
        cv2.imwrite(directory+'T//'+str(count['t'])+'.jpg', test_image)
        count['t'] += 1
    if interrupt & 0xFF == ord('u'):
        print('U saved as', count['u'], '.jpg')
        cv2.imwrite(directory+'U//'+str(count['u'])+'.jpg', test_image)
        count['u'] += 1
    if interrupt & 0xFF == ord('v'):
        print('V saved as', count['v'], '.jpg')
        cv2.imwrite(directory+'V//'+str(count['v'])+'.jpg', test_image)
        count['v'] += 1
    if interrupt & 0xFF == ord('w'):
        print('W saved as', count['w'], '.jpg')
        cv2.imwrite(directory+'W//'+str(count['w'])+'.jpg', test_image)
        count['w'] += 1
    if interrupt & 0xFF == ord('x'):
        print('X saved as', count['x'], '.jpg')
        cv2.imwrite(directory+'X//'+str(count['x'])+'.jpg', test_image)
        count['x'] += 1
    if interrupt & 0xFF == ord('y'):
        print('Y saved as', count['y'], '.jpg')
        cv2.imwrite(directory+'Y//'+str(count['y'])+'.jpg', test_image)
        count['y'] += 1
    if interrupt & 0xFF == ord('z'):
        print('Z saved as', count['z'], '.jpg')
        cv2.imwrite(directory+'Z//'+str(count['z'])+'.jpg', test_image)        
        count['z'] += 1
    
cap.release()
cv2.destroyAllWindows()
