# Importar librerías necesarias
import cv2

# Definir la ruta del video
video_path = "/Users/macbookair/Documents/Python Projects/CodePython/Mujer.mp4"

# Inicializar variables y cargar clasificadores
frame_list = []
capture = cv2.VideoCapture(video_path)
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Clasificador de caras
eye_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")  # Clasificador de ojos
color = (255, 255, 0)  # Color del rectángulo para caras
eye_box_color = (0, 0, 255)  # Color del rectángulo para ojos
thickness = 3
count = 0

# Procesar el video
while capture.isOpened():
    ret, image = capture.read()
    
    if not ret:
        print("No se pudo leer el frame (fin del video). Saliendo...")
        break
    
    # Convertir el frame a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en el frame
    faces = face_cascades.detectMultiScale(gray_image, 1.1, 4)
    
    for (x, y, width, height) in faces:
        # Dibujar rectángulo alrededor de las caras
        cv2.rectangle(image, (x, y), (x + width, y + height), color, thickness)
        
        # Región de interés para ojos (en la cara detectada)
        roi_gray = gray_image[y:y + height, x:x + width]
        roi_color = image[y:y + height, x:x + width]
        eyes = eye_cascades.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            # Dibujar rectángulo alrededor de los ojos
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), eye_box_color, 2)
    
    # Mostrar el frame procesado en una ventana
    cv2.imshow("Detección de Caras y Ojos", image)
    
    # Guardar el frame en la lista
    frame_list.append(image)
    
    count += 1
    if count > 200:  # Limitar el número de frames procesados
        break

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Crear un archivo de video con los frames procesados
if frame_list:
    height, width, _ = frame_list[0].shape
    size = (width, height)
    output_path = "faces_and_eyes.mp4"
    frames_per_second = 30
    output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"DIVX"), frames_per_second, size)
    
    for frame in frame_list:
        output.write(frame)
    
    output.release()
    print(f"Video guardado en: {output_path}")

# Liberar recursos
capture.release()
cv2.destroyAllWindows()
