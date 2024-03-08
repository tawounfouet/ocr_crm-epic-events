import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base  # Import relatif

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()


# Utiliser les variables d'environnement pour se connecter à la base de données
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


db_url = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


engine = create_engine(db_url)

# connexion à la base de données
try:
    connexion = engine.connect()
    print(f"Connexion à la base de données '{DB_NAME}' réussie !")

    # Créer les tables dans la base de données
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=connexion)
    print('Les tables ont été créées avec succès !')

    Session = sessionmaker(bind=engine)
    session = Session()
    
    
    # Ajouter des données dans la base de données
    
    # close the session
    session.close()


except Exception as e:
    print('Erreur de connexion à la base de données', e)




