import math

def terbilang(n):
    if n < 0:
        return 'minus ' + terbilang(-n)

    namas = ['elun', "jisi", "rolo", "letu",
            'tatap', 'mila', 'emen', 'tipu',
            'lowu', 'ngasa']
    
    if n < 10:
        return namas[n]
    
    n_digit = len(str(n))
    pangkat = n_digit - 1
    if pangkat > 3:
        pangkat //= 3
        pangkat *= 3
    pembagi = int(math.pow(10, pangkat))
    muka = n // pembagi
    ekor = n % pembagi
    
    if pangkat == 1:
        akhiran = 'lupuh'
    elif pangkat == 2:
        akhiran = 'tasus'
    else:
        raise ValueError
    
    if n > 10 and n < 20:
        muka = ekor
        ekor = 0
        akhiran = 'was'
    if n > 20 and n < 30:
        muka = ekor
        ekor = 0
        akhiran = 'kilur'
        
    
    if muka < 10:
        hasil = namas[muka]
    else:
        hasil = terbilang(muka)
        hasil += pemisah + akhiran
    if ekor > 0:
        hasil += ' ' + terbilang(ekor)
    elif ekor == 0:
        hasil += ' ' + "lupuh"
    return hasil

# for i in range(-10, 0):
#     print(terbilang(i))

for i in range(0,31):
    print(terbilang(i))