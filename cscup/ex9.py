string = input()
def ContaPalavras(string):
    txt = string.lower()
    txt = string.replace('!','').replace('?','').replace('.','').replace(',','').replace('"','')
    semSpace = txt.split()
    dicionario = dict()

    for i in semSpace:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1

    return print(dicionario)

def main():
    ContaPalavras(string)
main()