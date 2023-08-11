from sempy.fabric import FabricDataFrame
import geopandas


def test_function_geopandas():
    df = FabricDataFrame(
        {"country": ["US", "AT"],
         "lat": [40.7128, 47.8095],
         "long": [-74.0060, 13.0550]},
        column_metadata={"lat": {"data_category": "Latitude"}, "long": {"data_category": "Longitude"}},
    )

    df_geo = df.to_geopandas(lat_col="lat", long_col="long")

    # load NYC boros
    import geodatasets
    nybb_path = geodatasets.get_path('nybb')
    boros = geopandas.read_file(nybb_path)

    df_join = boros.sjoin(df_geo.to_crs(boros.crs))

    assert df_join["BoroName"].tolist() == ["Manhattan"]

    # useful for debugging
    # print([x for x in dir(df) if "to_geopandas" in x])

    # # check if it shows in intellisense
    assert "to_geopandas(lat_col='lat', long_col='long')" in dir(df)
