#Crie uma classe chamada Shape (Forma) que tenha um método chamado area (área) que retorna a área da forma. 
# Em seguida, crie duas subclasses chamadas Rectangle (Retângulo) e Circle (Círculo) que herdam da classe Shape. 
# Implemente os métodos area nas subclasses de forma adequada. Teste suas classes criando instâncias de Rectangle e Circle e exibindo suas áreas.
class Shape():
    def __init__(self) -> None:
        pass

    def area(self, tipo, raio_ou_altura, largura):
        if tipo == 1:
            return (raio_ou_altura * largura)
        elif tipo == 2:
            return (3.14 * raio_ou_altura * raio_ou_altura)
        else:
            return "Tipo não disponível"


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
class Circle(Shape):
        def __init__(self):
                super().__init__()

x = int(input("Insira o tipo de área que você deseja calcular\nRetângulo - 1\nCirculo - 2\n"))
if x == 1:
    y, z = input("Insira a altura e a largura do retângulo").split()
    y = int(y)
    z = int(z)
    rectangle = Rectangle()
    print(rectangle.area(x, y, z))
elif x == 2:
        y = input("Insira o raio do circulo")
        y = int(y)
        circle = Circle()
        print(f"{circle.area(x,y, 0):.3f}")
        