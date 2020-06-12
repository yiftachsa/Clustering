import pandas as pd
import numpy as np


def read_csv(path):
    try:
        data_frame = pd.read_csv(path)
        return data_frame
    except:
        print("an error occurred reading the csv file")  # TODO: print to GUI


def read_excel(path):
    try:
        data_frame = pd.read_excel(path)
        return data_frame
    except Exception as e:
        print(e)
        print("an error occurred reading the excel file")  # TODO: print to GUI


def fill_missing_values_numeric(data_frame):
    numeric_columns = list(data_frame.select_dtypes(include=[np.number]).columns.values)
    for column_name in numeric_columns:
        data_frame[column_name].fillna(data_frame[column_name].mean(), inplace=True)
    # df.apply(lambda x: sum(x.isnull()),axis=0) # Getting the numbers of missing values in each feature
    return data_frame


def z_score_standardization(data_frame):
    columns = list(data_frame.select_dtypes('float64').columns.values)
    for column_name in columns:
        data_frame[column_name] = (data_frame[column_name] - data_frame[column_name].mean()) / data_frame[
            column_name].std(ddof=0)
    return data_frame


def group_by_country(data_frame):
    new_columns_names = list(data_frame.select_dtypes('float64').columns.values)
    new_columns_names.insert(0, 'country')
    result_data_frame = pd.DataFrame(columns=new_columns_names)

    countries = data_frame.country.unique()
    for country in countries:
        # A sub-data frame containing all the years of this country
        country_df = data_frame.loc[data_frame['country'].eq(country)]
        new_row = {'country': [country]}  # a new row representing this country
        columns = list(country_df.select_dtypes('float64').columns.values)
        for column_name in columns:
            column_mean = country_df[column_name].mean()
            new_row[column_name] = [column_mean]
        new_country_df = pd.DataFrame(new_row)
        result_data_frame = result_data_frame.append(new_country_df, ignore_index=True)
    return result_data_frame


df = read_excel(
    "D:\\Documents\\Studies\\Documents for higher education\\Courses\\Year 3 Semester 2\\מדעי הנתונים ובינה עסקית\\עבודות להגשה\\תרגיל 4\\Dataset.xlsx")
# df.apply(lambda x: sum(x.isnull()),axis=0)
df = fill_missing_values_numeric(df)
df = z_score_standardization(df)
df_grouped = group_by_country(df)