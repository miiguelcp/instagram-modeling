import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

##class Person(Base):
  ##  __tablename__ = 'person'
  ##  # Here we define columns for the table person
  ##  # Notice that each column is also a normal Python instance attribute.
  ##  id = Column(Integer, primary_key=True)
  ##  name = Column(String(250), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(210), unique=True)
    user_name = Column(String(80), unique=True)
    favoritos = relationship('favorito', backref='usuario', uselist=True)
    favorito_id = Column(Integer, ForeignKey('favorito.id'), nullable=False)


class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)

class Vehicle(Base):
    __tablename__= 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    color = Column(String(40), nullable=False)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    terrain = Column(Integer)
    diameter = Column(Integer)
    poblation = Column(Integer)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    dob = Column(DateTime())
    gender = Column(String(20), nullable=False)
    eye_color = Column(String(20), nullable=False)


##class Address(Base):
##    __tablename__ = 'address'
##    # Here we define columns for the table address.
##    # Notice that each column is also a normal Python instance attribute.
##    id = Column(Integer, primary_key=True)
##    street_name = Column(String(250))
##    street_number = Column(String(250))
##    post_code = Column(String(250), nullable=False)
##    person_id = Column(Integer, ForeignKey('person.id'))
##    person = relationship(Person)
##
##    def to_dict(self):
##        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')