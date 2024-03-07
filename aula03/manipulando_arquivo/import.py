import os 
# Diretório base
diretorio_base = 'C:\\Users\\202308567861\\'

#Subdiretório e nome do arquivo 
subdiretorio = 'Documents\\aula03\\manipulando_arquivo/'
nome_arquivo = 'dados.txt'

#Construir o caminho relativo
caminho_relativo = os.path.join(diretorio_base, subdiretorio, nome_arquivo)

#Obter o caminho absoluto
caminho_absoluto = os.path.abspath(caminho_relativo)

#Exibir os resultados
print(f'Caminho relativo:{caminho_relativo}')
print(f'Caminho absoluto:{caminho_absoluto}')