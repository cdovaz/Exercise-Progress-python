#Crie uma função que receba uma string como parâmetro e retorne uma nova string na qual todas as vogais são substituídas pelo caractere "#". Em seguida, teste a função com uma string de sua escolha. 
text = input("Insira um texto qualquer aqui")
text = list(text)

for i in range(len(text)):
        if(text[i] == 'a' or text[i] == 'A' ):
                text[i] = '#'
        elif(text[i] == 'e' or text[i] == 'E' ):
                text[i] = '#'
        elif(text[i] == 'i' or text[i] == 'I' ):
                text[i] = '#'
        elif(text[i] == 'o' or text[i] == 'O' ):
                text[i] = '#'
        elif(text[i] == 'u' or text[i] == 'U'):
                text[i] = '#'
        
converted_text = ''.join(text)
print(converted_text)