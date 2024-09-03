
#almacenamiento de recetas
def almacenamiento(recetario):

    recetas={
        "milanesa de pollo":["pollo","pan molido", "huevo"],
        "vin chaud":["vino", "anis"]
        #aquí se agregan las recetas
        #incluir función para integrar una base de datos o guardar la información en .csv
    }  
     
    #print(recetas.keys())   
    recetario.update(recetas)
    return recetario


#buscar recetas con ingredientes específicos
def ingredients(recetario, ingredientes):#si agregas un * al principio de la variable se vuelve dinámico
    ingredientes_busqueda = [ingrediente.strip() for ingrediente in ingredientes.split(",")]
    
    print(f"Buscando recetas con {ingredientes_busqueda}...")
    
    print("■■□□□□□□□□ ")
    print("■■■■□□□□□□ ")
    print("■■■■■■■■□□ ")
    print("■■■■■■■■■■ ")
    
    none = True
    for key, value in recetario.items():
        if all(ingrediente in value for ingrediente in ingredientes_busqueda):
            print(f"Las recetas con {ingredientes_busqueda} son: {key.title()}")
            none = False
    
    if none is True:
        print(f"No hay recetas con {ingredientes_busqueda}")

        choice=input("¿Desea agregar una receta? s/n ")
        
        if choice == "s":
            receta=input("Nombre de la receta: ")
        
            ingredientes=input("Introduzca los ingredientes separados por comas:  ")
        
            add(recetario, receta, ingredientes)

    
#buscar recetas sin cosas específicas
def without(recetario, ingredientes):
    ingredientes_busqueda = [ingrediente.strip() for ingrediente in ingredientes.split(",")]
    
    print(f"Buscando recetas sin {ingredientes_busqueda}...")
    
    print("■■□□□□□□□□ ")
    print("■■■■□□□□□□ ")
    print("■■■■■■■■□□ ")
    print("■■■■■■■■■■ ")
    
    for key, value in recetario.items():
        if not all(ingrediente in value for ingrediente in ingredientes_busqueda):
            print(f"Las recetas sin {ingredientes_busqueda} son: {key.title()}")    
       
#buscar receta
def search(recetario, recipe):
    print(f"Busqueda de {recipe.capitalize()}...")
    print("■■□□□□□□□□ ")
    print("■■■■□□□□□□ ")
    print("■■■■■■■■□□ ")
    print("■■■■■■■■■■ ")
    
    for key, value in recetario.items():
        if key.lower()==recipe:
            print(f"{recipe.capitalize()} tiene:  {value.capitalize()}.")
    
def add(recetario, receta, ingredientes ):
    #quita los espacios y divide cada que ve un espacio
    list_ingredientes=[ingrediente.strip() for ingrediente in ingredientes.split(",")]

    nueva_receta= {receta: list_ingredientes}
    
    recetario.update(nueva_receta)
    
    print("■■□□□□□□□□ ")
    print("■■■■□□□□□□ ")
    print("■■■■■■■■□□ ")
    print("■■■■■■■■■■ ")
    print("Agregada con éxito!!")
    print(f"\n {recetario.capitalize()}")
             

    
#main menu
def main():
    
    #alamcenamiento
    
    recetario={}
    
    # with open("Recetario.txt") as file:
    #     file.write(f"{recetario}\n")
    
    print("\n// Recetario //\n")
    
    
    
    # Llamada para inicializar el recetario
    
    print("""Menu:
          1- Buscar recetas con..
          2- Buscar recetas sin...
          3- Buscar ingredientes de una receta
          4- Agregar receta
          5- Ver recetas disponibles
          6- Salir
          """)
    menu=int(input("Opción escogida: "))
    
    while True:
        if menu == 1:
            buscar=input("¿Qué ingrediente(s) debe tener? ")
            ingredients(recetario, buscar)
            
        if menu == 2:
            buscar=input("¿Qué ingrediente(s) no debe tener? ")
            without(recetario, buscar)
            
        elif menu == 3:
            #imprimir recetas disponibles para buscar ingredientes
            buscar=input("Busca tu receta: ").lower()
            search(recetario, buscar)
            
        elif menu == 4:

            choice="s"
            while choice == "s":
                receta=input("Nombre de la receta: ")
                
                ingredientes=input("Introduzca los ingredientes separados por comas:  ")
                
                add(recetario, receta, ingredientes)
                
                choice=input("Agregar otra receta?  s/n  ")
            
        
        elif menu == 5:
            print("\n## Recetas en el recetario ##")
            #omitimos el value poniendo underscore porque no usaremos el valor
            for key, _ in recetario.items(): #necesito que divida los elementos así que el error de value no lo podré quitar
                print(f">>{key.capitalize()}")
                
    
        if menu == 6:
            break
        
        else:
            print("Opción no disponible")
            
        menu=int(input("""\n ¿Qué hacemos ahora?
            Elige una opción:"""))
        
    recetario=almacenamiento(recetario)
        
    print("Nos vemos luego!!")
    
    
if __name__=="__main__":
    main()
