import math
try:
    r = float(input("jari-jari: "))
    
    if r < 0:
        print("jaari-jari lingkaran tidak boleh negatif")
    else:
        luas = math.pi * r * r
        keliling = 2 * math.pi * r
        
        print(f"Luas: {luas:.2f}")
        print(f"keliling: {keliling:.2f}")
     
except ValueError:
    print("Input tidak valid.")
