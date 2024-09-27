class String:
    def __init__(self, text):
        self.text = text
    
    def to_lower(self, text):
        for i in text:
            if ord(i) >= 65 and ord(i) <= 90:  
                print(chr(ord(i) + 32), end="")  
            else:
                print(i, end="")
        print()  

    def to_upper(self, text):
        for i in text:
            if ord(i) >= 97 and ord(i) <= 122:  
                print(chr(ord(i) - 32), end="")  
            else:
                print(i, end="")
        print()

    def is_lower(self, text):
        for i in text:
            if ord(i) >= 97 and ord(i) <= 122:  
                print(f"{i} is lower")
            else:
                print(f"{i} is not lower")

    def is_upper(self, text):
        for i in text:
            if ord(i) >= 65 and ord(i) <= 90: 
                print(f"{i} is upper")
            else:
                print(f"{i} is not upper")

a=String("Hello")
a.to_lower("Hello")  
a.to_upper("Hello")  
a.is_lower("Hello")  
a.is_upper("Hello")  
