import fileinput

print("1:link")
print("2:nome")

# número da linha onde a tag será adicionada
numero_linha = 73

# abrir o arquivo e ler as linhas
with fileinput.FileInput('links.html', inplace=True) as file:
    for num_linha, line in enumerate(file, start=1):
        # se for a linha correta, adicionar a tag HTML
        if num_linha == numero_linha:
            link = input("")
            nome = input("")

            print('<li><a href="' + link + '" target="_blanck">'+ nome +'</a></li>')
        # imprimir a linha original
        print(line, end='')
print("terminado")