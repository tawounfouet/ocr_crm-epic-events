from sqlalchemy import  ForeignKey, Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


# Définir une énumération pour les options de département
class RoleEnum(Enum):
    COMMERCIAL = 'commercial'
    SUPPORT = 'support'
    GESTION = 'gestion'


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    # role = Column(Enum(RoleEnum), nullable=False)


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    contact_employee = relationship('Employee', back_populates='clients')



class ContractStatusEnum(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    EXPIRED = 'expired'

class Contract(Base):
    __tablename__ = 'contracts'

    contract_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    contract_name = Column(String(255), nullable=False)
    employee = relationship('Employee', back_populates='contracts')
    invoice_amount = Column(Integer, nullable=False)
    balance_due = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    # contract_status = Column(Enum(ContractStatusEnum), nullable=False)
    


class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey('contracts.contract_id'))
    event_name = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    end_date = Column(DateTime, nullable=False)
    employee = relationship('Employee', back_populates='events')
    attendees = Column(Integer, nullable=False)
    