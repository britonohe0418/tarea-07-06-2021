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


# class Sintax:
#     instan = 0
#     def __init__(self, data = "Incializando..."):
#         self.palabra = data

#     def usoVariables(self):
#         edad, _peso = 21, 56.75
#         nombre = "Nohelia Brito"
#         tipoSex = "Femenino"
#         civilCasada = True
#         print("Nombre: {}".format(nombre))
#         print("Edad: {}".format(edad))
#         print("Tipo de Sexo: {}".format(tipoSex))
#         print("Estado Civil Casada: {}".format(civilCasada))
#         print("Peso: {}".format(_peso))


# ej3 = Sintax()
# print(ej3.palabra)
# ej3.usoVariables()


class Sintax:
    instan = 0
    def __init__(self, data = "Iniciando..."):
        self.frase = data

    def usoVariables(self):
        edad, _peso = 21, 56.75
        nombre = "Nohelia Brito"
        tipoSex = "Femenino"
        civilCasada = True
        # print("Nombre: {}".format(nombre))
        # print("Edad: {}".format(edad))
        # print("Tipo de Sexo: {}".format(tipoSex))
        # print("Estado Civil Casada: {}".format(civilCasada))
        # print("Peso: {}".format(_peso))
        
        # DATOS DE TIPO TUPLA
        user = ()
        user = ("Nohe0418", 2105, "anonymous", True)
        
        # DATOS DE TIPO LISTA
        materias = []
        materias = ["Programacion Web", "PHP", "Ruby"]
        materias[1] = "Python"
        materias.append("Go")

        # DATOS DE TIPO DICCIONARIO
        docente = {}
        docente = {"Nombre": "María", "Edad": 26, "Fac.": "FACI"}
        docente["Carrera"] = "CS"
        
        # PRINT FORMAT
        # print("""Me llamo {}, y tengo {}
        #          años""".format(nombre, edad))
        
        # SLICES OF WORDS
        print(user, materias, docente)
        print(user, user[0], user[0:2], user[-1])
        print(materias, materias[2:], materias[:1], materias[::], materias[-2:])
        print(docente, docente["Nombre"])
