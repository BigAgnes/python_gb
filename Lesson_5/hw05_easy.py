# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

path = ("dir_1","dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9")
for dir1 in path:
    os.makedirs(os.path.join(dir1))


path1 = ("dir_1","dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9")
for dir1 in path1:
    os.rmdir(os.path.join(dir1)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

for root, dir, files in os.walk("."):
    print(root)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

dir_1 = os.path.abspath('dir_1')
if not os.path.exists(dir_1):
    os.makedirs(dir_1)
