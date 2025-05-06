usuarios = {"iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},"fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},"aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"}}

intentos = 3
while intentos > 0:
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    if user in usuarios and usuarios[user]["password"] == pwd:
        print(f"Bienvenido/a {usuarios[user]['nombre']} {usuarios[user]['apellido']}")
        break
    else:
        intentos -= 1
        print(f"Datos incorrectos. Intentos restantes: {intentos}")
else:
    print("Acceso denegado.")