#Crie uma função que receba uma string e faça o mesmo que o método de
#string strip(). Se nenhum outro argumento for passado além da string em que a
#remoção será feita, os caracteres de espaço em branco serão removidos do
#início e do fim da string. Caso contrário, os caracteres especificados no
#segundo argumento da função serão removidos da string.

import re

def tiraEspacoBranco(frase):
    print("\nExpressão completa:"+frase+"")
    pattern = re.compile(r'\s+$')    
    frase = re.sub(pattern, '', frase)
    pattern = re.compile(r'^\s+')
    frase = re.sub(pattern,'', frase)
    print ("\nExpressão corrigida:"+frase+"")
    
    
def removex(frase,parte = 1):
    if type(parte) is str:
        print("\nExpressão completa:"+frase+"")
        pattern = re.compile(r''+parte)    
        frase = re.sub(pattern, '', frase)
        pattern = re.compile(r'^\''+parte)
        frase = re.sub(pattern,''+parte, frase)
        print ("\nExpressão corrigida:"+frase+"")
    else:
        tiraEspacoBranco(frase)


frase = input("Digite a frase: ")
parte = 1
parte = input("\nDigite a expressão a ser removida: ")

if(parte == ''):
    parte = 1
    
if type(parte) is int:
    removex(frase)
else:
    removex(frase,parte)