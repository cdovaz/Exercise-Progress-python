#Crie um dicionário que represente um cardápio de um restaurante, com o nome do prato como chave e o preço como valor. 
#Em seguida, escreva uma função que receba o dicionário e retorne o nome do prato mais caro.
def biggest_price(list):
        val = 0
        for i in range(len(list)):
               if(val < float(menu[i].get('price', "chave"))):
                       val = float(menu[i].get('price',"chave" ))
                       nome = menu[i].get("chave",'price' )
        print(str(val)+"\n"+nome)
menu = [{"chave":"Frango assado","price":"15"}, {"chave":"Tambaqui assado na brasa","price":"25"}, {"chave":"Arroz por baixo do feijão","price":"5"}]
biggest_price(menu)