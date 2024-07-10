
#Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário 
# e calcule as seguintes informações.

#O volume do aquário em litros;
#A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
#A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
#Volume é dado por (comprimento * altura * largura) / 1000
#A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo 
# utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
#A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

import calculos

print(dir(calculos))  # Mostra todos os atributos e métodos do módulo uteis


# comprimento = float(input("Digite o comprimento do aquário (cm): "))
# altura = float(input("Digite a altura do aquário (cm): "))
# largura = float(input("Digite a largura do aquário (cm): "))
# temp_desejada = float(input("Digite a temperatura desejada (°C): "))
# temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

# volume = calculos.calcular_volume(comprimento, altura, largura)

# potencia_termostato = calculos.calcular_potencia_termostato(volume, temp_desejada, temp_ambiente)

# filtragem_min, filtragem_max = calculos.calcular_filtragem(volume)

# print(f"\nVolume do aquário: {volume:.2f} litros")
# print(f"Potência do termostato necessária: {potencia_termostato:.2f} watts")
# print(f"Quantidade de filtragem por hora: entre {filtragem_min:.2f} e {filtragem_max:.2f} litros por hora")