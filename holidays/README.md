FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column.

Each semantic function uses information about the data types, metadata (such as Power BI data categories), and the data in a FabricDataFrame or FabricSeries to determine its relevance to the particular data on which you're working.

Semantic functions are automatically discovered when annotated with the @semantic_function decorator. You can think of semantic functions as being similar to C# extension methods applied to the popular DataFrame concept.

```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
    {"country": ["US", "AT"], "date": ["2023-01-06", "2023-01-06"]},
    column_metadata={"country": {"data_category": "Country"}},
)

df["date"] = pd.to_datetime(df["date"])

holiday_series = df.is_holiday(date_col="date", country_col="country")
```
