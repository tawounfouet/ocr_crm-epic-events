from setuptools import setup, find_packages

setup(
    name="epic-events-crm",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4.46",
        "typer[all]>=0.9.0",
        "click==8.1.7",
        "rich>=13.7.0",
        "pydantic>=1.10.13",
        "passlib[bcrypt]>=1.7.4",
        "pyjwt>=2.8.0",
        "python-dotenv>=1.0.0",
        "loguru>=0.7.2",
        "sentry-sdk>=1.38.0",
        "alembic>=1.13.1",
    ],
    entry_points={
        "console_scripts": [
            "epic-events=cli.main:app",
        ],
    },
    python_requires=">=3.9",
)
