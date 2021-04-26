#print("Hola mundo")
#edad=21
#print(edad)
for i in range(0,3):
#for i in range(3)
#for i in range(1,10,3) hace de 3 en 3
#for i in range(10,1,-1) esto va disminuyendo de uno en uno
    print(i)
    edad = input('Digame su edad: ')
    print(edad)
    #print(type(edad))
    edad = int(edad)
    #if edad >= 18:
    #    print('Usted es mayor de edad')
    #    if edad == 65:
    #        print('Prepare sus tramites de jubilación')
    #if edad < 18:
    #    print('Usted es menor de edad')
    #else:
    #    print('Usted es menor de edad')

    if edad < 0:
        print('Usted no nació')
    elif edad < 18:
        print('Usted es menor de edad')
    elif edad < 65:
        print('Usted es mayor de edad')
    elif edad < 120:
        print('Usted es jubilado')
    else:
        print('Usted está en el otro mundo')
        #break corta el ciclo, por mas que debiera seguir. Para cuando hay una determinada condicion
else:
    print('Proceso de carga finalizado')

    a ='hola '
    b = 'mundo'
    print(a+b)
