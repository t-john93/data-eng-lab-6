import pandas as pd
import numpy as np

census_tract = '/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab6/acs2017_census_tract_data.csv'
county_data = '/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab6/COVID_county_data.csv'
grouped_census = '/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab6/census_aggregate.csv'
grouped_covid = '/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab6/grouped_covid.csv'

census_tract_df = pd.read_csv(census_tract, low_memory=False)
covid_county_df = pd.read_csv(county_data, low_memory=False)

census_df = census_tract_df.groupby(['State', 'County']).sum().reset_index()
covid_df_gouped = covid_county_df.groupby(['state', 'county', 'fips']).sum().reset_index()

joined_covid_df = covid_county_df.join(covid_df_gouped,on='county',lsuffix='origin',rsuffix='grouped')

print(joined_covid_df)
# december_cases = pd.DataFrame(['County', 'TotalCases', 'TotalDeaths', ''])

# print(covid_df)

# for ind, rowin df.iterrows():
#         df.at[ind, 'County'] = ' '.join(row['County'].split(' ')[:-1])

# census_df.to_csv(grouped_census,index=False)
# covid_df.to_csv(grouped_covid,index=False)

# new_df = pd.DataFrame(data=None, index=None, columns=['County', 'Cases', 'Deaths', 'Deaths in Dec 2020'])


# print(census_df)
