# num = 65
# if type(num) == int:
#     print("Resultado:", num * 2)
# else:
#     print("Este dato NO es numérico.")

# def sms(men):
#     print(men)


# sms("Programa #1.")
# sms("Programa #2.")


# class Sintax:
#     def usoVariable(self):
#         edad, _peso = 70, 51.62
#         print("Edad de la persona: {}".format(edad))
#         print("Peso de la persona: {}".format(_peso))


# ej2 = Sintax()
# ej2.usoVariable()


class Sintax:
    instan = 0
    def __init__(self, data = "Incializando..."):
        self.palabra = data

    def usoVariables(self):
        edad, _peso = 21, 56.75
        nombre = "Nohelia Brito"
        tipoSex = "Femenino"
        civilCasada = True
        print("Nombre: {}".format(nombre))
        print("Edad: {}".format(edad))
        print("Tipo de Sexo: {}".format(tipoSex))
        print("Estado Civil Casada: {}".format(civilCasada))
        print("Peso: {}".format(_peso))
