from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
import psycopg2


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    anio_publicacion = db.Column(db.Integer, nullable=False)
    paginas = db.Column(db.Integer, nullable=False)
    foto = db.Column(db.String(100))

#cambiar datos
    def create_connection():
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="biblioteca",
            user="postgres",
            password="1011" #este
        )
        return connection

@app.route('/')
def listar_libros():
    libros = Libro.query.order_by(Libro.id.asc()).all()
    return render_template('listar_libros.html', libros=libros)


@app.route('/agregar_libro', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        anio_publicacion = request.form['anio_publicacion']
        paginas = request.form['paginas']
        foto = request.form['foto']

        libro = Libro(nombre=nombre, autor=autor, anio_publicacion=anio_publicacion, paginas=paginas, foto=foto)
        db.session.add(libro)

        db.session.commit()

        return redirect(url_for('listar_libros'))

    return render_template('agregar_libro.html')

@app.route('/editar_libro/<int:id>', methods=['GET', 'POST'])
def editar_libro(id):
    libro = Libro.query.get(id)

    if request.method == 'POST':
        libro.nombre = request.form['nombre']
        libro.autor = request.form['autor']
        libro.anio_publicacion = request.form['anio_publicacion']
        libro.paginas = request.form['paginas']
        libro.foto = request.form['foto']

        db.session.commit()

        return redirect(url_for('listar_libros'))

    return render_template('editar_libro.html', libro=libro)


@app.route('/eliminar_libro/<int:id>', methods=['GET', 'POST'])
def eliminar_libro(id):
    libro = Libro.query.get(id)
    return render_template('confirmar_eliminar_libro.html', libro=libro)

@app.route('/confirmar_eliminar_libro/<int:id>', methods=['POST', 'DELETE'])
def confirmar_eliminar_libro(id):
    print(id)
    libro = Libro.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('listar_libros'))


if __name__ == '__main__':
    app.run(debug=True)
