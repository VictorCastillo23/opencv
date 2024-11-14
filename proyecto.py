from deepface import DeepFace
import cv2
import pyttsx3

def reconocimiento(frame):
    try:
        recognition = DeepFace.find(frame,db_path='db',model_name='VGG-Face',silent=True)
        print(recognition[0]['identity'][0])

        recognition2 = recognition[0]['identity'][0]
        nombre = recognition2.split('\\')[1].split('/')[0]
        return nombre
    except ValueError:
        return 'Rostro No Detectado'
    except KeyError:
        return 'Rostro No Detectado'


def saludar(mensaje):
    if mensaje != 'Rostro No Detectado':
        engine.say('hola '+ mensaje)
        engine.runAndWait()


vid = cv2.VideoCapture(0)
engine = pyttsx3.init()
engine.setProperty('rate',125)
mensajeAnterior = ''
cv2.namedWindow('Reconocimiento Facial',cv2.WINDOW_NORMAL)

while True:
    ret,frame = vid.read()
    if not ret:
        break
    mensaje = reconocimiento(frame)

    if mensaje != mensajeAnterior:
        saludar(mensaje) 

    cv2.putText(frame,mensaje,(0,115),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))

    cv2.imshow('Reconocimiento Facial',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    mensajeAnterior = mensaje

vid.release()
cv2.destroyAllWindows()