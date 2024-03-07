'''caminho_arquivo = '/Users/202308567861/Documents/aula03/manipulando_arquivo/exemplo.txt'
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)'''

caminho_saida = '/Users/202308567861/Documents/aula03/manipulando_arquivo/exemplo.txt'
with open(caminho_saida, 'w') as arquivo:
    arquivo.write("Nossa aula!")
with open(caminho_saida, 'a') as arquivo:
    arquivo.write("\nde python!.")
    


