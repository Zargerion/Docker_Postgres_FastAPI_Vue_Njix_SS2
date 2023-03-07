from setuptools import setup 

setup(
    name='ss2',
    version='0.0.1',
    author='Oleg OSS Sabter Zarg',
    description='FastApiApp',
    install_requires=[
    'fastapi==0.70.0',
    'uvicorn==0.15.0',
    'SQLAlchemy==1.4.26',
    'pytest==6.2.5',
    'requests==2.26.0',
    ],
    scripts=['app/main.py']
)