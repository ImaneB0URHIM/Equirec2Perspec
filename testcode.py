import os
import cv2 
import Equirec2Perspec as E2P 
import matplotlib.pyplot as plt

if __name__ == '__main__':
    equ = E2P.Equirectangular('src/image.jpg')    # Load equirectangular image
    
    #
    # FOV unit is degree 
    # theta is z-axis angle(right direction is positive, left direction is negative)
    # phi is y-axis angle(up direction positive, down direction negative)
    # height and width is output image dimension 
    #
    img = equ.GetPerspective(60, 0, 0, 720, 1080) # Specify parameters(FOV, theta, phi, height, width)
    
    print(type(img))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
