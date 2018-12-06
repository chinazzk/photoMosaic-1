import numpy as np
import matplotlib.pyplot as plt
import cv2

result = np.load("result.npy")
print(result)
cv2.imwrite('result.jpg',result)
cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

