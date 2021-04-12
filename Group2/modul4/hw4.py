import sys
from pathlib import Path 

ext_image = ['JPEG', 'PNG', 'JPG', 'SVG']
ext_video = ['AVI', 'MP4', 'MOV', 'MKV']
ext_doc = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'XLS']
ext_music = ['MP3', 'OGG', 'WAV', 'AMR']
ext_archives = ['ZIP', 'GZ', 'TAR', 'RAR']

ext_other = set() # Знайдені невідомі розширення
ext_find = set() # Знайдені відомі розширення
files_list = {"image":[], "video":[], "doc":[], "music":[], "archives":[], "other":[]}


def find_files(_path):
    global ext_image, ext_video, ext_doc, ext_music, ext_archives, ext_other, ext_find, files_set
    for f in _path.iterdir():
        if f.is_file():
            ext = f.suffix[1:]
            ext_up = ext.upper()
            if ext_up in ext_image:
                files_list["image"].append(f.name)
                ext_find.add(ext)
            elif ext_up in ext_video:
                files_list["video"].append(f.name)
                ext_find.add(ext)
            elif ext_up in ext_doc:
                files_list["doc"].append(f.name)
                ext_find.add(ext)
            elif ext_up in ext_music:
                files_list["music"].append(f.name)
                ext_find.add(ext)
            elif ext_up in ext_archives:
                files_list["archives"].append(f.name)
                ext_find.add(ext)
            else:
                files_list["other"].append(f.name)
                ext_other.add(ext)
        else:
            find_files(f)
    return True


try:
    path_name = sys.argv[1]
except:
    print("No argument")
else:
    print(f"Start in {path_name}")
    path_ = Path(path_name)

    if not path_.exists():
        print(f"The path: {path_name} dosn't exists!")
    else:
        if find_files(path_):
            for key, values in files_list.items():
                print(f"Find {len(values)} of {key} files")
                print(values, "\n\n")

                print("All known extensions:")
                print(ext_find, "\n\n")

                print("All unknown extensions:")
                print(ext_other, "\n\n")

        else:
            print("Function does not work properly")
