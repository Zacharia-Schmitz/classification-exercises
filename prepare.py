from sklearn.model_selection import train_test_split


def split_data(df, stratify=None):
    """
    Take in a DataFrame and return train, validate, and test DataFrames; stratify on a specified variable.

    Parameters:
    -----------
    df : pandas DataFrame
        The DataFrame to be split into train, validate, and test DataFrames.
    stratify : str, default=None
        The name of the column to stratify the split on. If None, the split will not be stratified.

    Returns:
    --------
    train : pandas DataFrame
        The training set.
    validate : pandas DataFrame
        The validation set.
    test : pandas DataFrame
        The test set.
    """
    train_validate, test = train_test_split(
        df, test_size=0.2, random_state=123, stratify=df[stratify]
    )
    train, validate = train_test_split(
        train_validate,
        test_size=0.3,
        random_state=123,
        stratify=train_validate[stratify],
    )
    print(f"Train: {train/df}")
    print(f"Validate: {validate/df}")
    print(f"Test: {test/df}")

    return train, validate, test
