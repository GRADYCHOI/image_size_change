import cv2
height = 720
width = 1280
tot_acc = 0
tot_prec = 0
tot_rec = 0
for i in range(1,301):
    origin_img = cv2.imread("/home/choiin/image4/%d.png" %i)
    jungchub_img = cv2.imread("/home/choiin/image2/%d.jpg" %i)
    #lanenet_img = cv2.imread("/home/choiin/image3/%d.jpg" %i)
    print("%d th image read!" %i)
    point = 0
    acc = 0
    real_lane1 = 0
    real_lane2 = 0
    pred_lane1 = 0
    pred_lane2 = 0
    for j in range(0, height):
        for k in range(0, width):
            # accuracy
            if all(origin_img[j,k] == jungchub_img[j,k]):
                point +=1
            #precision
            if all(jungchub_img[j,k] == [255,255,255]):
                pred_lane2 +=1
                if all(origin_img[j,k] == [255,255,255]):
                    real_lane2 +=1

            #recall
            if all(origin_img[j,k] == [255,255,255]):
                real_lane1 +=1
                if all(jungchub_img[j,k] == [255,255,255]):
                    pred_lane1 +=1
            ##
    pixel = height * width
    acc = (point/pixel) * 100
    tot_acc += acc
    print("accuracy = ", acc, "%")

    precision = (real_lane2 / pred_lane2) * 100
    recall = (pred_lane1 / real_lane1) * 100
    print("precision = ", precision)
    print("recall = ", recall)
    tot_prec += precision
    tot_rec += recall


print("total accuracy = ", (tot_acc/300), "%")
print("total precision = ", (tot_prec/300))
print("total recall = ", (tot_rec/300))
