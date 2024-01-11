import pytest
import pandas as pd
from sempy.fabric import FabricDataFrame


@pytest.mark.filterwarnings("ignore: In a future version,")
def test_meteostat():
    df = FabricDataFrame({
         "lat": [40.7128, 47.8095, 47.8095, 47.8095],
         "long": [-74.0060, 13.0550, 13.0550, 13.0550],
         "date": ["2023-01-06", "2023-01-06", "2023-01-07", "2023-01-10"]
        },
        column_metadata={"lat": {"data_category": "Latitude"}, "long": {"data_category": "Longitude"}},
    )

    df["date"] = pd.to_datetime(df["date"])

    df_weather = df.add_weather_meteostat("lat", "long", "date")

    # replace nan with -1
    df_weather = df_weather.fillna(-1)

    assert df_weather.shape == (4, 13)
    assert df_weather.iloc[0].values.tolist() == \
        [40.7128, -74.006, pd.Timestamp('2023-01-06 00:00:00'), 5.9, 3.1, 7.9, 9.8, 0.0, 303.0, 9.2, -1, 1016.6, -1]
