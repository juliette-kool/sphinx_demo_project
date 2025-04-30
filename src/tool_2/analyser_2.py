"""
Clips a raster to a shape and computes basic stats for selected bands.
"""

import rioxarray
import pandas as pd


def compute_stats_from_s3(
    s3_path: str,
    gdf,
    var_to_index: dict,
    vars_to_check: list,
    rounding: dict = None
) -> pd.DataFrame:
    """
    Compute stats for specific bands in an S3-hosted raster clipped to a shape.

    Args:
        s3_path (str): S3 URI to the GeoTIFF
        gdf (GeoDataFrame): Shape to clip to
        var_to_index (dict): Variable name → band index (0-based)
        vars_to_check (list): Variables to extract
        rounding (dict): Optional rounding per variable

    Returns:
        DataFrame: Mean, median, min, max for each variable
    """
    rounding = rounding or {}
    stats_dict = {}

    da = rioxarray.open_rasterio(s3_path, chunks={"x": 512, "y": 512})
    da = da.rio.write_crs("EPSG:4326")

    clipped = da.rio.clip(gdf.geometry.values, gdf.crs, drop=True)

    for var in vars_to_check:
        if var not in var_to_index:
            print(f"Skipping unknown variable: {var}")
            continue

        band_data = clipped[var_to_index[var]]
        arr = band_data.compute()
        valid = arr.where(arr != arr.rio.nodata)

        stats = {
            "mean": float(valid.mean().values),
            "median": float(valid.median().values),
            "min": float(valid.min().values),
            "max": float(valid.max().values)
        }

        r = rounding.get(var, 2)
        stats_dict[var] = {k: round(v, r) for k, v in stats.items()}

    return pd.DataFrame(stats_dict).T[["mean", "median", "min", "max"]]