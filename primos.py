def primo(num):
    if num<4:
        return True
    r = int(n/2)+1
    for i in range (2, r):
        if num%i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))

if primo(n):
    print("Es primo.")

else:
    print("No es primo.")
