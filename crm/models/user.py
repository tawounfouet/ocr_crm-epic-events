# crm/models/user.py
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Role(str, Enum):
    """Énumération des rôles utilisateurs"""

    SALES = "SALES"
    SUPPORT = "SUPPORT"
    MANAGEMENT = "MANAGEMENT"


class User(Base, TimestampMixin):
    """Modèle utilisateur pour les employés d'Epic Events"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(SQLEnum(Role), nullable=False)

    # Relations
    clients = relationship(
        "Client", back_populates="sales_contact", cascade="all, delete-orphan"
    )
    contracts = relationship("Contract", back_populates="sales_contact")
    events = relationship("Event", back_populates="support_contact")

    def __repr__(self):
        return f"<User {self.email} ({self.role.value})>"

    @property
    def full_name(self):
        """Retourne le nom complet de l'utilisateur"""
        return f"{self.first_name} {self.last_name}"
