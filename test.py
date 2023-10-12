import numpy as np
import cv2
from matplotlib import pyplot as plt
import random #to create noise


#let's create some noise
def sp_noise(image,prob):

# Add salt and pepper noise to image
# prob: Probability of the noise

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

im = cv2.imread('image4.jpg') #loads image
image=cv2.cvtColor(im, cv2.COLOR_BGR2RGB) #makes image RGB
image_gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #makes image Gray
image_blur = cv2.blur(image,(50,50))
image_gaussianblur = cv2.GaussianBlur(image,(15,15),500) #ksize goes until 15 idk why
image_noise = sp_noise(image,0.1)  #the noise we created up
image_blurednoise = cv2.blur(image_noise,(15,15))
#plot images into subplots

plt.subplot(231), plt.imshow(image), plt.title('Yuji') #normal Yuji .....231 means 2x3 grid and this is the first item..2 is y 3 is x
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not

plt.subplot(232), plt.imshow(image_gray,cmap = 'gray'), plt.title('Yuji in gray') #cmap is needed for the image to be shown as gray lol idk why
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not

plt.subplot(233), plt.imshow(image_blur), plt.title('Yuji in blur')
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not

plt.subplot(234), plt.imshow(image_gaussianblur), plt.title('Yuji in gaussian blur')
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not


plt.subplot(235), plt.imshow(image_noise), plt.title('Yuji in noise')
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not

plt.subplot(236), plt.imshow(image_blurednoise), plt.title('Yuji in noise and then blurred')
plt.xticks([]) #makes numbers invisible  at x ,you have to put it after every subplot? idk hopefully not
plt.yticks([]) ##makes numbers invisible  at y, ,you have to put it after every subplot? idk hopefully not

"""
plt.xlabel('X axis', fontsize=15) if I want x label
plt.ylabel('Y axis', fontsize=15) if I want y label
"""

"""
----------------------------------------
 plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB)) without subplots I guess
"""

#show plots
plt.show()