from sempy.functions import semantic_function, semantic_parameters
from sempy.fabric import FabricDataFrame
from sempy.fabric.matcher import (
    LatitudeMatcher,
    LongitudeMatcher
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import geopandas


@semantic_function("to_geopandas", pip_packages=["geopandas"])
@semantic_parameters(lat_col=LatitudeMatcher,
                     long_col=LongitudeMatcher)
def to_geopandas(df: FabricDataFrame,
                 lat_col: str,
                 long_col: str
                 ) -> "geopandas.GeoDataFrame":
    """
    Convert a :class:`~sempy.fabric.FabricDataFrame` to a :class:`~geopandas.GeoDataFrame` and automatically converting the lat_col and long_col into a geometry column.

    Note: this function automatically shows up in :class:`sempy.fabric.FabricDataFrame` (e.g. df.to_geopandas(...)) if the column requirements are met.

    Parameters
    ----------
    df : FabricDataFrame
        The dataframe this function is applied on.
    lat_col : str
        Name of the latitude column.
    long_col : str
        Name of the longitude column.

    Returns
    -------
    geopandas.GeoDataFrame
        The new :class:`~geopandas.GeoDataFrame`.
    """

    import geopandas

    return geopandas.GeoDataFrame(
        df,
        geometry=geopandas.points_from_xy(df[long_col], df[lat_col], crs="EPSG:4326"))
