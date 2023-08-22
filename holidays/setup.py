from setuptools import setup, find_packages

version = "0.0.13"  # don't change - this is updated by .pipelines/version-patch.py

setup(name='semantic-link-functions-holidays',
      version=version,
      python_requires='>=3.10',
      description='Semantic link functions for holidays package. Enables enrichment of FabricDataFrame with public holidays.',
      author='Microsoft',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=["holidays", f"semantic-link-sempy=={version}"],
      author_email='semanticdatascience@service.microsoft.com',
      classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.10']
      )
