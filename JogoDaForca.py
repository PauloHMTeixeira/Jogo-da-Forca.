palavra = input('Qual vai ser a palavra do jogo? ')
forca = palavra.join(' ')
forca = forca.split()

def boneco():
    print('''-------|
            |       _
            |      ___
            |      _ _
            |
            |
            |''')

boneco()
def tamanho():
    print('_' * len(forca))

tamanho()
tentativa = input('Escolha uma letra: ')
while tentativa.isalpha() == True:
    if tentativa in forca:
        tamanho()