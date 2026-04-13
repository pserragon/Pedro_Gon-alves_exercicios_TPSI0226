# exception e um erro que ocorre em runtime e existe 

total=10/0 # zerodivisionerror

num=int("abc") # valueerror
lista = [1,2,3,4]

# print(lista[4])  # IndexError

n1 = int(input("introduz num: "))

try:
    total = 10 / n1
    print("Resultado:", total)
except ZeroDivisionError:
    print("Temos um ZeroDivisionError pois não podes dividir por 0")
except ValueError:
    print("Erro: tens de introduzir um número válido")

# total = 10 / 0  # ZeroDivisionError

# num = int("abc")  # ValueError

# Base 8: 0-7
# Base 16: 0-9 e A-F

char = str(1)

print(char)        # '1'
print(ord("1"))    # código ASCII de '1'
print(chr(65))     # letra correspondente ao código 65



try:
    result = int(string)
    print("Número convertido:", result)
except ValueError as erro:
    print("o erro e ", erro)


else:
    print("nao existe error:")

idade=10
if idade<0:
    raise ValueError("idade nao pode ser negativa")

else:
    print("idade certa")

except ValueError as erroridade:
     print (erroridade)


# total = 10 / 0  # ZeroDivisionError

# num = int("abc")  # ValueError
# Base 10: 0123456789
# Base 8: 01234567
# Base 16: 0123456789ABCDEF
# Base 2: 01

char = str(1)

print(char)        # '1'
print(ord("1"))    # 49
print(chr(65))     # 'A'