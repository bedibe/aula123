caminho_arquivo = '/Users/202308567861/Documents/aula03/manipulando_arquivo/escrevendo.txt'
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Esta é a primeira linha.\n')
    arquivo.write('Esta é a segunda linha.\n')

    linhas = ['Esta é a primeria linha em uma Lista.\n', 'Esta é a segunda linha em uma lista. \n']
    arquivo.writelines(linhas)