import os
import shutil

position = ['front', 'side', 'back', 'full']
sex = ['MEN', 'WOMEN']

count = 1
for adress, folders, files in os.walk(os.path.join('img', sex[0])):
    for file in range(len(files)):
        if position[0] in files[file]:
            os.rename(os.path.join(adress, files[file]), os.path.join(adress, (f'{str(position[0])}_{str(count)}')))
            count += 1

