lst=['olma','anor','gilos',True,12,10,'banan',9]

# for i, j in enumerate(lst):
#     dublikatlar = [a for a in j if j.count(a) > 1 and type(a) != bool]
#     if dublikatlar:
#         print(f"{i+1}-ro'yxatda dublikatlar bor: {set(dublikatlar)}")
#     else:
#         print(f"{i+1}-ro'yxatda dublikatlar yo'q")

if len(lst) == len(set(lst)):
    print("Bu listda dublikat yoq")