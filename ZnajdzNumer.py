def nrtel(text):
    if len(text) !=11:
        return False     # zly numer
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # brak 3 cyfr
        
    if text[3] != '-':
         return False    # brak kreski
        
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # brak 3 cyfr
        
    if text[7] != '-':
        return False     # brak drugiej kreski
    
    for i in range(8, 11):
        if not text[i].isdecimal():
            return False # brak ostatnich 3 cyfr
        
    return True

#print(nrtel('415-555-124'))

msg = 'Zadzwon do mnie 444-111-313 jutro\
        albo 512-412-563 pojutrze,\
        ewentualnie 412-312-512 za 4 dni'

znajdz = False

for i in range(len(msg)):
    skrawek = msg[i:i+11]
    if nrtel(skrawek):
        print('Znaleziony numer: ' + skrawek)
        znajdz = True
        
if not znajdz:
    print('nie znaleziono zadnych numerow')
