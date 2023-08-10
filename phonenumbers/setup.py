from setuptools import setup, find_packages

version = ""  # don't change - this is updated by .pipelines/version-patch.py

setup(name='semantic-link-functions-phonenumbers',
      version=version,
      python_requires='>=3.8',
      description='Semantic link functions for PhoneNumbers',
      author='Microsoft',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=["phonenumbers"],
      author_email='semanticdatascience@service.microsoft.com',
      )
