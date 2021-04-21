# Some convenient functions for working with databases (Python!)

### crop_df_utils.py

File composed of functions to find the position a dataset in an excel table. Used in **get_table_v2.py**.

### get_table_v2.py

Given an excel sheet, a sheet name, a value representing the upper left corner of a table and an offset (optional), returns a list of dataframes

### xlsx_to_csv

Given an input and output directory convert excel files into csv files. Create a folder for each excel file. Folders are populated with the different worksheets
