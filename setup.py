
  
#from pip.req import parse_requirements
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup


setup(
    name='xsdtojson',
    version='0.1',
    description='Convert XSD to JSON Schema',
    author='Ben Scott',
    author_email='ben@benscott.co.uk',
    packages=['xsdtojson'],
    entry_points={
        'console_scripts': ['xsdtojson=xsdtojson.cli:main'],
    }
)
