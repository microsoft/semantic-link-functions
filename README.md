# Semantic Link Functions

[![Semantic Link Functions](https://github.com/microsoft/semantic-link-functions/actions/workflows/build.yaml/badge.svg)](https://github.com/microsoft/semantic-link-functions/actions/workflows/build.yaml)
[![PyPI version](https://badge.fury.io/py/semantic-link-functions-geopandas.svg)](https://badge.fury.io/py/semantic-link-functions-geopandas)
[![PyPI version](https://badge.fury.io/py/semantic-link-functions-holidays.svg)](https://badge.fury.io/py/semantic-link-functions-holidays)
[![PyPI version](https://badge.fury.io/py/semantic-link-functions-meteostat.svg)](https://badge.fury.io/py/semantic-link-functions-meteostat)
[![PyPI version](https://badge.fury.io/py/semantic-link-functions-phonenumbers.svg)](https://badge.fury.io/py/semantic-link-functions-phonenumbers)
[![PyPI version](https://badge.fury.io/py/semantic-link-functions-validators.svg)](https://badge.fury.io/py/semantic-link-functions-validators)

[FabricDataFrames](https://learn.microsoft.com/en-us/python/api/sempy/sempy.fabric.fabricdataframe) dynamically expose semantic functions based on logic defined by each function.
For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column.

Each semantic function uses information about the data types, metadata (such as Power BI data categories),
and the data in a FabricDataFrame or FabricSeries to determine its relevance to the particular data on which you're working.

Semantic functions are automatically discovered when annotated with the @semantic_function decorator. You can think of semantic functions as being similar to C# extension methods applied to the popular DataFrame concept.

## Usage

Usually a FabricDataFrame is retrieved using fabric.read_table(...) or fabric.evaluate_measure(...)

```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
    {"country": ["US", "AT"],
        "lat": [40.7128, 47.8095],
        "long": [-74.0060, 13.0550]},
    column_metadata={"lat": {"data_category": "Latitude"}, "long": {"data_category": "Longitude"}},
)

# Convert to GeoPandas dataframe
df_geo = df.to_geopandas(lat_col="lat", long_col="long")

# Use the explore function to visualize the data
df_geo.explore()
```

You can also create ad-hoc semantic functions

```python
from sempy.fabric import FabricDataFrame, FabricSeries
from sempy.fabric.matcher import CountryMatcher, CityMatcher
from sempy.functions import semantic_function, semantic_paramters

@semantic_function("is_capital")
@semantic_parameters(col_country=CountryMatcher, col_city=CityMatcher)
def _is_captial(df: FabricDataFrame, col_country: str, col_city: str) -> FabricSeries:
    """Returns true if the city is a capital of the country"""
    capitals = {
        "US": ["Washington"],
        "AT": ["Vienna"],
        # ...
    }

    return df[[col_country, col_city]] \
        .apply(lambda row: row[1] in capitals[row[0]], axis=1)
```

## Development

Create a conda environment with the following command:

```bash
conda env create -f environment.yml -n sempy-func
conda activate sempy-func
```

For each package (e.g. holidays), run

```bash
cd holidays
pip install -e .
pytest -s tests/
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
