# crm/models/event.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    CheckConstraint,
)
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Event(Base, TimestampMixin):
    """Modèle événement pour les événements organisés par Epic Events"""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    client_contact = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    support_contact_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    location = Column(String(200), nullable=False)
    attendees = Column(Integer, nullable=False)
    notes = Column(Text, nullable=True)

    # Contraintes pour s'assurer que la date de fin est postérieure à la date de début
    __table_args__ = (
        CheckConstraint("end_date > start_date", name="check_end_date_after_start"),
        CheckConstraint("attendees > 0", name="check_attendees_positive"),
    )

    # Relations
    contract = relationship("Contract", back_populates="events")
    client = relationship("Client", back_populates="events")
    support_contact = relationship("User", back_populates="events")

    def __repr__(self):
        return f"<Event {self.name} - {self.start_date.strftime('%Y-%m-%d')}>"

    @property
    def duration_days(self):
        """Retourne la durée de l'événement en jours"""
        return (self.end_date - self.start_date).days + 1

    @property
    def has_support_assigned(self):
        """Vérifie si un support est assigné à l'événement"""
        return self.support_contact_id is not None
