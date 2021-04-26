nombre = input('Nombre: ')
adivinar = ''
oportunidades = 6
while nombre != adivinar:
    oportunidades -=1
    print('Oportunidades '+str(oportunidades))
    adivinar = input('Adivine el nombre: ')
    if oportunidades == 0:
        print('Perdiste')
        break
else:
    print('Adivinó!!')
