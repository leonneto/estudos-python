valor = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(valor))
print('Só tem espaço: ', valor.isspace() )
print('É numero: ', valor.isnumeric())
print('É alfabético: ', valor.isalpha())
print('É alfanumerico: ', valor.isalnum())
print('Está em maiusculo: ',valor.isupper())
print('Está em minusculo: ', valor.islower())
