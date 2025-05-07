import operaciones

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Entrada no numérica. Intente de nuevo.")
        continue

    operador = input("Ingrese el operador (+, -, *, /, **, //): ").strip()

    try:
        if operador == '+':
            resultado = operaciones.suma(num1, num2)
        elif operador == '-':
            resultado = operaciones.resta(num1, num2)
        elif operador == '*':
            resultado = operaciones.multiplicación(num1, num2)
        elif operador == '/':
            resultado = operaciones.división(num1, num2)
        elif operador == '**':
            resultado = operaciones.potencia(num1, num2)
        elif operador == '//':
            resultado = operaciones.división_entera(num1, num2)
        else:
            print("Operador inválido. Los operadores válidos son: +, -, *, /, **, //")
            continue

        print(f"El resultado de {num1} {operador} {num2} es {resultado}")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    continuar = input("¿Quieres seguir utilizando la calculadora? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break