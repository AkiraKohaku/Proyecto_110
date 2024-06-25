import random
respuesta=input("¿Desea tirar un dado?: ")

def tirar_dado(respuesta):
    while respuesta == "y":
        no = random.randint(1.6)
    if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            
    elif no == 2:
            print("[-----]")
            print("[     ]")
            print("[  1  ]")
            print("[     ]")
            print("[-----]")

    elif no == 3:
            print("[-----]")
            print("[     ]")
            print("[  2  ]")
            print("[     ]")
            print("[-----]")

    elif no == 4:
            print("[-----]")
            print("[     ]")
            print("[  3  ]")
            print("[     ]")
            print("[-----]")     

    elif no == 5:
            print("[-----]")
            print("[     ]")
            print("[  4  ]")
            print("[     ]")
            print("[-----]")

    else:
            print("[-----]")
            print("[     ]")
            print("[  5  ]")
            print("[     ]")
            print("[-----]")
    
    respuesta= input("Presiona y para rodar de nuevo,presiona n para salir")
    

tirar_dado(respuesta)