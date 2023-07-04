distancia= int(input('Digite a distancia em metros: '))
cm = distancia * 100
mm = distancia * 1000

print('A medida em {}M, {:.0f}cm, {:.0f}mm'.format(distancia,cm,mm))