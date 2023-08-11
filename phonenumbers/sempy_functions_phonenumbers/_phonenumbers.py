from sempy.functions import semantic_function, semantic_parameters
from sempy.fabric import FabricDataFrame, FabricSeries
from sempy.fabric.matcher import CountryMatcher


@semantic_function("is_phonenumber", pip_packages=["phonenumbers"], series_type=str)
def is_phonenumber_series(series: FabricSeries) -> FabricSeries:
    """
    Determine if a phone number is valid or not using the `phonenumbers <https://github.com/daviddrysdale/python-phonenumbers>`_ package.

    Parameters
    ----------
    series : FabricSeries
        The series this function is applied on.

    Returns
    -------
    FabricSeries
        A boolean series indicating if the phone number is valid or not.
    """
    import phonenumbers

    def is_phonenumber(v: str) -> bool:
        try:
            pn = phonenumbers.parse(v, None)
            return bool(phonenumbers.is_valid_number(pn))
        except Exception:
            return False

    return series.apply(is_phonenumber).rename(f"is_phonenumber({series.name})")


@semantic_function("is_phonenumber", pip_packages=["phonenumbers"])
@semantic_parameters(col_num=str,
                     col_country=CountryMatcher)
def is_phonenumber_dataframe(df: FabricDataFrame,
                             col_num: str,
                             col_country: str
                             ) -> FabricSeries:
    """
    Determine if a phone number is valid or not taking the supplied country into account using the `phonenumbers <https://github.com/daviddrysdale/python-phonenumbers>`_ package.

    Parameters
    ----------
    df : FabricDataFrame
        The dataframe this function is applied on.
    col_num : str
        Name of the phone number column.
    col_country : str
        Name of the country column.

    Returns
    -------
    FabricSeries
        A boolean series indicating if the phone number is valid or not.
    """
    import phonenumbers

    def is_valid(row):
        try:
            pn = phonenumbers.parse(row[0], row[1])
            return bool(phonenumbers.is_valid_number(pn))
        except Exception:
            return False

    return df[[col_num, col_country]].apply(is_valid, axis=1)


@semantic_function("parse_phonenumber", pip_packages=["phonenumbers"])
@semantic_parameters(col_num=str,
                     col_country=CountryMatcher)
def parse_phonenumbers(df: FabricDataFrame,
                       col_num: str,
                       col_country: str
                       ) -> FabricDataFrame:
    """
    Parse a phone number into country code and national number using the `phonenumbers <https://github.com/daviddrysdale/python-phonenumbers>`_ package.

    Note: this function automatically shows up in :class:`sempy.fabric.FabricDataFrame` (e.g. df.parse_phonenumbers(...)) if the column requirements are met.

    Parameters
    ----------
    df : FabricDataFrame
        The dataframe this function is applied on.
    col_num : str
        Name of the phone number column.
    col_country : str
        Name of the country column.

    Returns
    -------
    FabricDataFrame
        The resulting FabricDataFrame containing a country_code and national_number column.
    """
    import phonenumbers

    def parse(row):
        pn = phonenumbers.parse(row[0], row[1])
        return {"country_code": pn.country_code, "national_number": pn.national_number}

    return df[[col_num, col_country]].apply(parse, axis=1, result_type='expand')\
        .set_index(df.index)
