def test_cleaner_no_nan():
    import pandas as pd
    from src.Preparation.automates_cleaner import AutomateCleaner

    df = pd.read_csv("data/raw/automates.csv")
    cleaned = AutomateCleaner(df).clean()

    assert not cleaned.isnull().any().any()
