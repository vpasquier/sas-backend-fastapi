from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models
import schemas

router = APIRouter()

# User CRUD operations
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = user.password  # Hash the password in a real application
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user

# Profile CRUD operations
@router.post("/profiles/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileBase, db: Session = Depends(get_db)):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.get("/profiles/", response_model=List[schemas.Profile])
def read_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    profiles = db.query(models.Profile).offset(skip).limit(limit).all()
    return profiles

@router.get("/profiles/{profile_id}", response_model=schemas.Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.delete("/profiles/{profile_id}", response_model=schemas.Profile)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(profile)
    db.commit()
    return profile

# Booking CRUD operations
@router.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/bookings/", response_model=List[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bookings = db.query(models.Booking).offset(skip).limit(limit).all()
    return bookings

@router.get("/bookings/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/bookings/{booking_id}", response_model=schemas.Booking)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return booking

# Cart CRUD operations
@router.post("/carts/", response_model=schemas.Cart)
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

@router.get("/carts/", response_model=List[schemas.Cart])
def read_carts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    carts = db.query(models.Cart).offset(skip).limit(limit).all()
    return carts

@router.get("/carts/{cart_id}", response_model=schemas.Cart)
def read_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.delete("/carts/{cart_id}", response_model=schemas.Cart)
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    db.delete(cart)
    db.commit()
    return cart

# Offer CRUD operations
@router.post("/offers/", response_model=schemas.Offer)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = models.Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@router.get("/offers/", response_model=List[schemas.Offer])
def read_offers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).offset(skip).limit(limit).all()
    return offers

@router.get("/offers/{offer_id}", response_model=schemas.Offer)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

@router.delete("/offers/{offer_id}", response_model=schemas.Offer)
def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    db.delete(offer)
    db.commit()
    return offer

# Notification CRUD operations
@router.post("/notifications/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = models.Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/notifications/", response_model=List[schemas.Notification])
def read_notifications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notifications = db.query(models.Notification).offset(skip).limit(limit).all()
    return notifications

@router.get("/notifications/{notification_id}", response_model=schemas.Notification)
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.delete("/notifications/{notification_id}", response_model=schemas.Notification)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification)
    db.commit()
    return notification
