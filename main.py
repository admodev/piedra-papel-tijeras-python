import random
elecciones = ["Piedra", "Papel", "Tijera"]

def piedraPapelTijera():
  print("Elige...  \n Piedra, Papel o Tijera")
  eleccionUsuario = input()

  if eleccionUsuario == "Piedra" or eleccionUsuario == "Papel" or eleccionUsuario == "Tijera":
    eleccionIa = random.choice(elecciones)
  else:
    print("Por favor, elige: Piedra, Papel o Tijera")

  if eleccionUsuario == "Piedra" and eleccionIa == "Tijera":
    print("Ganaste! (usuario: Piedra, IA: Tijera)")
  elif eleccionUsuario == "Tijera" and eleccionIa == "Piedra":
    print("Gano la IA! (usuario: Tijera, IA: Piedra)")
  elif eleccionUsuario == "Papel" and eleccionIa == "Piedra":
    print("Ganaste! (usuario: Papel, IA: Piedra")
  elif eleccionUsuario == "Piedra" and eleccionIa == "Papel":
    print("Gano la IA! (usuario: Piedra, IA: Papel)")
  elif eleccionUsuario == "Papel" and eleccionIa == "Tijera":
    print("Gano la IA! (usuario: Papel, IA: Tijera")
  elif eleccionUsuario == "Tijera" and eleccionIa == "Papel":
    print("Ganaste! (usuario: Tijera, IA: Papel)")

piedraPapelTijera()

while True:
  piedraPapelTijera()
