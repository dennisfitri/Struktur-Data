import math

def terbilang(n):
    if n < 0:
        return "minus" + terbilang(-n)

    namas = ["nol", "satu", "dua", "tiga", "empat", "lima",
    "enam", "tujuh", "delapan", "sembilan"]
    