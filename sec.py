import numpy as np
secLar=np.array([904610,90629,12569,163402,904576,64589,98909])
print("array items=",secLar)
secLar.sort()
print("The second largest item in the array=",secLar[len(secLar)-2])