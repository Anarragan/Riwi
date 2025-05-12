
def lectura(cadena:str = "")->dict:
    cont:dict = {}
    for caracter in cadena:
        if caracter in cont:
            cont[caracter] += 1
        else:
            cont[caracter] = 1
    return cont

def main():
    tex:str = str(input("Cadena de texto: "))
    result = lectura(tex)
    for caracter, cantidad in result.items():
        print(f"{caracter!r}:{cantidad}")

if __name__ == "__main__":
    main()

        