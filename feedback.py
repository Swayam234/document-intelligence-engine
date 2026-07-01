import pandas as pd

def save_feedback(file, predicted, corrected):

    row = {
        "file": file,
        "predicted": predicted,
        "corrected": corrected
    }

    try:
        df = pd.read_csv(
            "corrected_labels.csv"
        )
    except:
        df = pd.DataFrame(
            columns=[
                "file",
                "predicted",
                "corrected"
            ]
        )

    df.loc[len(df)] = row
    df.to_csv(
        "corrected_labels.csv",
        index=False
    )