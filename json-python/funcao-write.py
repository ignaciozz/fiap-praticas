# Criando variável de texto
conteudo = ":)"

arquivo = open ("C:\\Users\\Gabriel\\Documents\\Gabriel\\Garoto de Programa\\fiap\\aulas-fiap\\fiap-praticas\\json-python\\arquivo.txt", "a", encoding="UTF-8") 

# Escrevendo a variável "conteudo" dentro do arquivo
arquivo.write(conteudo)

# Fechando arquivo
arquivo.close()