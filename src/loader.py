"""
Loads project config and vector shape.
"""

import yaml
import geopandas as gpd


def load_config(path: str) -> dict:
    """
    Load YAML config file.

    Args:
        path (str): Path to config.yaml

    Returns:
        dict: Parsed configuration
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_shape(path: str) -> gpd.GeoDataFrame:
    """
    Load a vector file (GeoPackage, GeoJSON, etc.).

    Args:
        path (str): File path

    Returns:
        GeoDataFrame: Loaded geometry
    """
    return gpd.read_file(path).to_crs("EPSG:4326")