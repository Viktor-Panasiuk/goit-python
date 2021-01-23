import re
def normalize(text):
    
    def transliterate(char):
        map = {ord('А'):"A", ord('Б'):"B", ord('В'):"V", ord('Г'):"G", ord('Д'):"D", ord('Е'):"E", ord('Є'):"JE", ord('Ж'):"ZH", ord('З'):"Z",
        ord('И'):"Y", ord('І'):"I", ord('Ї'):"JI", ord('Й'):"J", ord('К'):"K", ord('Л'):"L", ord('М'):"M", ord('Н'):"N", ord('О'):"O", ord('П'):"P",
        ord('Р'):"R", ord('С'):"S", ord('Т'):"T", ord('У'):"U", ord('Ф'):"F", ord('Х'):"H", ord('Ц'):"C", ord('Ч'):"CH", ord('Ш'):"SH", ord('Щ'):"SHH",
        ord('Ю'):"JU", ord('Я'):"JA", ord('Ь'):"'", ord('Ё'):"JO", ord('Ы'):"Y", ord('Э'):"JE"}
        
        if ord(char) in range(1040, 1104):
            return  char.translate(map) if char.isupper() else char.upper().translate(map).lower()
        else:
            return char
    
    result = ''
    for s in text:
        result += transliterate(s)

    return re.sub('\W', '_', result)
    