#Escreva um programa que resolva a seguinte equação: (a + b) * (c - d) / (e % f), onde a, b, c, d, e e f são variáveis fornecidas pelo usuário. #
#Certifique-se de tratar possíveis erros de divisão por zero.
numbers = input("Insira 6 variáveis")
numbers = numbers.split()
a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])
d = float(numbers[3])
e = float(numbers[4])
f = float(numbers[5])
try:
        val = (a + b) * (c - d) / (e % f)
except ZeroDivisionError:
        num = input("insira dois novos valores para os últimos números")
        num = num.split()
        e = float(num[0])
        f = float(num[1])
        val = (a + b) * (c - d) / (e % f)

print(val)