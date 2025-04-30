from src import load_config, load_shape
from src import compute_stats_from_s3

config = load_config("config/config.yaml")
gdf = load_shape(config["paths"]["shape"])

df = compute_stats_from_s3(
    s3_path=config["s3"]["raster_key"],
    gdf=gdf,
    var_to_index=config["variables"]["var_to_index"],
    vars_to_check=config["variables"]["vars_to_check"],
    rounding=config["variables"].get("rounding", {})
)

df.to_csv("output/stats.csv")
print("Saved stats to output/stats.csv")