import re, sys, shutil
from pathlib import Path 

files_to_sorted = {'images':['JPEG', 'PNG', 'JPG', 'SVG'],
                    'documents':['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'XLS'],
                    'audio':['MP3', 'OGG', 'WAV', 'AMR'],
                    'video':['AVI', 'MP4', 'MOV', 'MKV'],
                    'archives':['ZIP', 'GZ', 'TAR', 'RAR']}


def create_folder(path_name):
    #create folders (archives, video, audio, documents, images)
    path_ = Path(path_name)
    if not path_.exists():
        path_.mkdir()


def normalize_name(file_n):
    
    def transliterate(char):
        map = {ord('А'):"A", ord('Б'):"B", ord('В'):"V", ord('Г'):"G", ord('Д'):"D", ord('Е'):"E", ord('Є'):"JE", ord('Ж'):"ZH", ord('З'):"Z",
        ord('И'):"Y", ord('І'):"I", ord('Ї'):"JI", ord('Й'):"J", ord('К'):"K", ord('Л'):"L", ord('М'):"M", ord('Н'):"N", ord('О'):"O", ord('П'):"P",
        ord('Р'):"R", ord('С'):"S", ord('Т'):"T", ord('У'):"U", ord('Ф'):"F", ord('Х'):"H", ord('Ц'):"C", ord('Ч'):"CH", ord('Ш'):"SH", ord('Щ'):"SHH",
        ord('Ю'):"JU", ord('Я'):"JA", ord('Ь'):"'", ord('Ё'):"JO", ord('Ы'):"Y", ord('Э'):"JE"}
        
        if ord(char) in range(1040, 1104):
            return  char.translate(map) if char.isupper() else char.upper().translate(map).lower()
        else:
            return char
    
    
    name = file_n.name
    suffix = file_n.suffix
    text = name[:-len(suffix)] if file_n.is_file() else name
    result = ''
    for s in text:
        result += transliterate(s)

    name = re.sub('\W', '_', result) + suffix
    try:
        file_n = file_n.rename(file_n.with_name(name))
    except Exception as E:
        print(f'Error:\n{E}')
    return file_n

def unpack_archive(path_name):
    for f in path_name.iterdir():
        try:
            shutil.unpack_archive(f, f.parent)
            f.unlink()
        except Exception as E:
            print(f'Error:\n{E}')
            


def move_files(path_name, default_path, files_to_sorted):
    
    for f in path_name.iterdir():
        f_n = normalize_name(f)
        if f_n.is_file():
            ext = f_n.suffix[1:].upper()
            for keys in files_to_sorted.keys():
                if ext in files_to_sorted[keys]:
                    try:
                        f_n.rename(Path(default_path + '/' + keys + '/' + f_n.name))
                    except Exception as E:
                        print(f'Error:\n{E}')
                    break
        else:
            if not f_n.name in files_to_sorted.keys():
                move_files(f_n, default_path, files_to_sorted)
    # Delete dir
    if len(list(path_name.iterdir())) == 0:
        path_name.rmdir()


############################################
############################################

def clean_f(p = None):
    try:
        path_name = sys.argv[1] if p == None else p
        path_name = path_name[:-1] if (path_name[-1] == '\\') or (path_name[-1] == '/') else path_name
    except:
        print("No argument")
    else:
        print(f"Start: {path_name}\n")
        path_ = Path(path_name)
        if not path_.exists():
            print(f"The path: {path_name} dosn't exists!")
        else:
            # Create default folders
            for f in files_to_sorted.keys():
                create_folder(path_name + '/' + f)
            
            move_files(path_, path_name, files_to_sorted)
            unpack_archive(Path(path_name + '/archives'))
        print('Finish')


############################################
############################################

if __name__ == '__main__':
    clean_f()