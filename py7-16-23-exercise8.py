#Escreva um programa que receba duas listas de números e retorne uma nova lista contendo apenas os elementos que são comuns a ambas as listas, sem repetições. Em seguida, imprima a nova lista resultante.
var_list1 = input("Insira a 1a lista de números")
var_list2 = input("Insira a 2a lista de números")
var_list1 = var_list1.split()
var_list2 = var_list2.split()
numbers = []
if(len(var_list1) >= len(var_list2)):
        for i in range(len(var_list1)):
                for j in range(len(var_list2)):
                        if(var_list1[i] == var_list2[j]):
                                numbers.append(var_list1[i])
print(numbers)