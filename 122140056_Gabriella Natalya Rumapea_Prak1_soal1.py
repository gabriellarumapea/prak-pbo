batasBawah = int(input("batas bawah: "))
batasAtas = int(input("batas atas: "))

if batasBawah < 0 or batasAtas < 0:
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
else:
    hitung_bil = sum(1 for i in range(batasBawah, batasAtas + 1) if i % 2 != 0) + 1

    print("Bilangan ganjil:")
    for i in range(batasBawah, batasAtas + 1):
        if i % 2 != 0:
            print(i)
    print(f"Total: {hitung_bil}")