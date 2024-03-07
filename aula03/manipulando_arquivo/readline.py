caminho_arquivo = '/Users/202308567861/Documents/aula03/manipulando_arquivo/nomes.txt'
arquivo = open(caminho_arquivo, 'r')
linha1 = arquivo.readline()
print(f'Linha 1: {linha1}')

linha2 = arquivo.readline()
print(f'Linha 2: {linha2}')

linha3 = arquivo.readline()
print(f'Linha 3:{linha3}' )

linha4 = arquivo.readline()
print(f'Linha 4: {linha4}')
arquivo.close()