import pandas as pd
import click

@click.command()
@click.option('--city', default='San Francisco', help='City to search for taco trucks')
def get_taco_trucks(city):
    df = pd.read_csv('path/to/your/csv')
    taco_trucks = df[df['fooditems'].str.contains('taco', case=False, na=False)]
    for index, row in taco_trucks.iterrows():
        print(row['applicant'])

if __name__ == '__main__':
    get_taco_trucks()
