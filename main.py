'''
Crear un programa que almacene una lista de clientes. Cada cliente tiene su nombre, apellido y número de DNI. El programa tendrá el siguiente menú de opciones: 

1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir

Para cada opcion del menu se realizará con una función
'''

#Función creada para almacenar clientes dentro de un conjunto que contendrá los datos del cliente y que luego será almacenado dentro de una lista.__name__

def almacenar_cliente(lista_clientes, nombre, apellido, dni):
  diccionario_cliente = {} #Creo conjunto para almacenar los clientes
  diccionario_cliente["Nombre"] = nombre
  diccionario_cliente["Apellido"] = apellido
  diccionario_cliente["DNI"] = dni
  lista_clientes.append(diccionario_cliente) #Almaceno la información contenido en el conjunto en la lista creada


#Función creada para mostrar clientes

def mostrar_clientes(lista_clientes):
  for i in lista_clientes:
    print(f"Nombre: {i['Nombre']}")
    print(f"Apellido: {i['Apellido']}")
    print(f"DNI: {i['DNI']}")
    print() 


#Función creada para mostrar clientes por número de DNI

def cliente_dni(lista_clientes, dni):
  for i in lista_clientes: #El iterador en cada vuelta mostrará el conjunto creado con los datos del cliente
      if i["DNI"] == dni: #si el valor de la clave coincide con el dato ingresado por el usuario entonces imprimirá el valor de cada clave indicada
        print(f"Nombre: {i['Nombre']}")
        print(f"Apellido: {i['Apellido']}")
        print(f"DNI: {i['DNI']}")
        print()
      else:
        print("El cliente identificado con el número de dni ingreseado no existe en la base de datos")

#Función creada para eliminar un cliente de la lista de clientes

def borrar_cliente(lista_clientes, borrar):
  for i in lista_clientes:
      if i["DNI"] == borrar:
        lista_clientes.remove(i)
        return True
  return False

        
lista_clientes = [] #Creamos una lista vacía para luego completar con la información contenida en el conjunto creado

while True:

  #Creamos menú de opciones
  print('''
  \t\tLISTA DE CLIENTES
  
  1. Agregar nuevo cliente
  2. Mostrar todos los clientes
  3. Mostrar cliente por DNI
  4. Eliminar cliente
  5. Salir
  ''') #Print multilinea 
  
  opcion = int(input("Elija una opción ")) #Le pedimos al usuario que ingrese una opción del menu
  print() #Salto de línea
  
  if opcion == 1:
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    dni = input("Ingrese el número de DNI del cliente: ")

    #Llamamos a la función que recogerá la información ingresada por el usuario y la agregará a la lista. Para ello le pasamos como argumentos el nombre de la lista y las variables con la información ingresada por el usuario

    almacenar_cliente(lista_clientes, nombre, apellido, dni) 

 
  elif opcion == 2:
    print("\t\tLISTA DE CLIENTES ALMACENADOS")
    print()
    mostrar_clientes(lista_clientes)
    

  elif opcion == 3:

    #Solicitamos el ingreso del nº de dni del cliente
    
    dni = input("Ingrese el número de DNI del cliente que desea mostrar: ")
    print()
    cliente_dni(lista_clientes, dni)
 
       
  elif opcion == 4:
    borrar = input("Ingrese el número de dni del cliente que desea eliminar: ")
    print()

    if borrar_cliente(lista_clientes, borrar):
      print("Cliente eliminado")
    else:
      print("No se encontró ningún cliente")
       
  elif opcion == 5:
    print("Gracias por utilizar nuestros servicios!")
    break
    
  else:
    print("Ha ingresado una opción inválida. Por favor digite un número del 1 al 5: ")
    print()
  

    
