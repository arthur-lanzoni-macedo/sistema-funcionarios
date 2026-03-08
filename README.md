# Sistema de Funcionários em Python

Projeto desenvolvido em **Python** para praticar conceitos de **Programação Orientada a Objetos (POO)**.

## Conceitos aplicados

- Classes e Objetos
- Encapsulamento
- Herança
- Herança múltipla
- Métodos de classe

## Estrutura do Projeto

O sistema simula um ambiente simples de empresa com diferentes tipos de funcionários.

### Classes criadas

**Funcionario**

- Classe base com atributos:
  - nome
  - salário
  - cargo
- Métodos:
  - `aumentar_salario()`
  - `mostrar_dados()`
  - `bonus()`

---

**Desenvolvedor**

- Herda de `Funcionario`
- Método:
  - `programar()`

---

**DesenvolvedorSenior**

- Herda de `Desenvolvedor`
- Método:
  - `revisar_codigo()`

---

**Gerente**

- Herda de `Funcionario`
- Pode dar aumento para outros funcionários

## Herança Múltipla

Também foi criado um exemplo de herança múltipla:

Classes:
- Artista
- Programador

Classe final:
`GameDev`

Que herda comportamentos de ambas.

---

## Exemplo de execução

Nome: Arthur  
Cargo: Desenvolvedor  
Salário: R$ 3000.00

---

## Objetivo

Este projeto foi criado para praticar conceitos fundamentais de **POO em Python**, importantes para desenvolvimento de software, automação e aplicações em dados.

---

## Autor

Arthur Lanzoni Macedo
