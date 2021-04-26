nombre = input('Hola, ingrese su nombre: ')
apellido = input('También ingrese su apellido: ')
edad = input('Y por último, ingrese su edad: ')
edad = int(edad)
#tambien funciona de la siguiente manera
#edad = int(input('Y por último, ingrese su edad: '))
if edad < 18:
    condicion = ('menor')
elif edad < 65:
    condicion = ('mayor')
elif edad < 120:
    condicion = ('jubilado')
else:
    condicion = ('cadaver')

print('Su nombre es: '+nombre+' '+apellido+' y usted es: '+condicion)
print ('Su nombre es: {} {} y usted es {}'.format(nombre,apellido,condicion))
