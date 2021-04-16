import pandas as pd
import numpy as np
from utils.crop_df_utils import *

def get_table_v2(excel_table, sheet_name, value=None, offset=0):

    excel_table = excel_table
    offset = offset
    df = pd.read_excel(excel_table, sheet_name=sheet_name, header=None, skiprows=offset)
    
    ### PADDING: append an empty row and column to the excell sheet   
    
    # Add an empty row at the end of the table
    df = df.append(pd.Series(), ignore_index=True)
    # Add an empy column on the right side of the table
    df[len(df.columns)] = np.nan

    ### Find the coordinates of the different corners

    # Get the x and y coordinates of the upper left corner

    # If no names  for the sheet, we assume that an offset has been
    # specified so the upper left corner has coordinates (0,0)
    if value == None:
        # Need to be an array because these are coordinates
        # of the cell, otherwise will return the VALUE of 
        # the cell
        x, y = (np.array([0]), np.array([0]))

    # Otherwise look for the value name
    else:
        x, y = find_upper_left_corner_coord(df, value)
        if len(x) > 1:
            print("[INFO] {} cell has been detected with this value".format(len(x)))

    # From the row of the upper left corner until the potential end row (potential length of the table)
    len_x = [len(df.iloc[int(x):len(df), :]) for x in x]

    # From the col of the upper left corner until the potential the end col (potential length of the table)
    len_y = [len(df.columns[int(y):len(df.columns)]) for y in y]

    # Find the lower left corner of the table
    llc_x = [find_lower_left_corner_x(df, np.array([a]), np.array([b]), c) for a, b, c in zip(x, y, len_x)]

    # Find the upper right corner of the table
    urc_y = [find_upper_right_corner_y(df, np.array([a]), np.array([b]), c) for a, b, c in zip(x, y, len_y)]

    # llc_x and urc_y are Int64Index which is like a list, I need to get the ith element from the list
    # and then the first from the Int64Index
    d = [crop_df(df, int(a), int(b), int(c[0]), int(d[0])) for a,b,c,d in zip(x, y, llc_x, urc_y)]
    print("[INFO] The function has returned a list of {} tables".format(len(d)))
    
    # return the list of table
    return d