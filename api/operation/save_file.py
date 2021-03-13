def save_df_as_csv(df, file_name):
    return df.to_csv('data/' + file_name + '.csv', index=True)
