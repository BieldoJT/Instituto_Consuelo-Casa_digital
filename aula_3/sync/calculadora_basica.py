#!/usr/bin/python3

def soma(a, b):
     print(a,'+',b,'=',a+b)

def subtracao(a, b):
    print(a,'-',b,'=',a-b)

def multi(a, b):
     print(a,'*',b,'=',a*b)

def divisao(a, b):
    if b == 0:
        print("Não existe divisão por zero!!")
    else:
         print(a,'/',b,'=',a/b)

def calculadora(num1, num2):
    soma(num1, num2)
    subtracao(num1, num2)
    multi(num1, num2)
    divisao(num1, num2)


if __name__ == "__main__":
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Dgite outro numero: "))
    except:
        print("Voce deve adicionar um numero!!")
    else:
        calculadora(num1, num2)