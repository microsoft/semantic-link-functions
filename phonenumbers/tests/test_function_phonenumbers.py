from sempy.fabric import FabricDataFrame
import pandas as pd


def test_function_phonenumbers():
    df = FabricDataFrame(
        {"num": ["+442083661177", "12345"]}
    )

    # print([m for m in dir(df["num"]) if "phone" in m])

    is_phone_series = df["num"].is_phonenumber()
    assert is_phone_series.tolist() == [True, False]

    assert "is_phonenumber()" in dir(df["num"])


def test_function_phonenumbers_country():
    df = FabricDataFrame(
        {"num": ["+442083661177", "ABC000-0000", "abc"], "country": ["US", "AT", "Unknown"]},
        column_metadata={"country": {"data_category": "Country"}},
    )

    is_phone_series = df.is_phonenumber(col_num="num", col_country="country")

    assert is_phone_series.tolist() == [True, False, False]


def test_function_phonenumbers_country_parse():
    df = FabricDataFrame(
        {"num": ["+442083661177", "ABC000-0000"], "country": ["US", "AT"]},
        column_metadata={"country": {"data_category": "Country"}},
    )

    df = df.set_index(pd.Index(["A", "B"]))

    df_phone = df.parse_phonenumber(col_num="num", col_country="country")

    assert df_phone.index.tolist() == ["A", "B"]
    assert df_phone["country_code"].tolist() == [44, 43]
    assert df_phone["national_number"].tolist() == [2083661177, 0]
