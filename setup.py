from setuptools import setup, find_packages

setup(
    name="dmutils",
    version="0.1.0",
    description="Utils para el airflow de datamanagment",
    packages=find_packages(),
    author="Data Managment",
    author_email="DataManagementMKTn@teco.com.ar",
    install_requires=[
        'apache-airflow==1.10.10',
    ],
)