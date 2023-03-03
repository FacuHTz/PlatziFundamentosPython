 # Input del Usuario de su elección 
print("[1] Piedra")   
print("[2] Papel")   
print("[3] Tijeras") 

opcionUsuario = int(input("Escoge tu opción: "))

    # Elección aleatoria de la máquina 
opcionMaquina = random.choice(opciones) 

    # Mostrar elección del usuario (versión visual)  
if opcionUsuario == 1:    
        print("\nTu elegiste Piedra \n")         

elif opcionUsuario == 2:    
        print("\nTu elegiste Papel \n")         

elif opcionUsuario == 3:    
        print("\nTu elegiste Tijeras \n ")     

   # Mostrar eleccioń de la máquina (versión visual)                                              
if opcionMaquina == "Piedra":    
        print ("La computadora eligió Piedra \n")         

elif opcionMaquina == "Papel":    
        print ("La computadora eligió Papel \n")     

elif opcionMaquina == "Tijeras":    
        print ("La computadora eligió Tijeras \n")     

   # Resultados en números para hacer los cálculos pertinentes          

   # Identificar los posibles ganadores con un IF esta vez emplearemos ELIF y ELSE                                     
if (opcionUsuario == 1 and opcionMaquina=="Tijeras" ) or (opcionUsuario == 2 and  opcionMaquina=="Piedra" ) or (opcionUsuario == 3 and 	opcionMaquina == 