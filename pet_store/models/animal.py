# models/animal.py
# Modelo para la base de datos de los animales

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class Animal(db.Model):
    __tablename__ = 'animals'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def to_dict(self):
        """
        Convierte el objeto Animal a un diccionario.
        """
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

    @staticmethod
    def get_all(db_session):
        """
        Obtiene todos los animales del inventario.
        """
        return db_session.query(Animal).all()
    
    @staticmethod
    def find_by_name(db_session, name):
        """
        Encuentra un animal por su nombre.
        """
        return db_session.query(Animal).filter_by(name=name).first()
    
    def save(self, db_session):
        """
        Guarda el animal en la base de datos.
        """
        db_session.add(self)
        db_session.commit()
