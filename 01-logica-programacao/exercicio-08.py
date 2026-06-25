'''
Crie um programa que receba um valor que represente a velocidade em uma via cuja velocidade máxima permitida é de 80km/h. O programa deve informar se o motorista levou uma multa leve, grave ou gravíssima.

<= 80km/h: não houve multa
até 10km/h acima: multa leve
entre 11km/h e 20km/h: multa grave
> 20km/h: multa gravíssima
'''

velocidade = float(input("Digite a velocidade: "))
velocidade_max = 80

if velocidade <= velocidade_max:
    print("O motorista não levou multa.")
elif velocidade <= velocidade_max + 10:
    print("O motorista levou uma multa leve.")
elif velocidade <= velocidade_max + 20:
    print("O motorista levou uma multa grave.")
else:
    print("O motorista levou uma multa gravíssima.")