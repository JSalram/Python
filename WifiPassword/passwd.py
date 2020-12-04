import subprocess

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("UTF-8").split("\n")

wifis = [line.split(":")[1][1:-1] for line in data if "Perfil de todos los usuarios" in line]

passwd = []
for wifi in wifis:
    result = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ISO-8859-1").split("\n")
    passwd += [line.split(":")[1][1:-1] for line in result if "Contenido de la clave" in line]

for i in range(len(wifis)):
    print(f"Nombre: {wifis[i]}, Contraseña: {passwd[i]}")
