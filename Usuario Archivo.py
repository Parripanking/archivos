class USUARIO():
	def __init__(self,nombre,apellido,correo,contraseña):
		self.apellido = apellido
		self.contraseña = contraseña
		self.correo = correo
		self.nombre = nombre
	def guardarenelarchivo(self):
		archivo = open('registro.txt','a')
		archivo.write('''Nombre: {}
Apellido: {}
Correo: {}
Contraseña: {}

'''.format(self.nombre,self.apellido,self.correo,self.contraseña))
		archivo.close()
def mostrararchivo():
	archivo = open('registro.txt','r')
	print(archivo.read())
def crearusuario():
	correo = input('Correo: ')
	contraseña = input('Contraseña: ')
	nombre = input('Nombre: ')
	apellido = input('Apellido: ')
	usuariocreado = USUARIO(nombre,apellido,correo,contraseña)
	usuariocreado.guardarenelarchivo()

def calculadora(opcion):
	ciclo = True
	while ciclo == True:
		try:
			num1 = int(input('Primer numero: '))
			num2 = int(input('Segundo numero: '))
			break
		except:
			print('Tiene que ingresar un numero')
			continue
	if opcion == '1':
		return num1+num2
	elif opcion == '2':
		return num1-num2
	elif opcion == '3':
		return num1*num2
	elif opcion == '4':
		return num1/num2
while True:
	print('OPCIONES')
	print('')
	print('1-Registrar')
	print('2-Ingresar')
	print('3-Salir')
	opcion = input('Opcion: ')
	if opcion == '1':
		crearusuario()
	elif opcion == '2':	
		archivo = open('registro.txt','a')
		archivo.close()
		archivo = open('registro.txt','r')
		lineas_archivo = archivo.readlines()
		archivo.close()
		correo = input('Ingrese su correo: ')
		if 'Correo: '+correo+'\n' in lineas_archivo:
			contraseña = input('Ingrese la contraseña: ')
			if 'Contraseña: '+contraseña+'\n' in lineas_archivo:
				print('')
				ciclo = True
				while ciclo == True:
					print('OPERACIONES ARITMETICAS')
					print('1-sumar')
					print('2-restar')
					print('3-multiplicar')
					print('4-dividir')
					entrada = input('Opcion: ')
					print('Resultado: ',calculadora(entrada))
					cerrar = input('Desea cerrar su cuenta? s/n: ')
					if cerrar == 's':
						break
					elif cerrar == 'n':
						continue		
			else:
				print('Contraseña incorrecta')
		elif correo == 'administrador':
			contraseña = input('Ingrese la contraseña: ')
			if contraseña == 'administrador':
				mostrararchivo()
				break
			else:
				print('Contraseña incorrecta')
		else:
			print('Correo invalido, ingrese un correo valido')
				
	elif opcion == '3':
		print('GRACIAS :)')
		break
