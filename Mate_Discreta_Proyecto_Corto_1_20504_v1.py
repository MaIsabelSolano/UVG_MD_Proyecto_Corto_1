# Universidad del Valle de Guatemala
# MM2015 Matemática discreta 1
# Proyecto corto 1 - funciones
# Maria Isabel Solano Bonilla 20504

Loop = True

def NumsAleatorios (n, a, c, m, s):
    n = n -1
    if n > 0:
        r = (a*NumsAleatorios((n-1),a,c,m,s)+c)%m
        print (r)
    else:
        print ("Algoritmo terminado...")


# Inicio del menu
while Loop:
    try:
        print("\n¿Qué función desea utilizar?\n1)Función de dispersión\n2)Generar números pseudoaleatorios\n2)Salir del programa")
        Menu = int(input("Ingrese el número de la función que desea utilizar: "))
        
        if Menu == 1:
            # Función de dispersión
            print ("\n  Eligió Función de dispersión\n")
            
            # Pedir el arreglo
            mod = int(input("¿Qué módulo desea utilizar?: "))
            
            # Hay que pedir la cantidad de números pero esta no puede superar al número de módulo
            #verificador = True
            #while verificador:
            #    cant = int(input("Ingese la cantidad de números que desea ingresar (debe ser menor que el número de módulo): "))
            #    if cant > mod:
            #        print ("Por favor ingrese una cantidad válida")
            #    if cant <= mod:
            #        # Se puede continuar
            #        verificador = False
            # Ya no es necesaria esta parte porque siempre se va a ingresar un array con la cantidad de elementos del módulo
                    
            Numeros = [None]*mod #Originalmente decía *cant
            i = 0
            print ("Ingrese los números que desee ordenar (deben ser mayores al módulo ingresado)")
            while i<mod:
                #revisar que sea más pequeño
                verificador = True
                while verificador:
                    num = int(input(f"Ingrese el número no. {i+1}: ")) # num = número ingresado por el usuario
                    
                    # Ingresar mun al array ya ordenado
                    if num>=mod:
                        # Se puede utilizar, se ordena en el hash
                        m = num%mod
                        if Numeros[m] == None:
                            # Se ingresa ahí
                            Numeros[m] = num
                            print (f"{num} ingresado...")
                            verificador = False # Salir el loop de verificación
                        elif Numeros[m] != None:
                            # Hubo un choque
                            verificador2 = True
                            while verificador2:
                                # Se repite el loop hasta que se ingrese el valor en alguna posicion
                                m = m + 1
                                if m >= mod:
                                    # Se regresa al inicio para que busque en las primeras posiciones
                                    m = 0
                                # Ingresar o no
                                if Numeros[m] == None:
                                    # Se guarda ahí
                                    Numeros[m] = num
                                    print (f"{num} ingresado....")
                                    #verificador2 = False # Salir del loop de colisiones
                                    verificador = False # Salir del loop de verificaión
                                    break
                                if Numeros[m] != None:
                                    # Se repite el loop
                                    verificador2 = True
                        
                    if num<mod:
                        # Se debe repetir
                        print ("El valor ingresado no es válido")
                    
                i = i+1
            print(Numeros)
            
            
        if Menu == 2:
            # Generador de números pseudoaletorios
            print ("\n  Eligió Generador de Pseudoaleatorios\n")
            
            #pedir módulo, tiene que ser mayor a 2
            mod = 0
            verificador = True
            while verificador:
                mod = int(input("¿Qué módulo desea utilizar? (Debe ser mayor o igual a 2): "))
                if mod >= 2:
                    verificador = False
                elif mod < 2:
                    print("Ingrese un número válido")
                    # Se repite el loop
            
            # Pedir n
            n = 0
            verificador = True
            while verificador:
                n = int(input("¿Cuántos números desea generar?: "))
                if n >= 1:
                    verificador = False
                elif n < 1:
                    print("Ingrese un número válido")
                    # Se repite el loop
                    
            # Pedir multiplicador
            a = 0
            verificador = True
            while verificador:
                a = int(input("Ingrese un multiplicador: "))
                if a >= 2 and a <= mod:
                    verificador = False
                elif a < 2 or a > mod:
                    print("Ingrese un número válido")
                    # Se repite el loop
                    
            # Pedir incremento
            c = 0
            verificador = True
            while verificador:
                c = int(input("Ingrese un incremento: "))
                if c >= 0 and c <= mod:
                    verificador = False
                elif c < 0 or c > mod:
                    print("Ingrese un número válido")
                    # Se repite el loop
                    
            # Pedir incremento
            s = 0
            verificador = True
            while verificador:
                s = int(input("Ingrese una semilla: "))
                if s >= 0 and s <= mod:
                    verificador = False
                elif s < 0 or s > mod:
                    print("Ingrese un número válido")
                    # Se repite el loop
            
            NumsAleatorios(n,a,c,mod,s)
            

        if Menu == 3:
            # Salir del programa
            print ("\n  Gracias por utilizar el programa\n")
            Loop = False
        
        if Menu != 1 and Menu != 2 and Menu != 3:
            # Si no es ninguna de la anteriores, impimir mensaje de erro y repetir el loop
            print ('\nLa opción que eligió no existe\n')
        
    except ValueError:
        print ('El valor ingresado no es válido')


        
