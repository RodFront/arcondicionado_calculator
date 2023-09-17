class CalcBtus:
    def __init__(self):
        self.horas = 0
        self.dias = 0
        self.tarifa = 0
        self.btu_7000 = 678
        self.btu_9000 = 815
        self.btu_12000 = 1085
        self.btu_18000 = 1720
        self.btu_24000 = 1980
        self.btu_30000 = 2895

    def calcular(self, btu):
        self.horas = float(input('Horas: '))
        self.dias = float(input('Dias: '))
        self.tarifa = float(input('Digite a tarifa de energia da sua cidade: '))
        btu_value = getattr(self, btu, None)

        if btu_value is not None:
            calculo = float((btu_value * self.dias * self.horas) / 1000 * float(self.tarifa))
            print(f'Você gastará aproximadamente R$ {calculo:.2f} reais!')
        else:
            print('Opção de BTU inválida.')


calc1 = CalcBtus()

while True:
    print("Escolha uma opção de BTU:")
    print("1. 7000 BTU")
    print("2. 9000 BTU")
    print("3. 12000 BTU")
    print("4. 18000 BTU")
    print("5. 24000 BTU")
    print("6. 30000 BTU")
    print("7. Sair")

    escolha = input("Digite o número da opção desejada ou '7' para sair: ")

    if escolha == '1':
        calc1.calcular('btu_7000')
    elif escolha == '2':
        calc1.calcular('btu_9000')
    elif escolha == '3':
        calc1.calcular('btu_12000')
    elif escolha == '4':
        calc1.calcular('btu_18000')
    elif escolha == '5':
        calc1.calcular('btu_24000')
    elif escolha == '6':
        calc1.calcular('btu_30000')
    elif escolha == '7':
        break
    else:
        print('Opção inválida. Tente novamente.')
