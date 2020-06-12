from pre_processing import preprocess as pp

df = pp.read_excel(
    "D:\\Documents\\Studies\\Documents for higher education\\Courses\\Year 3 Semester 2\\מדעי הנתונים ובינה עסקית\\עבודות להגשה\\תרגיל 4\\Dataset.xlsx")
# df.apply(lambda x: sum(x.isnull()),axis=0)
df = pp.fill_missing_values_numeric(df)
df = pp.z_score_standardization(df)
df_grouped = pp.group_by_country(df)

print(df_grouped.columns.values)