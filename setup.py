from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="tap30-mlops",
    version="0.1.0",
    author="َAli Moharmzadeh",
    packages=find_packages(),
    install_requires=requirements,
)