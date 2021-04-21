'''This python script is to extract each sheet in an Excel workbook as a new csv file'''

import os
import shutil
import logging
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", required=True, 
               help="path to input directory")
ap.add_argument("-o", "--output_dir", required=True, 
               help="path to ouput directory")
args = vars(ap.parse_args())

"""
Define the function that convert Excel file as csv.
The function creates a folder for each excel file
and fill the folder with the worksheets
"""
def xlsx_to_csv(input_dir, output_dir):
    
    # List all the files in the input directory (.xlsx or .xls files)
    xlsx_docs = os.listdir(input_dir)
    
    # Loop through all the excel files
    for i in range(len(xlsx_docs)):
        
        # Get the path of the sheet
        path_sheet = os.sep.join([input_dir, xlsx_docs[i]])
        
        # Get the name of the excel file
        excel_file = pd.ExcelFile(path_sheet)
        
        # list the worksheet names
        list_worksheet = excel_file.sheet_names

        # Take the name of the excel sheet only (without the extension)
        name_excel_table = excel_file.io.split("/")[-1].split(".")[0]

        # Create a path name for creating a directory for the excel file
        # where we will store all the individual worksheets
        folder_table_name = os.sep.join([output_dir, name_excel_table])

        # Create a new directory with the name of the excel file
        # OVERWRITE existing folder!
        if os.path.exists(folder_table_name) is True:
            shutil.rmtree(folder_table_name)
            logging.warning("Overwriting an existing folder")
                                
        os.mkdir(folder_table_name)
        
        # Loop through the worksheet of the excel table
        for i in range(len(list_worksheet)):
            # open the ith worksheet
            sheet = pd.read_excel(excel_file, list_worksheet[i])
    
            # save the sheet as a csv file in the output directory
            sheet.to_csv(os.sep.join([folder_table_name, list_worksheet[i]]) + ".csv")
            
if __name__ == "__main__":
    xlsx_to_csv(args["input_dir"], args["output_dir"])
        
        