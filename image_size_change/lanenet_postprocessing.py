import cv2
height = 720
width = 1280
for i in range(201,301):
    jungchub_img = cv2.imread("/home/choiin/image1/GT_2/%d.png" %i)
    print("%d th image read!" %i)
    for j in range(0, height):
        point = 0
        for k in range(0, width):
            if all(jungchub_img[j,k] == [255,255,255]) and all(jungchub_img[j,k-1] != [255,255,255]):
                jungchub_img[j,k-4] = [255,255,255]
                jungchub_img[j,k-3] = [255,255,255]
                jungchub_img[j,k-2] = [255,255,255]
                jungchub_img[j,k-1] = [255,255,255]
                if point >= 4:
                    point = 0

            if k < 1276:
                if all(jungchub_img[j,k] == [255,255,255]) and all(jungchub_img[j,k+1] != [255,255,255]) and point < 4:
                    jungchub_img[j,k+1] = [255,255,255]
                    point += 1


#            if all(jungchub_img[j,k] == [255,255,255])  and all(jungchub_img[j,k+1] == [255,255,255]):
#                print(k, end = " ")
#                point += 1
#            elif all(jungchub_img[j,k] == [255,255,255]) and all(jungchub_img[j,k+1] != [255,255,255]):
#                print("\n point :", point)
#                point = 0
        point = 0
        
    cv2.imwrite("/home/choiin/image4/%d.png" %i, jungchub_img)
    

            
            
                



