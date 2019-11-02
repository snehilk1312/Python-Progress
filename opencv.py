#### IMAGE READING:-
##import cv2
##img=cv2.imread('vijay.jpg')
##cv2.imshow('vijay',img)
##cv2.waitKey(1000)
##cv2.destroyAllWindows()
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
## IMAGE WRITTING:-
##import cv2
##img=cv2.imread('vijay.jpg')
##outpath="D:/2017-2018 COMMITMENT/vijay.jpg"
##cv2.imwrite(outpath, img)
##cv2.imshow('vijy',img)
##cv2.waitKey(0)
##cv2.destroyAllWindow('vijay')
####
##
##
##
##
##
##
##
##
##
##
##
##
## VIDEO CAPTURE:-
##import cv2
##import numpy as np
##cap=cv2.VideoCapture(0)
##while (True):
##    _,frame=cap.read()
##    cv2.imshow('frame',frame)
##    if (cv2.waitKey(1)  & 0xFF == ord('q')):
##        break
##cap.release()
##cv2.destroyAllWindows()
##
##
##
##
##
##
##
##
##
##
##
##
 
##VIDEO CAPTURE USING MOBILE CAMERA:-
import cv2  
import urllib.request  
import numpy as np  
while(1):
    # reads frames from a camera
    url="http://192.168.1.42:8080/shot.jpg"
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    image=cv2.imdecode(imgNp,-1)
    cv2.imshow('Edges',image)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
 
 
 
 
 
 
 
##
##
##
#### CREATE AN TEXTS
##import cv2
##import numpy as np
##img1 = np.zeros((512, 512, 3), np.uint8)
##cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
##cv2.rectangle(img1, (100, 60), (200, 170), (0, 255, 0), -1)
##cv2.circle(img1, (0, 0), 7, (0, 0, 255), -1)
##cv2.ellipse(img1, (256, 256), (100, 100), 0, 0, 360, (127, 127, 127), -1)
##text1 = 'ABc'
##cv2.putText(img1, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 7, (255, 255, 0))  
##cv2.imshow('Lena', img1)
##cv2.waitKey(0)
##cv2.destroyWindow('Lena')
 
 
 
 
 
 
 
 
 
 
 
## GLOBAL THRESHOLDING
##import cv2
##import numpy as np
##img = cv2.imread('1.jpg',0)
##ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
##ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
##ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
##ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
##ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
##cv2.imshow('draw',thresh1)
##cv2.waitKey(0)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
## GLOBAL THRESHOLDING USING REAL TIME:-
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    # reads frames from a camera
##    url="http://192.168.1.14:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    img=cv2.imdecode(imgNp,-1)
##    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    ret,thresh1 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY)
##    ret,thresh2 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY_INV)
##    ret,thresh3 = cv2.threshold(hsv,127,255,cv2.THRESH_TRUNC)
##    ret,thresh4 = cv2.threshold(hsv,127,255,cv2.THRESH_TOZERO)
##    ret,thresh5 = cv2.threshold(hsv,127,255,cv2.THRESH_TOZERO_INV)
##    cv2.imshow('Edges',thresh1)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##        break
##cv2.destroyAllWindows()
 
 
 
## LOCAL THRESHODING
##import cv2
##import numpy as np
##from matplotlib import pyplot as plt
##img = cv2.imread('vijay.jpg',0)
##th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
##th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
##cv2.imshow('draw1',th4)
##cv2.waitKey(0)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
##LOCAL THRESHODING USING REAL TIME
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    # reads frames from a camera
##    url="http://10.128.144.197:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    img=cv2.imdecode(imgNp,-1)
##    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    th3 = cv2.adaptiveThreshold(hsv,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)  
##    th4 = cv2.adaptiveThreshold(hsv,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
##    cv2.imshow('Edges',th4)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##        break
##cv2.destroyAllWindows()
 
 
 
 
 
 
 
 
## EROSION & DILATION
##import cv2
##import numpy as np
##img = cv2.imread('1.jpg',0)
##kernel = np.ones((5,5), np.uint8)
##img_erosion = cv2.erode(img, kernel, iterations=1)
##img_dilation = cv2.dilate(img, kernel, iterations=1)
##cv2.imshow('Input', img)
##cv2.imshow('Erosion', img_erosion)
##cv2.imshow('Dilation', img_dilation)
##cv2.waitKey(0)
##
 
 
 
 
 
 
 
 
 
 
 
## EROSION & DILATION USING REAL TIME:-
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    url="http://192.168.1.14:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    img=cv2.imdecode(imgNp,-1)
##    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    ret,thresh1 = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY)
##    kernel = np.ones((5,5), np.uint8)
##    img_erosion = cv2.erode(thresh1, kernel, iterations=3)
##    img_dilation = cv2.dilate(thresh1, kernel, iterations=3)
##    cv2.imshow('Edges',img_erosion)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##        break
##cv2.destroyAllWindows()
##
 
 
 
 
 
 
## EDGE DETECTION USING CANNY:-
##import cv2
##import numpy as np
##from matplotlib import pyplot as plt
##img = cv2.imread('1.jpg',0)
##edges = cv2.Canny(img,100,200)
##plt.subplot(121),plt.imshow(img,'gray')
##plt.title('Original Image'), plt.xticks([]), plt.yticks([])
##plt.subplot(122),plt.imshow(edges,'gray')
##plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
##plt.show()
 
 
 
 
 
 
 
 
 
 
 
 
 
## CANNY EDGE DETECTION USING REAL TIME:-
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    # reads frames from a camera
##    url="http://192.168.1.14:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    image=cv2.imdecode(imgNp,-1)
##    edges = cv2.Canny(image,100,200)  
##    cv2.imshow('Edges',edges)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##        break
##cv2.destroyAllWindows()
 
 
 
 
 
 
 
 
 
 
## SOBEL EDGE DETECTION:-
##import cv2
##import numpy as np
##img = cv2.imread('vijay.jpg')
##hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
### Calcution of Sobelx
##sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
### Calculation of Sobely
##sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
### Calculation of Laplacian
##laplacian = cv2.Laplacian(img,cv2.CV_64F)
##cv2.imshow('sobelx',sobelx)
##cv2.imshow('sobely',sobely)
##cv2.imshow('laplacian',laplacian)
##cv2.waitKey(0)
 
 
 
 
 
 
 
 
 
## SOBEL EDGE DETECTION USING REAL TIME:-
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    # reads frames from a camera
##    url="http://192.168.1.14:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    img=cv2.imdecode(imgNp,-1)
##    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
##    # Calcution of Sobelx
##    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
##    # Calculation of Sobely
##    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
##    # Calculation of Laplacian
##    laplacian = cv2.Laplacian(img,cv2.CV_64F)
##    cv2.imshow('laplacian',laplacian)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##       break
##cv2.destroyAllWindows()
 
 
## MACHINE LEARNING USING K-MEANS CLUSTERING:-
import numpy as np
import cv2
 
img = cv2.imread('vijay.jpg')
Z = img.reshape((-1,3))
## convert to np.float32
Z = np.float32(Z)
## define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,100,cv2.KMEANS_RANDOM_CENTERS)
## Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
 
 
##import cv2  
##import urllib  
##import numpy as np  
##while(1):
##    w = 160
##    h = 120
##    url="http://192.168.1.14:8080/shot.jpg"
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    img=cv2.imdecode(imgNp,-1)
##    Z = img.reshape((-1,3))
##    Z = np.float32(Z)
##    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
##    K = 2
##    ret,label,center=cv2.kmeans(Z,K,None,criteria,100,cv2.KMEANS_RANDOM_CENTERS)
##    center = np.uint8(center)
##    res = center[label.flatten()]
##    res2 = res.reshape((img.shape))
##    cv2.imshow('res2',res2)
##    if cv2.waitKey(5) & 0xFF==ord('q'):
##       break
##cv2.destroyAllWindows()
