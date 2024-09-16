valyutalar={
    "dollar":[12600,12540,12900,12450,11900],
    "Rubl":[135,120,144,150,130],
    "yevro":[13650,13520,13240,13700,13000],
    "funt":[16150,15380,16640,14980,15540],
    "Tenge":[15,20,40,30,25]
}
for i,j in valyutalar.items():
    print(f'{i}:eng baland narx:{max(j)},eng past narx:{min(j)}')
