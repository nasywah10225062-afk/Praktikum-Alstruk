angka = int(input("Masukkan angka: "))

if angka < 2:
    print("Bukan bilangan prima")
else:
    prima = True

    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

    if prima:
        print("Bilangan prima")
    else:
        print("Bukan bilangan prima")
