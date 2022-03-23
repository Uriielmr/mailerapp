import os  #configuracion de la API para el servicio de correos

from flask import Flask

def create_app():          #esta funcion siempre se ejcuta en un comienzo cuando este construida en flask
    app = Flask(__name__)

    app.config.from_mapping(  #aqui se insertarn variables de entorno y se cambiaran cuando se suba a produccion
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),          #ESTE ES EL SERVICIO DE CORREOS QUE SE VA A UTILIZAR ES GRATUITO
        SECRET_KEY=os.environ.get('SECRET_KEY'),      #ESTE ES EL
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db
    
    db.init_app(app)

    from . import mail

    app.register_blueprint(mail.bp)

    return app

