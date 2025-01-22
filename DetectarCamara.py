# Importar librerías necesarias
import cv2

# Inicializar clasificadores
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Clasificador de caras
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")  # Clasificador de ojos

# Iniciar captura desde la cámara
capture = cv2.VideoCapture(0)  # Índice 0 para la cámara principal

if capture.isOpened():
    print("Cámara activa. Presiona 'q' para salir.")
    while True:
        ret, frame = capture.read()
        
        if not ret:
            print("Advertencia: No se pudo capturar el frame. Reintentando...")
            continue

        # Convertir el frame a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar caras en el frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Dibujar rectángulo azul alrededor de la cara
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

            # Región de interés para los ojos dentro de la cara
            roi_gray = gray_frame[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Detectar ojos dentro de la región de interés
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
            
            for (ex, ey, ew, eh) in eyes:
                # Dibujar rectángulo rojo alrededor de los ojos (más pequeño)
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        # Mostrar el frame procesado
        cv2.imshow("Detección de Caras y Ojos", frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos y cerrar ventanas
    capture.release()
    cv2.destroyAllWindows()
else:
    print("Error: No se pudo abrir la cámara.")
