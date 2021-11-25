import os


position = ['front', 'side', 'back', 'full', 'additional']
sex = ['MEN', 'WOMEN']


def Rename(sex, position):
    count = 1
    for adress, folders, files in os.walk(os.path.join('img', sex)):
        for file in files:
            if position in file:
                os.rename(os.path.join(adress, file), os.path.join(adress, f'{str(position)}_{str(count)}.jpg'))
                count += 1


def Show(sex, position):
    for adress, folders, files in os.walk(os.path.join('img', sex)):
        for file in files:
            if position in file:
                print(os.path.join(adress, file))


def Rename_RUN():
    for s in range(len(sex)):
        for p in range(len(position)):
            Rename(sex[s], position[p])
    print('all is ready >> Rename!')

def Move(sex, position):
    path = r'C:\Users\Ryzen 7\Desktop\Task_parsing\Base'

    for adress, folders, files in os.walk(os.path.join('img', sex)):
        for file in files:
            if position in file:
                os.replace(os.path.join(adress, file), os.path.join(path, f'{sex}\\{position}\\{file}.jpg'))

def Move_RUN():
    for s in range(len(sex)):
        for p in range(len(position)):
            Move(sex[s], position[p])
    print('all is ready >> Move!')

Rename_RUN()
Move_RUN()
