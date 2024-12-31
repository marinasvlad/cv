import cv2

img = cv2.imread('D:\\MasterTapi\\ComputerVisioning\\python\\DATA\\00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    
    #IF WE WAITED AT LEAST 1MS and WE PRESSED THE ESCAPE KEY
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()