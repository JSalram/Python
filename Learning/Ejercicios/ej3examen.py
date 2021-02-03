class Equipos:
    def __init__(self):
        self.equipos = []
        self.cantidades = []
        self.alquilados = []
        self.usuarioAlquiler = {}
        self.rellenaEquipos()
    
    def rellenaEquipos(self):
        self.equipos += ["Kayak", "Windsurf", "Bicicleta de montaña", "Quad", "Kite-surf"]
        self.cantidades += [4, 2, 3, 1, 3]
        self.alquilados += [0, 0, 0, 0, 0]

    def alquilaEquipo(self, usuario, i):
        i -= 1
        if i < len(self.equipos) and self.cantidades[i] > 0 and usuario not in self.usuarioAlquiler:
            self.usuarioAlquiler[usuario] = self.equipos[i]
            self.cantidades[i] -= 1
            self.alquilados[i] += 1
            return True
        else:
            return False

    def compruebaAlquilados(self):
        for usuario in self.usuarioAlquiler:
            print("Alquiler de {}: {}".format(usuario, self.usuarioAlquiler[usuario]))

    def __str__(self):
        cad = ""
        for i in range(len(self.equipos)):
            cad += str(self.equipos[i]) + " restantes: " + str(self.cantidades[i])
            if i < len(self.equipos)-1:
                cad += "\n"

        return cad


class Usuarios:
    def __init__(self):
        self.usuarios = []
        self.contrasennas = []
        self.rellenaUsuarios()

    def rellenaUsuarios(self):
        self.usuarios += ["juan13", "mermile45", "sorledo2", "miriam25"]
        self.contrasennas += ["1234", "abcd", "a1b2c3", "2930"]

    def registraUsuario(self, usuario, contrasenna):
        if usuario not in self.usuarios:
            self.usuarios += [usuario]
            self.contrasennas += [contrasenna]
            return True
        else:
            return False

    def compruebaUsuario(self, usuario, contrasenna):
        if usuario in self.usuarios:
            i = self.usuarios.index(usuario)
            return self.contrasennas[i] == contrasenna
        else:
            return False

    
class Encargados:
    def __init__(self):
        self.usuarios = []
        self.contrasennas = []
        self.rellenaEncargados()

    def rellenaEncargados(self):
        self.usuarios += ["jorge", "cristobal", "ana"]
        self.contrasennas += ["1234", "wasd", "nana"]

    def compruebaEncargado(self, usuario, contrasenna):
        if usuario in self.usuarios:
            i = self.usuarios.index(usuario)
            return self.contrasennas[i] == contrasenna
        else:
            return False


servidor = Usuarios()
equipos = Equipos()
encargados = Encargados()
seguir = True

print("Gestor de alquiler de ocio en la costa")

while seguir:
    print()

    print("¿Qué desea hacer?")
    print("1. Iniciar sesión como encargado         2. Iniciar sesión como cliente")
    print("3. Salir")
    opcion = input("Opción: ")

    try:
        opcion = int(opcion)
    except:
        print("Opción incorrecta.")
        break

    if opcion == 1:
        usuario = input("Introduzca su usuario: ")
        contrasenna = input("Introduzca su contraseña: ")

        if encargados.compruebaEncargado(usuario, contrasenna):
            print("Bienvenido {}\n".format(usuario))

            print("¿Qué desea hacer?")
            print("1. Comprobar existencias         2. Comprobar equipos alquilados")
            opcion = input("Opción: ")

            try:
                opcion = int(opcion)
            except:
                print("Opción incorrecta.")
                break
            
            if opcion == 1:
                print(equipos)
            elif opcion == 2:
                equipos.compruebaAlquilados()
            else:
                print("Opción incorrecta.")

        else:
            print("Usuario o contraseña incorrectos.")

    elif opcion == 2:
        usuario = input("Introduzca su usuario: ")
        contrasenna = input("Introduzca su contraseña: ")

        if servidor.compruebaUsuario(usuario, contrasenna):
            print("Bienvenido {}\n".format(usuario))

            print("¿Qué desea alquilar?")
            print("1. Kayak                     2. Windsurf")
            print("3. Bicicleta de montaña      4. Quad")
            print("5. Kite-Surf")
            opcion = input("Opción: ")

            try:
                opcion = int(opcion)
            except:
                print("Opción incorrecta.")
                break
            
            if 1 <= opcion <= 5:
                if equipos.alquilaEquipo(usuario, opcion):
                    print("Equipo alquilado con éxito. Recuerde que dispone de un día completo máximo para su uso.")

                else:
                    print("No disponemos en este momento de este equipoo ya dispone de un equipo alquilado. Inténtelo más tarde.")

            else:
                print("Opción incorrecta")

        else:
            print("Usuario o contraseña inexistente. ¿Desea registrarse?")
            opcion = input("s/n: ")

            while opcion != "s" and opcion != "n":
                opcion = input("Opción incorrecta. Vuelva a intentarlo (s/n): ")

            if opcion == "s":
                usuario = input("Indique un usuario: ")
                contrasenna = input("Indique una contraseña: ")

                while not servidor.registraUsuario(usuario, contrasenna):
                    print("Usuario ya existente. Pruebe de nuevo")
                    usuario = input("Usuario: ")
                    contrasenna = input("Contraseña: ")

                print("Usuario ({}) registrado con éxito".format(usuario))

            else:
                print("¡Hasta luego!")
    
    elif opcion == 3:
        print("¡Hasta luego!")
        seguir = False
    
    else:
        print("Opción incorrecta.")