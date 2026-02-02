import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load


def main():
    '''
    This program loads a file
    and displays the requested country informations
    '''
    try:
        dataset = load("Espérance de vie.csv")
        row_ds = dataset.loc['France']

        row_ds = row_ds.reset_index()
        row_ds.columns = ["Year", "Life excpectancy"]
        row_ds["Year"] = row_ds["Year"].astype(int)

        sns.lineplot(data=row_ds, x="Year", y="Life excpectancy")
        plt.title("France Life excpectancy Projections")
        plt.show()

    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    main()
