import random

usuarios=["donramon","goku","saitama","luffy","ichigo","gon","eren","shinji","sakura","ranma"]
cuentas=[]

#Funcion que crea cuentas de usuario en diccionarios
def crear_cuenta(user,dic):
    for i in user:
        clave=crear_contrasena()
        #Agregar teléfonos de usuarios
        while True:
            telefono=int(input(f"agregue su numero de telefono para {i}  con 8 digitos(********): ").strip())
            if len(str(telefono))!=8:
                print("es incorrecto vuelva a ingresar el numero de telefono")
            else :
                break        

        cuenta={"nombre": i,
                "pasaword":clave,
                "telefono":str(telefono)}
        
        dic.append(cuenta)
    
    return dic

#Funcion que crea contraseña con los parametros requeridos
def crear_contrasena():
    contrasena=[]
    caracter_minusculas=list("abcdefghijklmnopqrstuvwxyz")
    caracteres_mayusculas=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digitos=list("0123456789")
    cantidad_min=random.randint(3,6)
    cantidad_may=random.randint(1,3)
    cantidad_dig=random.randint(2,4)

    
    contrasena+=[random.choice(caracter_minusculas) for i in range(cantidad_min)]
        
  
    contrasena+=[random.choice(caracteres_mayusculas)for i in range(cantidad_may)]
 

    contrasena+=[random.choice(digitos)for i in range(cantidad_dig)]

    random.shuffle(contrasena)
    contrasena_str="".join(contrasena)
    

    return contrasena_str


#Ejecutando función
cuentas=crear_cuenta(usuarios,cuentas)
print(cuentas)