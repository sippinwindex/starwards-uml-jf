from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """
    User model for blog users who can login and save favorites
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    favorite_characters = db.relationship('FavoriteCharacter', backref='user', lazy=True, cascade='all, delete-orphan')
    favorite_planets = db.relationship('FavoritePlanet', backref='user', lazy=True, cascade='all, delete-orphan')
    favorite_vehicles = db.relationship('FavoriteVehicle', backref='user', lazy=True, cascade='all, delete-orphan')
    blog_posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class Character(db.Model):
    """
    StarWars Character model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    hair_color = db.Column(db.String(20))
    height = db.Column(db.String(20))
    mass = db.Column(db.String(20))
    skin_color = db.Column(db.String(50))
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    favorited_by = db.relationship('FavoriteCharacter', backref='character', lazy=True)
    
    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld_id": self.homeworld_id,
            "homeworld": self.homeworld.serialize() if self.homeworld else None,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class Planet(db.Model):
    """
    StarWars Planet model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    diameter = db.Column(db.String(20))
    rotation_period = db.Column(db.String(20))
    orbital_period = db.Column(db.String(20))
    gravity = db.Column(db.String(50))
    population = db.Column(db.String(50))
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(20))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    residents = db.relationship('Character', backref='homeworld', lazy=True)
    favorited_by = db.relationship('FavoritePlanet', backref='planet', lazy=True)
    
    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class Vehicle(db.Model):
    """
    StarWars Vehicle/Starship model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100))
    vehicle_class = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.String(50))
    length = db.Column(db.String(50))
    crew = db.Column(db.String(50))
    passengers = db.Column(db.String(50))
    max_atmosphering_speed = db.Column(db.String(50))
    cargo_capacity = db.Column(db.String(50))
    consumables = db.Column(db.String(50))
    vehicle_type = db.Column(db.String(20), default='vehicle')  # 'vehicle' or 'starship'
    hyperdrive_rating = db.Column(db.String(20))  # Only for starships
    MGLT = db.Column(db.String(20))  # Only for starships
    starship_class = db.Column(db.String(50))  # Only for starships
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    favorited_by = db.relationship('FavoriteVehicle', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return f'<Vehicle {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_type": self.vehicle_type,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class FavoriteCharacter(db.Model):
    """
    Junction table for User-Character many-to-many relationship
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Unique constraint to prevent duplicate favorites
    __table_args__ = (db.UniqueConstraint('user_id', 'character_id', name='unique_user_character'),)
    
    def __repr__(self):
        return f'<FavoriteCharacter user_id={self.user_id} character_id={self.character_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "character": self.character.serialize() if self.character else None,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class FavoritePlanet(db.Model):
    """
    Junction table for User-Planet many-to-many relationship
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Unique constraint to prevent duplicate favorites
    __table_args__ = (db.UniqueConstraint('user_id', 'planet_id', name='unique_user_planet'),)
    
    def __repr__(self):
        return f'<FavoritePlanet user_id={self.user_id} planet_id={self.planet_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "planet": self.planet.serialize() if self.planet else None,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class FavoriteVehicle(db.Model):
    """
    Junction table for User-Vehicle many-to-many relationship
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Unique constraint to prevent duplicate favorites
    __table_args__ = (db.UniqueConstraint('user_id', 'vehicle_id', name='unique_user_vehicle'),)
    
    def __repr__(self):
        return f'<FavoriteVehicle user_id={self.user_id} vehicle_id={self.vehicle_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "vehicle": self.vehicle.serialize() if self.vehicle else None,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class BlogPost(db.Model):
    """
    Blog posts about StarWars content
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(250), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_published = db.Column(db.Boolean, default=False, nullable=False)
    published_at = db.Column(db.DateTime)
    featured_image_url = db.Column(db.String(255))
    excerpt = db.Column(db.Text)
    tags = db.Column(db.String(500))  # Comma-separated tags
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<BlogPost {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "slug": self.slug,
            "author_id": self.author_id,
            "author": {
                "username": self.author.username,
                "first_name": self.author.first_name,
                "last_name": self.author.last_name
            } if self.author else None,
            "is_published": self.is_published,
            "published_at": self.published_at.isoformat() if self.published_at else None,
            "featured_image_url": self.featured_image_url,
            "excerpt": self.excerpt,
            "tags": self.tags.split(',') if self.tags else [],
            "view_count": self.view_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }