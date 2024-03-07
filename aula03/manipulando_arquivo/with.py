caminho_arquivo =  ('/Users/202308567861/Documents/aula03/manipulando_arquivo/nomes.txt')
with open(caminho_arquivo, 'r') as arquivo: 
    linha1 = arquivo.readline()
    print(f'Linha 1: {linha1}')