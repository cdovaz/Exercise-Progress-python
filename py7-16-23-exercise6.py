#Escreva um programa que leia uma sequência de caracteres numéricos e converta-a em uma lista de inteiros. Em seguida, calcule a soma dos elementos da lista e exiba o resultado.

def splitter():
        numbers = input("Insira uma sequência de caracteres numéricos")
        numbers = numbers.split()
        return numbers
def main():
        numbers = splitter()
        var = 0
        for i in range(len(numbers)):
                var += int(numbers[i])
        print(var)
        
main()