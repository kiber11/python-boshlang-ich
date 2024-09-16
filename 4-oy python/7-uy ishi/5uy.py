    #1-usul
# import json
# Login=input('login kiriting: ')
# Parol=input('parol kiriting: ')
# d={}
# with open("5foydalanuvchi.json","r") as f:
    
#     d=json.load(f)
# for i in d:
#     if i['login']==Login:
#         if i['parol']==Parol:
#             print('OK')
#             break
#         else:
#             print('Xato parol kiritdingiz')
#             break
#     else:
#         print('Bunday foydalanuvchi yo’q')
#         break
    #2-usul
# import json
# import sys
# d = {}

# with open("5foydalanuvchi.json", "r") as f:
#     d = json.load(f)


# while True:
#     Login = input('Login kiriting: ')
#     Parol = input('Parol kiriting: ')
    
   
#     user_found = False
#     for i in d:
#         if i['login'] == Login:
#             user_found = True
#             if i['parol'] == Parol:
#                 print('OK')
#                 sys.exit() 
#             else:
#                 print('Xato parol kiritdingiz')
#                 break
    
#     if not user_found:
#         print('Bunday foydalanuvchi yo’q')

