import pandas as pd
import glob
import zipfile

# Find all 12 ZIP files
files = glob.glob("2024_flights/*.zip")

dfs = []

for file in files:
    with zipfile.ZipFile(file) as z:
        # Find the CSV file inside the ZIP
        csv_file = [name for name in z.namelist()
                    if name.lower().endswith(".csv")][0]

        # Read the CSV directly from the ZIP
        with z.open(csv_file) as f:
            df_month = pd.read_csv(f)
            dfs.append(df_month)

# Combine all 12 months
# Combine all 12 months
df = pd.concat(dfs, ignore_index=True)

# Save directly as a compressed Parquet file
df.to_parquet(
    "2024_flights/flights_2024_combined.parquet",
    compression="zstd",
    index=False
)