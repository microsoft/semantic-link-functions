from setuptools import setup, find_packages

version = ""  # don't change - this is updated by .pipelines/version-patch.py

setup(name='semantic-link-functions-phonenumbers',
      version=version,
      python_requires='>=3.10',
      description='Semantic link functions for PhoneNumbers',
      author='Microsoft',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=["phonenumbers", "semantic-link-sempy"],
      author_email='semanticdatascience@service.microsoft.com',
      classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'License :: Other/Proprietary License', 'Programming Language :: Python :: 3.10']
      )
