# Criando função para definir o level do herói baseado no XP

def classificar_heroi(xp):
    if xp < 1000:
        return "Ferro"
    elif xp <= 2000:
        return "Bronze"
    elif xp <= 5000:
        return "Prata"
    elif xp <= 7000:
        return "Ouro"
    elif xp <= 8000:
        return "Platina"
    elif xp <= 9000:
        return "Ascendente"
    elif xp <= 10000:
        return "Imortal"
    elif xp>10000:
        return "Radiante"

# Função principal
def main():
    # Entrada de dados
    nome = input("Insira o nome do herói: ")
    
    while True:
        try:
            xp = int(input("Insira a quantidade de XP do herói: "))
            if xp < 0:
                print("Por favor, insira um valor não negativo para XP.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número inteiro válido para XP.")
    
    # Chamada da função classificar_heroi()
    level = classificar_heroi(xp)
    
    # Saída de dados
    print(f"O Herói de nome {nome} está no nível de {level}")

if __name__ == "__main__":
    main()
