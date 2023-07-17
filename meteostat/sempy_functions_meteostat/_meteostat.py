from sempy.functions import semantic_function, semantic_parameters
from sempy.fabric import (
    FabricDataFrame,
)
from sempy.fabric.matcher import (
    LatitudeMatcher,
    LongitudeMatcher,
)
import datetime
import pandas as pd


@semantic_function("add_weather_meteostat", pip_packages=["meteostat"])
@semantic_parameters(lat_col=LatitudeMatcher,
                     long_col=LongitudeMatcher,
                     date_col=datetime.datetime)
def add_weather_meteostat(df: FabricDataFrame,
                          lat_col: str,
                          long_col: str,
                          date_col: str,
                          freq: str = "daily") -> FabricDataFrame:
    """
    For each date, latitude and longitude fetch the historical weather using the Meteostat library.

    Note: this function automatically shows up in :class:`sempy.fabric.FabricDataFrame` (e.g. df.add_weather_meteostat(...)) if the column requirements are met.

    Parameters
    ----------
    df : FabricDataFrame
        The dataframe this function is applied on.
    date_col : str
        Name of the date column.
    lat_col : str
        Name of the latitude column.
    long_col : str
        Name of the longitude column.

    Returns
    -------
    FabricDataFrame
        The provided Fabric DataFrame with additional weather columns (tavg, tmax, prcp, wdir, wspd, wpget, pres, tsun).
    """
    from meteostat import Daily, Hourly, Monthly, Point

    freq_dict = {"daily": Daily, "hourly": Hourly, "monthly": Monthly}

    if freq not in freq_dict.keys():
        raise ValueError(f"freq must be one of {','.join(freq_dict.keys())} ")

    freq_ctor = freq_dict[freq]

    def per_location(g):
        # find consecutive data ranges
        g_consecutive = pd.DataFrame({
            'date': g[date_col],
            'grp': g[date_col].diff().dt.days.ne(1).cumsum()
        })

        groups = []

        (lat, long) = g.name

        for _, row in g_consecutive.groupby("grp").agg(['first', 'last']).iterrows():
            weather_df = freq_ctor(Point(lat, long), start=row['date']['first'], end=row['date']['last']).fetch()

            weather_df.reset_index(inplace=True)
            weather_df.rename({"time": date_col}, axis=1, inplace=True)

            weather_df[lat_col] = lat
            weather_df[long_col] = long

            groups.append(weather_df)

        return pd.concat(groups, ignore_index=True)

    weather_df = df.groupby([lat_col, long_col], group_keys=False).apply(per_location)

    return df.merge(weather_df, how="left", on=[lat_col, long_col, date_col])
