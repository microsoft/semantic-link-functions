from setuptools import setup


# list all subpackages here
extras_packages = ["geopandas", "holidays", "phonenumbers", "validators"]

# create a dictionary of all subpackages and their dependencies
extras_require = {pkg: [f"semantic-link-functions-{pkg}"] for pkg in extras_packages}
extras_require["all"] = [item for group in extras_require.values() for item in group]

setup(name='semantic-link-functions',
      version="0.0.1",
      python_requires='>=3.8',
      description='Semantic Link Functions',
      author='SemPy Authors',
      url='https://github.com/microsoft/semantic-link-functions',
      packages=[],
      extras_require=extras_require,
      author_email='semanticdatascience@service.microsoft.com',
      )
