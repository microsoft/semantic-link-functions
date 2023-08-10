from setuptools import setup, find_packages

version = ""  # don't change - this is updated by .pipelines/version-patch.py

setup(name='semantic-link-functions-holidays',
      version=version,
      python_requires='>=3.8',
      description='Semantic link functions for Holidays',
      author='Microsoft',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=["holidays"],
      author_email='semanticdatascience@service.microsoft.com',
      )
