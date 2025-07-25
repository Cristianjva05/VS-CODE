print ("calculadora");

print ("+ = 1");

print ("- = 2");

print ("* = 3");

operacion = int (input("operacion a realizar:"));

numero = int (input("numero 1:"));

numero2 = int (input("numero 2:"));

if operacion == 1:
    print (numero+numero2)
elif operacion == 2:
    print (numero-numero2)
