from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum classes for Rating and Status
class Rating(str, Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"

class Status(str, Enum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

# User Schema
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Profile Schema
class ProfileBase(BaseModel):
    rating: Optional[Rating] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Booking Schema
class BookingBase(BaseModel):
    make_up: Optional[bool] = False
    wig: Optional[bool] = False
    clothes: Optional[bool] = False
    status: Status
    location: str
    comment: Optional[str] = None
    price: float = 0.0

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    created: datetime
    updated: datetime
    designer_id: Optional[int] = None
    customer_id: Optional[int] = None

    class Config:
        orm_mode = True

# Cart Schema
class CartBase(BaseModel):
    sessions_id: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True

# Offer Schema
class OfferBase(BaseModel):
    wig_price: float = 0.0
    clothes_price: float = 0.0
    make_up_price: float = 0.0
    comments: Optional[str] = None

class OfferCreate(OfferBase):
    pass

class Offer(OfferBase):
    id: int
    designer_id: int

    class Config:
        orm_mode = True

# Notification Schema
class NotificationBase(BaseModel):
    message: Optional[str] = None
    read: bool = False

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
