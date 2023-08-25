import os

k = 0
for i in range(5000):
    if (os.path.exists(str(i)+'.jpg')):
        os.rename(str(i)+'.jpg',str(k)+'.jpg')
        k = k + 1
