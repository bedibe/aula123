caminho_arquivo = '/Users/202308567861/Documents/aula03/manipulando_arquivo/nomes.txt'

arquivo = open(caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i, linha in enumerate(linhas, start=1):
    print(f'Linha {i}: {linha}')