import cv2
import numpy
import sys
import array

def calcularUmbral(image):
  alto,ancho = image.shape
  vector = range(256)
  suma=0
  for i in range(256):
    vector[i]=0
  for i in range(alto):
        for j in range(ancho):
            vector[image[i][j]]=vector[image[i][j]]+1
  mayor = 0
  for i in range(256):
    if vector[i] > mayor:
      mayor = i
  return 255 - mayor


def recorte(image):
    #matriz=double(imagen)
    alto, ancho = image.shape
    contador=0
    ban=True
    neg=True
    e1=-1#0
    e2=-1#alto
    e3=-1#0
    e4=-1#ancho
    for i in range(alto/2,1,-1):
      #for j in range(1,ancho):
        #if image[i][j]==255:
	        #contador=contador+1
      #if contador>(ancho*3/4) and ban:
	#ban=False
        #e1=i
      for j in range(1,ancho-1):
	if image[i][j]==image[i][j+1] and image[i][j]==255:
		contador=contador+1
	else:
		contador=0
	if contador>(ancho*2)/3 and ban:
		ban=False
		e1=i
      #elif  ban==False and contador<(ancho*1/4)and neg:
	#print "segunda condicion"
	#e1=i
	#neg=False

      contador=0
    ban=True
    for i in range(alto/2,alto):
      for j in range(1,ancho-1):
        if image[i][j]==image[i][j+1] and image[i][j]==255:
		contador=contador+1
        else:
           contador=0

      	if contador>ancho/2 and ban:
		ban=False
		e2=i
      contador=0
    ban=True
    for j in range(1,ancho/2):
      for i in range(e1,e2):
	if image[i][j]==image[i+1][j] and image[i][j]==255:
		contador=contador+1
	else:
	   contador=0
        if contador==(e2-e1) and ban:
		ban=False
		e3=j
      contador=0
    ban=True
    for j in range(ancho-1,ancho/2,-1):
      for i in range(e1,e2):
        if image[i][j]==image[i+1][j] and image[i][j]==255:
		contador=contador+1
	else:
	   contador=0
        if contador==(e2-e1) and ban:
		ban=False
		e4=j
      contador=0
    return e1,e2,e3,e4

def caracteres(image):
    alto,ancho =image.shape
    e1=1
    e2=ancho/4
    ban = True
    contador=0
    for j in range(1,ancho/3):
      for i in range(1,alto):
	if image[i][j]==0 and ban:
		ban=False
		e1=j
    ban=True
    for j in range(e1+1,ancho/2):
      for i in range(1,alto):
	if image[i][j]==0:
	   contador=contador+1
      if contador==0 and ban:
	 e2=j
	 ban=False
      contador=0
    ban = True
    for j in range(e2+1,ancho/2):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e3=j
    ban=True
    for j in range(e3+1,ancho/2):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e4=j
         ban=False
      contador=0
    ban=True
    for j in range(e4+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e5=j
    ban=True
    for j in range(e5+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e6=j
         ban=False
      contador=0
    ban=True
    for j in range(e6+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e7=j
    ban=True
    for j in range(e7+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e8=j
         ban=False
      contador=0
    ban=True
    for j in range(e8+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e9=j
    ban=True
    for j in range(e9+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e10=j
         ban=False
      contador=0
    ban=True
    for j in range(e10+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e11=j
    ban=True
    for j in range(e11+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e12=j
         ban=False
      contador=0
    ban=True
    for j in range(e12+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0 and ban:
                ban=False
                e13=j
    ban=True
    for j in range(e13+1,ancho):
      for i in range(1,alto):
        if image[i][j]==0:
           contador=contador+1
      if contador==0 and ban:
         e14=j
         ban=False
      contador=0

    e = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]
    return e

def extraerVectorCaracteristico(image):
    alto,ancho = image.shape
    descriptor=""
    blanco = 0
    negro = 0
    for h in range(7):
        for k in range(5):
            for i in range (((h*alto)/7),((h+1)*alto/7)):
                for j in range((k*(ancho/5)),((k+1)*ancho/5)):
                    if image[i][j]==255:
                            blanco=blanco+1
                    else:
                            negro=negro+1
            if blanco>negro:
                    descriptor+="0"
            else:
                    descriptor+="1"
            blanco=0
            negro=0
    print descriptor
    return descriptor

def main():
    vector=""
    imagen_dir = sys.argv[1]
    imagen = cv2.imread(imagen_dir)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    #blur = cv2.blur(gray,(5,5))
    #for i in range(0,4):
       #blur = cv2.blur(blur,(5,5))
    #for i in range(0,4):
       #blur = cv2.medianBlur(blur,5)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    umbral = calcularUmbral(blur)
    _ ,umbral = cv2.threshold(blur,68, 255, cv2.THRESH_BINARY) #68
    e1,e2,e3,e4 = recorte(umbral)
    if e1 ==-1 or e2 ==-1 or e3 == -1 or e4 == -1:
      print "No se encontro placa"
    else:
      crop = umbral[e1:e2,e3:e4]
      #c1,c2,c3,c4,c5,c6 = letras(crop)
      a = caracteres(crop)
      alto,ancho = crop.shape
      f1=a[0]
      f2=a[1]
      f3=a[2]
      f4=a[3]
      f5=a[4]
      f6=a[5]
      f7=a[6]
      f8=a[7]
      f9=a[8]
      f10=a[9]
      f11=a[10]
      f12=a[11]
      f13=a[12]
      f14=a[13]
      c1 = crop[1:alto,f1:f2]
      c2 = crop[1:alto,f3:f4]
      c3 = crop[1:alto,f5:f6]
      c4 = crop[1:alto,f7:f8]
      c5 = crop[1:alto,f9:f10]
      c6 = crop[1:alto,f11:f12]
      c7 = crop[1:alto,f13:f14]
      vector+= extraerVectorCaracteristico(c1) +"\n"
      vector+=extraerVectorCaracteristico(c2) +"\n"
      vector+=extraerVectorCaracteristico(c3) +"\n"
      vector+=extraerVectorCaracteristico(c4) +"\n"
      vector+=extraerVectorCaracteristico(c5) +"\n"
      vector+=extraerVectorCaracteristico(c6) +"\n"
      vector+=extraerVectorCaracteristico(c7) +"\n"
      archivo = open("vectores.txt","w")
      archivo.write(vector)
      archivo.close()
      cv2.imshow('original',imagen)
      cv2.imshow('gris',gray)
      cv2.imshow('filtro',blur)
      cv2.imshow('binarizacion',umbral)
      cv2.imshow('recorte',crop)
      cv2.imshow('caracter 1',c1)
      cv2.imshow('caracter 2',c2)
      cv2.imshow('caracter 3',c3)
      cv2.imshow('caracter 4',c4)
      cv2.imshow('caracter 5',c5)
      cv2.imshow('caracter 6',c6)
      cv2.imshow('caracter 7',c7)
      #cv2.waitKey(0)
      c = cv2.waitKey(0)
      if 'q' == chr(c & 255):
        QuitProgram()
if __name__ == '__main__':
    main()
