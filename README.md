## Retrieval of Chandra Sensitivity Maps

This repository provides tools for retrieving and processing Chandra sensitivity maps. The code allows users to generate associations between Chandra Source Catalog (CSC) source names and their corresponding sensitivity maps, and to visualize these maps.

#### Usage

The main script, main.py, supports two primary commands: get_data and retrieve.

#### Command-line Arguments

```
usage: main.py [-h] {get_data,retrieve} ...

Process stack IDs for retrieving sensitivity maps.

positional arguments:
  {get_data,retrieve}  Available commands:
    get_data           Retrieve data based on separation and theta parameters.
    retrieve           Retrieve data using the specified stack IDs.

optional arguments:
  -h, --help           Show this help message and exit.

```

#### Example Usage

To generate data for the current sensitivity maps, use the following command:

```
python3 main.py get_data --separation 1.3 --theta_min 0 --theta_max 3
```


This command will create a `stack_ids.txt` file, which contains a list of all stack IDs, and an `associations_sep1.3_theta0.0-3.0.csv` file, which lists the associations between CSC 2.1 source names and stack IDs.

#### Data Source

The data source for this script is most_prob.csv, which includes all Chandra sources matched using the NWAY tool. (Not present in the repo)

#### Output

All sensitivity map tarballs will be stored in the ./output/ directory. You can use the generated CSV file to associate each CSC source name with its corresponding stack sensitivity map.

## Plotting Sensitivity Maps

A supplementary script, `plot_sens.py`, is available for plotting sensitivity maps. Ensure the relevant FITS files are located in the `./fits` directory. To plot a sensitivity map for a specific stack ID, use the following command:

```python3 plot_sens.py <stack_id>```

#### Example

```python3 plot_sens.py acisfJ0000115p321112_001```

Executing this command will generate and display a plot for the specified stack ID.