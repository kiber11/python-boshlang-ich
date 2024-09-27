class Convertor:
    ru_to_en_dict = {
        "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "Yo", "Ж": "Zh", "З": "Z", "И": "I", "Й": "Y",
        "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F",
        "Х": "Kh", "Ц": "Ts", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ъ": "'", "Ы": "Y", "Ь": "'", "Э": "E", "Ю": "Yu", "Я": "Ya",
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "zh", "з": "z", "и": "i", "й": "y",
        "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
        "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": "'", "ы": "y", "ь": "'", "э": "e", "ю": "yu", "я": "ya"
    }
    en_to_ru_dict = {
        "A": "А", "B": "Б", "V": "В", "G": "Г", "D": "Д", "E": "Е", "Yo": "Ё", "Zh": "Ж", "Z": "З", "I": "И", "Y": "Й",
        "K": "К", "L": "Л", "M": "М", "N": "Н", "O": "О", "P": "П", "R": "Р", "S": "С", "T": "Т", "U": "У", "F": "Ф",
        "Kh": "Х", "Ts": "Ц", "Ch": "Ч", "Sh": "Ш", "Shch": "Щ", "'": "Ъ", "Y": "Ы", "E": "Э", "Yu": "Ю", "Ya": "Я",
        "a": "а", "b": "б", "v": "в", "g": "г", "d": "д", "e": "е", "yo": "ё", "zh": "ж", "z": "з", "i": "и", "y": "й",
        "k": "к", "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с", "t": "т", "u": "у", "f": "ф",
        "kh": "х", "ts": "ц", "ch": "ч", "sh": "ш", "shch": "щ", "'": "ь", "yu": "ю", "ya": "я"
    }

    def ru_to_en(self, text):
        result = ""
        for char in text:
            result += self.ru_to_en_dict.get(char, char)  
        return result

    def en_to_ru(self, text):
        result = ""
        skip = False
        for i in range(len(text)):
            if skip:
                skip = False
                continue
            
            if i + 1 < len(text) and text[i:i+2] in self.en_to_ru_dict:
                result += self.en_to_ru_dict[text[i:i+2]]
                skip = True  
            else:
                result += self.en_to_ru_dict.get(text[i], text[i]) 
        return result

converter = Convertor()
ruscha_text = "Привет, как дела?"
inglizcha_text = converter.ru_to_en(ruscha_text)
print(f"Ruscha: {ruscha_text}\nInglizcha: {inglizcha_text}\n")

inglizcha_text = "Salom dunyo"
ruscha_text = converter.en_to_ru(inglizcha_text)
print(f"Inglizcha: {inglizcha_text}\nRuscha: {ruscha_text}")
