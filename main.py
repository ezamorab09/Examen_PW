from flask import Flask
from flask import render_template, request



app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


def calculo_de_compras(nombre, edad, cantidad_de_tarros):

    precio_tarro = 9000

    total_compra = cantidad_de_tarros * precio_tarro
    descuento = 0
    error_nombre = ""
    error_edad = ""
    error_cantidad_de_tarros = ""

    if not nombre.isalpha():
        error_nombre = "Error. El nombre debe contener solo letras"
    if edad < 0:
        error_edad = "Error. La edad debe ser un numero entero"
    if cantidad_de_tarros < 0:
        error_cantidad_de_tarros = "Error. La cantidad de tarros debe ser un numero entero"

    if not error_nombre and not error_edad and not error_cantidad_de_tarros:
        if 18 <= edad <= 30:
            descuento = total_compra * 0.15
        elif edad > 30:
            descuento = total_compra * 0.25

    total_a_pagar = total_compra - descuento
    return total_compra, descuento, total_a_pagar, error_nombre, error_edad, error_cantidad_de_tarros


@app.route('/Ejercicio1', methods=['GET', 'POST'])
def calculo_compra_web():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_de_tarros = int(request.form['cantidad_de_tarros'])
        total_compra, descuento, total_a_pagar, error_nombre, error_edad, error_cantidad_de_tarros = calculo_de_compras(nombre, edad, cantidad_de_tarros)
        return render_template('Ejercicio1.html', nombre=nombre, total_compra=total_compra, descuento=descuento,
                               total_a_pagar=total_a_pagar, error_nombre=error_nombre, error_edad=error_edad,
                               error_cantidad_de_tarros=error_cantidad_de_tarros)

    return render_template('Ejercicio1.html')

usuarios = {'juan': 'admin', 'pepe': 'user'}
@app.route('/Ejercicio2', methods=['GET', 'POST'])
def inicio_sesion():
    mensaje = ''

    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre in usuarios and usuarios[nombre] == contraseña:
            mensaje = f'Bienvenido {"administrador"  if contraseña == "admin" else "usuario"} {nombre}'
        else:
            mensaje = 'Usuario o contraseña incorrecta'

        return render_template('Ejercicio2.html', mensaje=mensaje)
    return render_template('Ejercicio2.html')

if __name__ == '__main__':

    app.run(debug=True)