class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.salario += ((percentual / 100) * self.salario)
        else:
            print('Erro: A porcentagem de aumento não pode ser menor que zero.')
            
    def mostrar_dados(self):
        print(f'Nome: {self.nome}\nCargo: {self.cargo}\nSalário: R$ {self.salario:.2f}')
        
    def bonus(self, valor):
        self.salario += valor
        
class Desenvolvedor(Funcionario):
    def programar(self):
        print(f"{self.nome} está programando em Python")
        
class DesenvolvedorSenior(Desenvolvedor):
    def revisar_codigo(self):
        print(f'{self.nome} está revisando o código da equipe')
        
class Gerente(Funcionario):
    def dar_aumento(self, funcionario, percentual):
        funcionario.aumentar_salario(percentual)
        print(f"{self.nome} deu {percentual}% de aumento para {funcionario.nome}")

# Usando Herança múltipla
class Artista():
    def __init__(self, nome):
        self.nome = nome

    def desenhar(self):
        print(f"{self.nome} está desenhando o personagem")

class Programador():
    def __init__(self, nome):
        self.nome = nome
    
    def programar(self):
        print(f"{self.nome} está programando")

class GameDev(Artista, Programador):
    pass

# Teste do código

func1 = Funcionario("Arthur", 3000, "Desenvolvedor")

func1.mostrar_dados()

print()

func1.aumentar_salario(10)
func1.mostrar_dados()

print()

func1.bonus(500)
func1.mostrar_dados()

print()

dev1 = Desenvolvedor("Arthur", 3000, "Desenvolvedor")
gerente1 = Gerente("Ana", 5000, "Gerente")

dev1.programar()
gerente1.dar_aumento(dev1, 10)
dev1.mostrar_dados()

print()

dev_senior1 = DesenvolvedorSenior('Arthur', 3000, 'Desenvolvedor Sênior')
dev_senior1.revisar_codigo()

print()

dev = GameDev('Arthur')

dev.desenhar()
dev.programar()