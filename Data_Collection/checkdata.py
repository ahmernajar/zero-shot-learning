import numpy as np
import cv2
i=int(input('>'))
train_data = np.load('frame-{}.npy'.format(i))
print (len(train_data))

for data in train_data:
    img = data[0]
    dat=data[1]
    print(dat)
    
    cv2.imshow('test',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
            
