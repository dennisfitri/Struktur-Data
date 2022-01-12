import math

def terbilang (n):
    hasil = ''

    namas = ("nol", "satu", "dua", "tiga", "empat", "lima",
    "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas")

    if n < 0:
        hasil += "minus"
        n = -n

    if n < 12:
        if hasil :
            hasil += " "
            hasil += namas[n]
            return hasil

akhirans = ("", "ribu", "juta", "milyar", "triliun")
n_digit = len(str(n))
n_grup = math.ceil(n_digit)
#math.ceil = pembulatan keatas
#math.floor = pembulatan kebawah
