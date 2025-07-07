# crm/models/client.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Client(Base, TimestampMixin):
    """Modèle client pour les clients d'Epic Events"""

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    company_name = Column(String(100), nullable=False)
    sales_contact_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relations
    sales_contact = relationship("User", back_populates="clients")
    contracts = relationship(
        "Contract", back_populates="client", cascade="all, delete-orphan"
    )
    events = relationship(
        "Event", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Client {self.full_name} ({self.company_name})>"
