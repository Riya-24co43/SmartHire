# Processed Job Dataset

The `cleaned_jobs.csv` file is not included in this repository because of its large file size (approximately 80 MB).

The SmartHire application requires this file to run.

Place the file in this folder:

```text
data/processed/cleaned_jobs.csv
```

The file is generated from the raw job listing dataset during the data preparation stage.

To reproduce the processed dataset:

1. Place the raw job listing dataset in the appropriate `data/raw/` folder.
2. Open `notebooks/01_data_preparation.ipynb`.
3. Run the notebook.
4. The cleaned dataset will be saved as:

```text
data/processed/cleaned_jobs.csv
```
