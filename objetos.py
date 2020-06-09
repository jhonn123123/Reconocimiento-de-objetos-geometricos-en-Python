#importacion de modulos

import cv2
import numpy as np


captura=cv2.VideoCapture(0) 

while True:
        (grabbed,image) = captura.read()
        if not grabbed:
            break

        #1.Conversion a Escala de Grises
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Escala de Grises ",gray)
        gray=cv2.GaussianBlur(gray,(3,3),0)
        #cv2.imshow("Escala de Grises",gray)

        #2.Deteccion de bordes
        edged=cv2.Canny(gray,10,150)
        edged = cv2.dilate(edged, None, iterations=1)#///////////////
        edged = cv2.erode(edged, None, iterations=1)#------------
        cv2.imshow("Bordes",edged)

        #3.Operaciones Morfologicas Cierre
        kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        closed=cv2.morphologyEx(edged,cv2.MORPH_CLOSE,kernel,iterations=2)

        #cv2.imshow("Closed",closed)

        #4.Encontrar contornos

        #(contornos,_) = cv2.findContours(umbral.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts,_ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #print "contornos",len(cnts)
        
        total=0

        for c in cnts:
                epsilon = 0.01*cv2.arcLength(c,True)
                approx = cv2.approxPolyDP(c,epsilon,True)
	        #print(len(approx))
                x,y,w,h = cv2.boundingRect(approx)
	        
                
                if len(approx)==3:
                        cv2.drawContours(image,[approx],-1,(0,255,0),3,cv2.LINE_AA)
                        total+=1

                if len(approx)==4:
                        cv2.drawContours(image,[approx],-1,(0,255,0),3,cv2.LINE_AA)
                        total+=1   

                if len(approx)==5:
                        cv2.drawContours(image,[approx],-1,(0,255,0),3,cv2.LINE_AA)
                        total+=1  
                if len(approx)==6:
                        cv2.drawContours(image,[approx],-1,(0,255,0),3,cv2.LINE_AA)
                        total+=1    
                """if len(approx)>50:
                        cv2.drawContours(image,[approx],-1,(0,255,0),3,cv2.LINE_AA)
                        total+=1 """             
                

        #5.Poner texto en imagen
        letrero= 'Objetos: '+ str(total)
        cv2.putText(image,letrero,(10,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        
        #Mostramos imagen
        cv2.imshow("video", image)
        #capturamos teclado
        tecla=cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla== 27:
            break


#Liberamos Objeto
captura.release()

#Destruimos Ventanas
cv2.destroyAllWindows()