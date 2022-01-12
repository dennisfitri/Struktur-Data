import math

def terbilang(n):
    if n < 0:
        return 'minus ' + terbilang(-n)

    numbers = ['elun', "jisi", "rolo", "letu",
            'tatap', 'mila', 'emen', 'tipu',
            'lowu', 'ngasa']
    
    if n < 10:
        return numbers[n]
    
    digit = len(str(n))
    divider = int(math.pow(10, digit-1))
    head = n // divider
    tail = n % divider
    
    if digit == 2:
        suffix = ' lupuh'
    elif digit == 3:
        suffix = ' tasus'
    else:
        raise ValueError

    if n > 10 and n < 20:
        head = tail
        tail = 0
        suffix = ' was'
    if n > 20 and n < 30:
        head = tail
        tail = 0
        suffix = ' kilur'
        
    if head < 10:
        result = numbers[head]
    else:
        result = terbilang(head)
    result += suffix
    if tail > 0:
        result += " " + terbilang(tail)
    return result

for i in range(0, 1000):
    print(terbilang(i))