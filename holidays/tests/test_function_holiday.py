from sempy.fabric import FabricDataFrame
import pandas as pd


def test_function_holiday():
    df = FabricDataFrame(
        {"country": ["US", "AT"], "date": ["2023-01-06", "2023-01-06"]},
        column_metadata={"country": {"data_category": "Country"}},
    )

    df["date"] = pd.to_datetime(df["date"])

    holiday_series = df.is_holiday(date_col="date", country_col="country")
    assert holiday_series.tolist() == [False, True]

    assert "is_holiday(date_col='date', country_col='country')" in dir(df)


def test_function_holiday_with_province():
    df = FabricDataFrame(
        {
            "country": ["US", "AT", "US", "US"],
            "state": ["CA", None, "PR", "PR"],
            "date": ["2023-01-06", "2023-01-06", "2018-01-06 12:00", "2018-01-06 13:00"],
        },
        column_metadata={
            "country": {"data_category": "Country"},
            "state": {"data_category": "StateOrProvince"},
        },
    )

    df["date"] = pd.to_datetime(df["date"])

    holiday_series = df.is_holiday(
        date_col="date", country_col="country", state_or_province_col="state"
    )
    assert holiday_series.tolist() == [False, True, True, True]

    assert "is_holiday(date_col='date', country_col='country', state_or_province_col='state')" in dir(df)


def test_function_holiday_multiple():
    df = FabricDataFrame(
        {"country": ["US", "AT"], "date": ["2023-01-06", "2023-01-06"]},
        column_metadata={"country": {"data_category": "Country"}},
    )

    df["date"] = pd.to_datetime(df["date"])
    df["date2"] = df["date"]
    df["date3"] = df["date"]

    holiday_series = df.is_holiday(date_col="date", country_col="country")
    assert holiday_series.tolist() == [False, True]

    assert "is_holiday(date_col='date', country_col='country')" in dir(df)
    assert "is_holiday(date_col='date2', country_col='country')" in dir(df)
    assert "is_holiday(date_col='date3', country_col='country')" in dir(df)
