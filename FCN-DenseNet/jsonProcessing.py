import os
import shutil

path = 'C:\\Users\\tzbz_\Documents\Pytorch\Data\\train\json'
new_path = 'C:\\Users\\tzbz_\Documents\Pytorch\Data\\train\images'
count = os.listdir(path)
for j in range(53, len(count) + 1):
    for root, dirs, files in os.walk(path):
        if len(dirs) == 0:
            for i in range(len(files)):
                print("i=", i)
                if files[i].find('img.png') != -1:
                    shutil.copy(os.path.join(path + '/image_' + str(j).zfill(5) + '_json/', files[i]),
                                os.path.join(new_path, 'image_' + str(j).zfill(5) + '.jpg'))