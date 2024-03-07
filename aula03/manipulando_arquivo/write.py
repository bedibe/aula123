arquivo = open('/Users/202308567861/Documents/aula03/manipulando_arquivo/nomes.txt','w')
arquivo.write('Bernardo')
arquivo.close()

arquivo = open('/Users/202308567861/Documents/aula03/manipulando_arquivo/nomes.txt')
print(arquivo.readline())
arquivo.close()
