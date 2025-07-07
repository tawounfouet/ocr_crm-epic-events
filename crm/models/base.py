from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func

Base = declarative_base()


class TimestampMixin:
    """Mixin pour ajouter les timestamps created_at et updated_at"""

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
