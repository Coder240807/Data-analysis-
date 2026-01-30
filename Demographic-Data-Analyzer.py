import numpy as np
import pandas as pd

df=pd.read_csv('adult.csv')

race = pd.Series({"white": df['race'].value_counts()['White'],
        "black": df['race'].value_counts()['Black']})

average_age = df['age'].mean().round(1)
 
percent_of_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1) 

degrees = ['Bachelors', 'Masters', 'Doctorate']

advanced_education_grp = df.loc[df['education'].isin(degrees), 'income']
percent_of_ppl_advance50k = round(advanced_education_grp.value_counts(normalize=True)['>50K'] * 100, 1)

not_advanced_education_grp = df.loc[~df['education'].isin(degrees), 'income']
percent_of_ppl_notadvance50k = round(not_advanced_education_grp.value_counts(normalize=True)['>50K'] * 100, 1)

min_work_hours = df['hours.per.week'].min()

percent_of_min_workers = round(df.loc[df['hours.per.week'] == min_work_hours, 'income'].value_counts(normalize=True)['>50K'] * 100, 1)

subset = df.loc[df['income'] == '>50K', 'native.country']
vc = subset.value_counts(normalize=True)
highest_earning_country = vc.index[0]
highest_earning_country_percentage = round(vc.iloc[0] * 100, 1)

most_popular_us_occupation_50k = df.loc[(df['native.country'] == 'United-States') & (df['income'] == '>50K'), 'occupation'].value_counts().idxmax()
print(most_popular_us_occupation_50k)
