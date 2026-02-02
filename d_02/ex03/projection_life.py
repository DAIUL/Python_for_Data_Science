import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def main():
    '''
    This program loads file
    and display the requested year informations
    '''
    try:
        df_revenue = load("Revenu par personne ajusté.csv")
        df_lifespan = load("Espérance de vie.csv")

        df_lifespan_1900 = df_lifespan['1900']
        df_revenue_1900 = df_revenue['1900']
        df_1900_compare = pd.concat([df_lifespan_1900, df_revenue_1900],
                                    axis=1)
        df_1900_compare.columns = ['Life Excpectancy',
                                   'Gross domestic product']

        sns.scatterplot(data=df_1900_compare,
                        x='Gross domestic product', y='Life Excpectancy')
        plt.title('1900')
        plt.show()

    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    main()
