registros = int(input('Ingrese cuantas personas se van a registrar: '))
for i in range(registros):
    print (i)
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Y por último ingrese su edad: '))
    while (edad <= 0) or (edad > 120):
        edad = int(input('Ingrese una edad valida: '))

    if edad < 18:
        condicion = ('menor')
    elif edad  < 65:
        condicion = ('mayor')
    elif edad <= 120:
        condicion = ('jubilado')

    print('Su nombre es '+nombre+' '+apellido+' '+'y usted es '+condicion)
