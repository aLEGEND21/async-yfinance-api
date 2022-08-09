from setuptools import setup
from setuptools import find_packages

# Requirements
requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="async-yfinance-wrapper",
    version="0.1.0",
    description="A Python module to fetch financial data from Yahoo Finance.",
    author="aLEGEND21",
    packages=find_packages(),
    install_requires=requirements,
)