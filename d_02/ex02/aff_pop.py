import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def str_to_float(value: str) -> float:
    '''
    This function takes a string with a numeral value
    and turns it into a float

    :type value: str
    :rtype: float
    '''
    value = value.strip().lower()
    multipliers = {
        'k': 1_000,
        'm': 1_000_000,
        'b': 1_000_000_000
    }

    if value[-1] in multipliers:
        return float(value[:-1]) * multipliers[value[-1]]
    return float(value)


def main():
    '''
    This program loads file
    and displays the requested courties informations
    '''
    try:
        df = load("Population Totale.csv")
        row_df = df.loc['France']
        row_df_2 = df.loc['Japan']

        row_df = row_df.reset_index()
        row_df.columns = ["Year", "Population"]
        row_df["Population"] = row_df["Population"].apply(str_to_float)
        row_df["Year"] = row_df["Year"].astype(int)
        row_df = row_df[row_df["Year"] <= 2050]

        row_df_2 = row_df_2.reset_index()
        row_df_2.columns = ["Year", "Population"]
        row_df_2["Population"] = row_df_2["Population"].apply(str_to_float)
        row_df_2["Year"] = row_df_2["Year"].astype(int)
        row_df_2 = row_df_2[row_df_2["Year"] <= 2050]

        row_df["Country"] = "France"
        row_df_2["Country"] = "Japan"

        combined_df = pd.concat([row_df, row_df_2])

        sns.lineplot(data=combined_df,
                     x="Year", y="Population", hue="Country")
        plt.title("Population Projections")
        plt.show()

    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    main()
