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
        pop_france = df.loc['France']
        pop_japan = df.loc['Japan']

        pop_france = pop_france.reset_index()
        pop_france.columns = ["Year", "Population"]
        pop_france["Population"] = pop_france["Population"].apply(str_to_float)
        pop_france["Year"] = pop_france["Year"].astype(int)
        pop_france = pop_france[pop_france["Year"] <= 2050]

        pop_japan = pop_japan.reset_index()
        pop_japan.columns = ["Year", "Population"]
        pop_japan["Population"] = pop_japan["Population"].apply(str_to_float)
        pop_japan["Year"] = pop_japan["Year"].astype(int)
        pop_japan = pop_japan[pop_japan["Year"] <= 2050]

        pop_france["Country"] = "France"
        pop_japan["Country"] = "Japan"

        combined_df = pd.concat([pop_france, pop_japan])

        sns.lineplot(data=combined_df,
                     x="Year", y="Population", hue="Country")
        plt.title("Population Projections")
        plt.show()

    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    main()
