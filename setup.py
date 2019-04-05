from setuptools import find_packages, setup

setup(
    name="brigade-tutorial-products",
    version="0.0.1",
    description="Store and serve products",
    packages=find_packages(exclude=["test", "test.*"]),
    install_requires=[
        "nameko==3.0.0-rc6",
        "nameko-sqlalchemy==1.5.0",
        "alembic==1.0.8",
        "psycopg2==2.8",
    ],
    extras_require={"dev": ["pytest==4.3.1", "coverage==4.5.3", "flake8==3.7.7"]},
    zip_safe=True,
)
