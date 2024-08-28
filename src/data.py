import pandas as pd
from astropy.io.votable import parse

def votable_to_pandas(votable_file):
    '''
    Converts votable to pandas dataframe.
    '''
    votable = parse(votable_file)
    table = votable.get_first_table().to_table(use_names_over_ids=True)
    return table.to_pandas()


def read_votable_to_dataframe(filepath, columns=None):
    """
    Read a VOTable file and convert it to a Pandas DataFrame.
    Optionally select specific columns.

    Parameters:
    - filepath: str, path to the VOTable file.
    - columns: list of str, specific columns to select (default is None).

    Returns:
    - pd.DataFrame
    """
    df = votable_to_pandas(filepath)
    if columns:
        df = df[columns]
    return df

def get_data(separation_threshold=1.3, theta_range=[0,3]):
    first_prob_df = pd.read_csv('data/most_prob_class_gaia_props.csv')
    all_stack_df = read_votable_to_dataframe('data/all_stacks.vot')

    # filter dataframe
    filtered_df = first_prob_df[
        (first_prob_df['separation'] <= separation_threshold) &
        (first_prob_df['min_theta_mean'] >= theta_range[0]) &
        (first_prob_df['min_theta_mean'] < theta_range[1])
    ]

    # merge filtered data with all_stack_df
    merged_df = pd.merge(
        filtered_df, 
        all_stack_df[['name', 'detect_stack_id']], 
        left_on='csc21_name',
        right_on='name'
    )

    # save stack ids
    stack_ids = merged_df['detect_stack_id'].unique()
    with open('stack_ids.txt', 'w') as f:
        f.write("#skip me\n")  # Add this line
        for id in stack_ids:
            f.write(f"{id}\n")

    # save associations
    associations_df = merged_df[['csc21_name', 'detect_stack_id']]
    associations_df.to_csv(
        f'associations_sep{separation_threshold}_theta{theta_range[0]}-{theta_range[1]}.csv', 
        index=False
    )

    print("generated data succesfully.")