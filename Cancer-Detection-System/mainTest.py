import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('SkinCancer.h5')

image=cv2.imread(r'C:\Users\clins\Desktop\CANCER_SYSTEM\dataset_skin\test\benign\1.jpg')

img=Image.fromarray(image)

img=img.resize((64,64))

img=np.array(img)

input_img=np.expand_dims(img, axis=0)

result=np.argmax(model.predict(input_img), axis=-1)

print(result)




