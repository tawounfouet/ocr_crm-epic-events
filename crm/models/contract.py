# crm/models/contract.py
from sqlalchemy import Column, Integer, Numeric, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from .base import Base, TimestampMixin


class Contract(Base, TimestampMixin):
    """Modèle contrat pour les contrats clients d'Epic Events"""

    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    sales_contact_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    amount_due = Column(Numeric(10, 2), nullable=False)
    signed_status = Column(Boolean, default=False, nullable=False)

    # Contrainte pour s'assurer que le montant dû ne dépasse pas le montant total
    __table_args__ = (
        CheckConstraint(
            "amount_due <= total_amount", name="check_amount_due_lte_total"
        ),
        CheckConstraint("total_amount >= 0", name="check_total_amount_positive"),
        CheckConstraint("amount_due >= 0", name="check_amount_due_positive"),
    )

    # Relations
    client = relationship("Client", back_populates="contracts")
    sales_contact = relationship("User", back_populates="contracts")
    events = relationship(
        "Event", back_populates="contract", cascade="all, delete-orphan"
    )

    def __repr__(self):
        status = "Signé" if self.signed_status else "Non signé"
        return f"<Contract #{self.id} - {status} - {self.total_amount}€>"

    @property
    def is_paid(self):
        """Vérifie si le contrat est entièrement payé"""
        return self.amount_due == 0

    @property
    def payment_progress(self):
        """Retourne le pourcentage de paiement"""
        if self.total_amount == 0:
            return 100
        return round(
            ((self.total_amount - self.amount_due) / self.total_amount) * 100, 2
        )
