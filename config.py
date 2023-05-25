import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1011@localhost/biblioteca' #cambiar contraseña
    SQLALCHEMY_TRACK_MODIFICATIONS = False


''' CREATE TABLE libro (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    autor VARCHAR(200) NOT NULL,
    anio_publicacion INTEGER NOT NULL,
    paginas INTEGER NOT NULL,
    foto VARCHAR(2000)
);   '''
