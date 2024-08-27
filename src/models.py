from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum
from datetime import datetime

# Enum classes for Rating and Status
class Rating(PyEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"

class Status(PyEnum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

# User Model (Simplified version of Django's User)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# Profile Model
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Enum(Rating), nullable=True)
    avatar = Column(String, default="")
    bio = Column(Text, nullable=True)

    user = relationship("User", back_populates="profile")

User.profile = relationship("Profile", uselist=False, back_populates="user")

# Booking Model
class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    make_up = Column(Boolean, default=False)
    wig = Column(Boolean, default=False)
    clothes = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(Enum(Status), default=Status.PENDING)
    designer_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    customer_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    location = Column(String(180))
    comment = Column(String(180), nullable=True)
    price = Column(Float, default=0.0)

    designer = relationship("User", foreign_keys=[designer_id], backref="designer_bookings")
    customer = relationship("User", foreign_keys=[customer_id], backref="customer_bookings")

# Cart Model
class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, index=True)
    sessions_id = Column(Integer, ForeignKey('bookings.id'))
    customer_id = Column(Integer, ForeignKey('users.id'))

    sessions = relationship("Booking", backref="carts")
    customer = relationship("User", backref="cart")

# Offer Model
class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True, index=True)
    wig_price = Column(Float, default=0.0)
    clothes_price = Column(Float, default=0.0)
    make_up_price = Column(Float, default=0.0)
    designer_id = Column(Integer, ForeignKey('users.id'))
    comments = Column(String(180), nullable=True)

    designer = relationship("User", backref="offers")

# Notification Model
class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(180), nullable=True)
    read = Column(Boolean, default=False)

    user = relationship("User", backref="notifications")
