from setuptools import setup, find_packages

setup(name='semantic-link-functions-holidays',
      version="0.0.1",
      python_requires='>=3.8',
      description='Semantic Link Functions for Holidays',
      author='SemPy Authors',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=["holidays"],
      author_email='semanticdatascience@service.microsoft.com',
      )