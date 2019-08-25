import cv2
import numpy
import sys
import array
import math

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
    patron = []
    for i in range (0,7):
    	patron.append(['0']*5)

    for h in range(7):
        for k in range(5):
            for i in range (((h*alto)/7),((h+1)*alto/7)):
                for j in range((k*(ancho/5)),((k+1)*ancho/5)):
                    if image[i][j]==255:
                            blanco=blanco+1
                    else:
                            negro=negro+1
            if blanco>negro:
                    patron[h][k]=0
            else:
                    patron[h][k]=1
            blanco=0
            negro=0
                     
    return patron

def interprete(patron):
	

    pesos_entrada_oculta = [[-1.6848378619760225,2.481506465615935,0.6094184815499525,-0.33795209684361277,-1.716912263206526,1.7892705742111428],
                [1.441025875127969,1.0160356413571423,1.7630088702871651,0.3840711913377028,-0.5030275567641477,0.24667076649613223],
                [0.8299164462869006,1.1451224745676012,0.6149726266478852,-1.3704756433535095,0.6059843470329916,0.7120059112319642],
                [-1.0738449540917363,-2.3638395490858115,-1.7744615854048922,0.3833273108000279,-0.17064572341200593,-1.2914602604314032],
                [1.3589201598619607,0.895026263836683,1.4258989688332853,-0.3151688889156804,-1.4089950576335908,0.6922362330971019],
                [1.6666452317732021,-0.8628007960123801,-1.0303260427211252,-1.793096393859576,0.47521306359842946,1.1728238414791707],
                [0.9225905249516589,1.4058956611114677,0.9612268958562344,0.45337684719330384,5.4258752877509675,0.24061214069143766],
                [-0.7381959140794144,-1.5731426569113185,-2.0456187967500106,0.033163654946877175,1.2568815104859572,-0.9112064852600845],
                [-1.201720608153229,1.1958140882691086,0.7769800275338634,0.40154459632141076,3.840376173939716,-1.064243719943074],
                [0.25826846769049994,0.3803154317886557,0.8790693249255608,-0.7222663840847969,-2.3476780332950926,0.7446869838772376],
                [1.3050507475584254,2.1594223270654918,0.35730142384401087,0.11129336925351954,0.4716423276754541,2.7210833837049906],
                [0.5716629052784589,0.0035836063336991296,0.4687666768322973,2.0791959084907945,1.498770273444022,-1.1280603400419933],
                [-1.3653847693684438,1.8483800027327977,1.8977508427145335,-0.42518511715989965,-0.710120992072003,-0.7655990056376573],
                [-1.9060731252299208,-1.8615359021715683,0.010388347892575816,-2.6842458353378413,-1.2798005133890997,-3.0101620510993397],
                [3.4115772021348034,0.07537877276074086,-0.008130043803718196,-0.7060254334535628,-1.4046063646111344,2.0615781444071692],
                [1.1288299503693613,2.0958240710253264,0.5938961151429973,0.05344009463157925,0.444691579687352,2.703678088732442],
                [1.1934808115176878,0.9737893842059897,1.088188744768974,2.074325796635011,2.363616819517201,-0.6895417180759926],
                [-0.5209397687777679,2.863097220552923,2.863832596094881,0.12863040408956783,0.3861164194581136,-0.12327098292640758],
                [-1.3852348279764333,-2.182966594572841,-0.3780831462120074,-1.3075960991306548,-1.2941558178521995,-2.9607536263434007],
                [-2.2023829394102292,0.5987905319383365,-0.9587732912010222,1.2368141667954082,-1.8994587264737202,0.8814809809432503],
                [-0.06196631551957258,0.3335716894213285,-1.1494539319617407,1.595227474179075,-0.7037375748422597,1.4559848419257038],
                [0.2613545348543904,0.3517159782134014,0.5030651487342328,1.9648490345703846,0.3571318537336636,-0.125311092661087],
                [2.4477940973638908,-1.2293700332979776,0.9753281548102604,-0.5373891965773431,-1.181876292669534,-1.0380549159740424],
                [-0.21220438056053992,-0.6916249879707848,-1.3977170282377893,0.6962827328725442,1.9664272822247808,-0.6942764472425085],
                [-2.189725918008322,0.5694418099726425,-0.6014971109800056,1.6660562803004284,-1.6422497724773568,0.7180511744315621],
                [-0.28723921037842287,-0.5877924572506755,0.8169474451918072,0.6433273024505608,-2.4808305392811234,-1.085665911690052],
                [1.3568338801588213,-2.0975693712314167,0.21006737736528933,0.5960308710034407,-1.484766380016528,-1.9836109105152826],
                [0.36584857567626544,-0.07357015892012798,-0.1189019058466474,1.2839642483960225,-0.47412355758644786,-0.1142090510183527],
                [-0.5244006817056462,-1.2986551975867076,-1.344659926019296,0.6876850808411246,2.6640403529902272,-1.5117053749477707],
                [-1.1399683471077136,1.846013107242629,0.35285618694307397,1.6513062884236742,-0.5351958520164326,1.069079704407308],
                [-1.3053375928311255,-0.21187283280020833,-0.24536975984418738,-3.2833524980314293,-2.171724128876916,-0.0776193834505635],
                [-0.020467548382862386,0.5247750019732532,0.14377429390857163,-1.5026995138520172,0.23249403028352966,0.2234349123519996],
                [-0.512865035122655,-1.2900213736077966,-0.8420311338453583,-1.5839340266716777,0.22168768863700603,-0.45671485757080965],
                [-1.0185749313041628,-1.676815031762868,-1.0086580319234684,-0.5530775409326651,-0.7361972381858369,-1.1326475053734488],
                [2.4575595512843513,-0.4641288755942567,-1.291410285572042,-2.269574953204384,-0.8544070132281202,1.9982958964746855]]
    
    pesos_oculta_salida = [[0.7955673200077219,-0.8656990323889875,4.37136618776722,-8.39608628878951,-2.6126405834634165],[2.9300653098505296,-4.86742502316716,-5.299597089210913,1.8261953321916577,-4.552458758703902],[-2.056687223344379,-5.106810967268074,-0.07422752475926486,2.0965582059192935,-4.1983607738041675],[-3.317129093895342,-6.740023157061013,-5.465013247761863,-2.195672365391713,8.408140983305117],[-8.935679368400669,6.417133257559493,-6.907911953918349,-4.849877571683896,-1.2015456149358956],[7.491548332503251,-1.5152806497363347,-3.2323951472864714,-3.009437840217465,-2.540662823644251]]
        
        
    bias_entrada = [-0.6386622337894349,
                -0.7695307348826369,
                -0.6472225587281962,
                -0.4263720771624468,
                -0.7055330428592813,
                -0.5130600719740981,
                -0.3675096529324021,
                -0.13530293742348723,
                -0.38378381004424733,
                -0.8081432369113769,
                -0.6463170636165572,
                -0.31821628498323323,
                -0.6190633326296219,
                -0.44978991877889,
                -0.6002268658086938,
                -0.638109112726942,
                -0.2914741955146214,
                -0.5387231928552358,
                -0.4149322607675947,
                -0.6919718885698116,
                -0.6507358104266554,
                -0.36832442849569264,
                -0.4872300701747713,
                0.09498909984202361,
                        -0.6664586316111542,
                        -0.7376189827451429,
                        -0.45201083183772167,
                        -0.517934690589731,
                        -0.28697244294596597,
                        -0.6826785765578431,
                        -0.5968206670136965,
                        -0.7241340558059698,
                        -0.6436790496127638,
                        -0.5534469479874197,
                        -0.5661964212122665]
    bias_oculta = [0.45674818653894017,
                -0.2324532084046825,
                0.014870851472806772,
                0.26349788091870163,
                1.3186956367749232,
                        -0.6541693309881582]
        
    bias_salida = [-3.140543397164683,
                -0.3319260891283996,
                1.4509181776464157,
                2.6017999694020806,
                        -0.574667284899352]
    filas_entrada = 7
    col_entrada = 5
    neuronas_entrada = 35
    neuronas_oculta = 4
    neuronas_salida = 5
    entrada = range(35)
    sumatoria_entrada = range(neuronas_entrada)
    sigmoidal_entrada = range(neuronas_entrada)
        
    oculta = range(neuronas_oculta)
    sumatoria_oculta = range(neuronas_oculta)
    sigmoidal_oculta = range(neuronas_oculta)
        
    salida = range(neuronas_salida)
    sumatoria_salida = range(neuronas_salida)
    sigmoidal_salida = range(neuronas_salida)
    
    for i in range(filas_entrada):
        for j in range(col_entrada):         
            entrada[i * col_entrada + j] = patron[i][j]


    for i in range(neuronas_entrada):
        sumatoria_entrada[i] = entrada[i] + bias_entrada[i]
        sigmoidal_entrada[i] = 1 / (1 + math.exp(-1 * sumatoria_entrada[i]))
    
    for j in range(neuronas_oculta):
        oculta[j] = 0
        for i in range(neuronas_entrada):
            oculta[j] += sigmoidal_entrada[i] * pesos_entrada_oculta[i][j]
        
    
    for i in range(neuronas_oculta):
        sumatoria_oculta[i] = oculta[i] + bias_oculta[i]
        sigmoidal_oculta[i] = 1 / (1 + math.exp(-1 * sumatoria_oculta[i]))
    
    for j in range(neuronas_salida):
        salida[j] = 0
        for i in range(neuronas_oculta): 
            salida[j] += sigmoidal_oculta[i] * pesos_oculta_salida[i][j]
        
    
    for i in range(neuronas_salida):
        sumatoria_salida[i] = salida[i] + bias_salida[i]
        sigmoidal_salida[i] = 1 / (1 + math.exp(-1 * sumatoria_salida[i]))
    
    mayor = -0.999
    neurona_activada = -1
    for i in range(neuronas_salida):
        if (sigmoidal_salida[i] > mayor):
            mayor = sigmoidal_salida[i]
            neurona_activada = i
        
    
    if (mayor > 0.75 ):
        
        if neurona_activada==0:
            print "0 "
        if neurona_activada==1:
            print "1 "
        if neurona_activada==2:
            print "2 "
        if neurona_activada==3:
            print "3 "
        if neurona_activada==4:
            print "4 "
        if neurona_activada==5:
            print "5 "
        if neurona_activada==6:
            print "6 "
        if neurona_activada==7:
            print "7 "
        if neurona_activada==8:
            print "8 "
        if neurona_activada==9:
            print "9 "
        if neurona_activada==10:
            print "- "
        if neurona_activada==11:
            print "A "
        if neurona_activada==12:
            print "C "
        if neurona_activada==13:
            print "D "
        if neurona_activada==14:
            print "E "
        if neurona_activada==15:
            print "F "
        if neurona_activada==16:
            print "G "
        if neurona_activada==17:
            print "J "
        if neurona_activada==18:
            print "K "
        if neurona_activada==19:
            print "L "
        if neurona_activada==20:
            print "N "
        if neurona_activada==21:
            print "O "
        if neurona_activada==22:
            print "P "
        if neurona_activada==23:
            print "T "
        if neurona_activada==24:
            print "W "
              
    else:
        print "No reconcozco el numero"

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
    #umbral = calcularUmbral(blur)
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
      vector1= extraerVectorCaracteristico(c1)
      interprete(vector1)
      vector2=extraerVectorCaracteristico(c2)
      interprete(vector2)
      vector3=extraerVectorCaracteristico(c3)
      interprete(vector3)
      vector4=extraerVectorCaracteristico(c4)
      interprete(vector4)
      vector5=extraerVectorCaracteristico(c5)
      interprete(vector5)
      vector6=extraerVectorCaracteristico(c6)
      interprete(vector6)
      vector7=extraerVectorCaracteristico(c7)
      interprete(vector7)
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
