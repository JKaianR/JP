

# Función para parar el programa en cada una de las opciones
def parar():
    input("Presione <ENTER> para continuar")


# Función que permite capturar los números que serán objetos de la operación
def capturar():
    try:
        T = float(input("Por favor digite la temperatura: "))
        return T
    except Exception as ex:
        print(ex)


def celsiusFahrenheit(C):
    # F = (C * 9/5) + 32
    return (C * 9 / 5) + 32


def celsiusKelvin(C):
    # K = C + 273.15
    return C + 273.15


def kelvinFahrenheit(K):
    # F = (K - 273.15) * 9/5 + 32
    return (K - 273.15) * 9 / 5 + 32


def kelvinCelsius(K):
    # C = K - 273.15
    return K - 273.15


def fahrenheitKelvin(F):
    # K = (F - 32) * 5/9 + 273.15
    return (F - 32) * 5 / 9 + 273.15


def fahrenheitCelsius(F):
    # C = (F - 32) * 5/9
    return (F - 32) * 5 / 9


def main():
    try:
        continuar = True
        T = 0
        while continuar:
            opcion = input(
                "Seleccione una opción:"
                + chr(13)
                + "\n"
                + "1-> Capturar Temperatura"
                + chr(13)
                + "2-> Celsius a Fahrenheit"
                + chr(13)
                + "3-> Celsius a Kelvin"
                + chr(13)
                + "4-> Kelvin a Fahrenheit"
                + chr(13)
                + "5-> Kelvin a Celsius"
                + chr(13)
                + "6-> Fahrenheit a Kelvin"
                + chr(13)
                + "7-> Fahrenheit a Celsius"
                + chr(13)
                + "0-> Salir"
            )
            if opcion == "1":
                T = capturar()
            elif opcion == "2":
                print(f"{T}°C = {celsiusFahrenheit(T)} °F")
                parar()
            elif opcion == "3":
                print(f"{T}°C = {celsiusKelvin(T)} °K")
                parar()
            elif opcion == "4":
                print(f"{T}°K = {kelvinFahrenheit(T)} °F")
                parar()
            elif opcion == "5":
                print(f"{T}°K = {kelvinCelsius(T)} °C")
                parar()
            elif opcion == "6":
                print(f"{T}°F = {fahrenheitKelvin(T)} °K")
                parar()
            elif opcion == "7":
                print(f"{T}°F = {fahrenheitCelsius(T)} °C")
                parar()
            elif opcion == "0":
                print("Byw")
                continuar = False
            else:
                print("Seleccione una opción valida")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()







