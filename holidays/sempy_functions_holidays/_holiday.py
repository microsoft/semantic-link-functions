from sempy.functions import semantic_function, semantic_parameters
from sempy.fabric import (
    FabricDataFrame,
    FabricSeries,
)
from sempy.fabric.matcher import (
    CountryMatcher,
    StateOrProvinceMatcher
)
from typing import Optional
import datetime


@semantic_function("is_holiday", pip_packages=["holidays"])
@semantic_parameters(date_col=datetime.datetime,
                     country_col=CountryMatcher,
                     state_or_province_col=Optional[StateOrProvinceMatcher])
def is_holiday(df: FabricDataFrame,
               date_col: str,
               country_col: str,
               state_or_province_col: Optional[str] = None
               ) -> FabricSeries:
    """
    For each date, country and optional state/province determines if it is a public holiday using the `holidays <https://python-holidays.readthedocs.io/en/latest>`_ package.

    Note: this function automatically shows up in :class:`sempy.fabric.FabricDataFrame` (e.g. df.is_holiday(...)) if the column requirements are met.

    Parameters
    ----------
    df : FabricDataFrame
        The dataframe this function is applied on.
    date_col : str
        Name of the date column.
    country_col : str
        Name of the country column.
    state_or_province_col : str, default=None
        Name of the state/province column, by default to None.

    Returns
    -------
    FabricSeries
        A boolean series indicating if the date is a public holiday.
    """
    import holidays

    cols = [date_col, country_col]
    if state_or_province_col is not None:
        cols.append(state_or_province_col)

    df_holiday = df[cols].copy()

    # keep date portion only
    df_holiday[date_col] = df_holiday[date_col].dt.floor('d')
    df_holiday_unique = df_holiday.drop_duplicates().copy()

    # compute for unique combinations
    if state_or_province_col is not None:
        df_holiday_unique["__is_holiday"] = df_holiday_unique.apply(lambda row: row[0] in holidays.country_holidays(row[1], row[2]), axis=1)
    else:
        df_holiday_unique["__is_holiday"] = df_holiday_unique.apply(lambda row: row[0] in holidays.country_holidays(row[1]), axis=1)

    # project back to original dataframe
    return df_holiday.merge(df_holiday_unique).set_index(df.index)["__is_holiday"]
