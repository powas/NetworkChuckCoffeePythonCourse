print("Hola, bienvenido a Braniak Café")
name = input("Como es tu nombre?\n")
if name == "Ben" or name == "Patricia" or name == "Loki":
  evil_status = input("\nSos malvado?\n")
  good_deeds = int(input("\nCuantas cosas buenas hiciste hoy?\n"))
  if evil_status == "si" and good_deeds <= 4:
    print( "\n" + name + ", no sos bienvenido/a en este establecimiento! Fuera!!!")
    exit()
  else:
    print("\nPasá nomas!!!")
else:
  print("\nHola " + name + ", gracias por visitarnos hoy!!!")

beard_length = float(input("\nCuán larga es tu barba?\n"))
if beard_length >= 3:
  print("\nPasá por acá, capo!")
else:
  print("\nBien por vos, volvé al final de la final!")

menu = "Cafe negro, Espresso, Latte, Cappuccino, Frappuccino"
order = input("\nQué te gustaría tomar?\n" + "Menú: " + menu + "\n")
if order == "Frappuccino":
  price = 13
elif order == "Cappuccino":
  price = 12
elif order == "Latte":
  extra_crema = input("\nTe gustaría crema extra?\n")
  if extra_crema == "si":
    price = 11
  else:
    price = 9
elif order == "Espresso":
  price = 10
elif order == "Cafe negro":
  price = 4
else:
  print("No tenemos eso.")
  exit()

quantity = input("\nCuantos quisieras?\n")
total = price * int(quantity)
print("\nGracias, el total es: $" + str(total))
print("\nGenial " + name + ", tu/s " + quantity + " " + order + " estará/n listo/s en unos instantes!!!")