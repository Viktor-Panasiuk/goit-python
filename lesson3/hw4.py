import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
try:
    path = sys.argv[1]
except:
    print("No argument")
else:
    print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)
count = len(files)
print(f"Count filles: {count}")

ext_image = ['JPEG', 'PNG', 'JPG']
ext_video = ['AVI', 'MP4', 'MOV']
ext_doc = ['DOC', 'DOCX', 'TXT']
ext_music = ['MP3', 'OGG', 'WAV', 'AMR']
ext_other = list() # Невідомі розширення

all_ext = list() # Всі розширення

files_image = list()
files_video = list()
files_doc = list()
files_music = list()
files_other = list()

for file in files:
    index = file.rfind(".")
    if index>-1:
        ext = file[index + 1:]
        ext = ext.upper()
        all_ext.append(ext)
        if ext in ext_image:
            files_image.append(file)
        elif ext in ext_video:
            files_video.append(file)
        elif ext in ext_doc:
            files_doc.append(file)
        elif ext in ext_music:
            files_music.append(file)
        else:
            files_other.append(file)

print(f"Find {len(files_image)} of image files")
print(files_image)
print("\n", "\n")

print(f"Find {len(files_video)} of video files")
print(files_video)
print("\n", "\n")

print(f"Find {len(files_doc)} of documents files")
print(files_doc)
print("\n", "\n")

print(f"Find {len(files_music)} of music files")
print(files_music)
print("\n", "\n")

print(f"Find {len(files_other)} of other files")
print(files_other)
print("\n", "\n")

print("All extensions:")
print(list(set(all_ext)))