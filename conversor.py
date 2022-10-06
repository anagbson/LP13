def conversor(v):
  c = v * 0.39
  file = open(' conversão.txt', 'w+')
  file.write(f'o valor {v} em centímetros corresponde a {c} valor em polegadas.')
  file.close