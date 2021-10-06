import cv2

for i in range(1, 21):
    image = cv2.imread("/home/choiin/image_make/%d.jpg" %i)
    print("%d th image read!" %i)
    image = cv2.resize(image, (512, 206), interpolation=cv2.INTER_AREA)
    image = cv2.copyMakeBorder(image, 50, 0, 0, 0, cv2.BORDER_CONSTANT, value = [0,0,0])
    image = cv2.resize(image, (1280, 720), interpolation=cv2.INTER_LINEAR)
    
    
    cv2.imwrite("/home/choiin/image3/%d.jpg" %i, image)
