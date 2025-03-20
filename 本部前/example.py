import cv2
import numpy as np  # PythonのOpenCVでは、画像はnumpyのarrayとして管理される
dif=[0, 90, 130, 90, 90, 90, 90, 90, 30, 30, -30, 50, 10, 30, 70, 30, 30, -130, -130, -130, -130, -90, -50, -90, -90]
for i in range(17, 25):
    img = cv2.imread("honbumae"+str(i)+".jpg")
    out = np.zeros((780, len(img[0]), 3), dtype=np.uint8) 
    for j in range(130+dif[i], 910+dif[i]):
        for k in range(len(img[0])):
            out[j-(130+dif[i])][k] = img[j][k]
    cv2.imwrite("xxx"+str(i)+".jpg", out) # 画像の表示
# i=20
# img = cv2.imread("honbumae"+str(i)+".jpg")
# out = np.zeros((780, len(img[0]), 3), dtype=np.uint8) 
# for j in range(130+dif[i], 910+dif[i]):
#     for k in range(len(img[0])):
#         out[j-(130+dif[i])][k] = img[j][k]
# cv2.imwrite("xxx"+str(i)+".jpg", out) # 画像の表示