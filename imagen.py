import cv2
import numpy as np
#PARA QUE FUNCIONE CV2 HAY QUE INSTALAR ESTAS LIBRERIAS
#pip install opencv-python
#pip install opencv-contrib-python ESTO PARA WINDOWS PARA MAC ES OTRA COSA

# Cargar la imagen dañada
damaged = cv2.imread("/Users/macbookair/Downloads/deadpool.png")
cv2.imshow("Damaged Image", damaged)  

# Cargar la máscara de la imagen
damaged_mask = cv2.imread("/Users/macbookair/Downloads/deadpool.png")
cv2.imshow("Damaged Mask", damaged_mask)  

# Aplicar umbral
threshold_value = 254
output_value = 255
ret, thresh = cv2.threshold(damaged_mask, threshold_value, output_value, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Image", thresh) 

# Crear un kernel para la dilatación
kernel = np.ones((3, 3), np.uint8)
mask = cv2.dilate(thresh, kernel, iterations=1)
gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Mask", gray_mask) 

# Restaurar la imagen
inpaint_radius = 3
restored = cv2.inpaint(damaged, gray_mask, inpaint_radius, cv2.INPAINT_NS)
cv2.imshow("Restored Image", restored)  

# Guardar la imagen restaurada
cv2.imwrite("/Users/macbookair/Downloads/restored_deadpool.png", restored)  # Solo un slash

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()