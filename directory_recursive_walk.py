import os


def obxodFile(path, level=1):
    print('Папка', path)
    print('level = ', level, 'Content:', os.listdir(path))
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        if os.path.isdir(sub_path):
            print('Спускаемся в папку: ', sub_path)
            obxodFile(sub_path, level + 1)
            print('Возвращаемся в папку: ', path)


path = os.path.abspath(os.path.normpath(input()))

obxodFile(path)
