##############################################################
# Utils functions for cropping a dataset out of an
# excell sheet based on the value of the upper left corner
# of the dataframe
#############################################################
import pandas as pd
import numpy as np

##########################
# Find upper left corner #
##########################

def find_upper_left_corner_coord(df, value):
    # Get the x and y coordinates of the "value" cell
    x, y = np.where(df.values == value)
    return (x,y)

#######################################
# Find the X of the lower left corner #
#######################################

def find_lower_left_corner_x(df, x, y, len_x):
    
    # Loop through the potential length of the 
    # table rows
    for i in range(len_x):
        i = i+1
        # At each loop, go down one row
        loc_row = df.iloc[x + i, y]
    
        # Test if the row is empty, if
        # yes return the X of the previous 
        # non-empty cell
        if loc_row.isnull().bool():  
        
            lower_left_corner_x = loc_row.index
            return lower_left_corner_x
        
        # otherwise continue to next i
        else:
            continue

########################################
# Find the Y of the upper right corner #
########################################

def find_upper_right_corner_y(df, x, y, len_y):
    
    # Loop through the potential length of the 
    # table cols
    for i in range(len_y):
        i = i+1
        # Test if the row is empty, if
        # yes return the X of the previous 
        # non-empty cell
        loc_col = df.iloc[x, y + i]

        if loc_col.isnull().bool():

            upper_right_corner_y = loc_col.columns
            return upper_right_corner_y

        # otherwise continue to next i
        else:
            continue
            
##########################################
# Crop the table out of the excell sheet #
##########################################

def crop_df(df, x, y, x_end, y_end):
    
    cropped_df = df.iloc[x:x_end, y:y_end]
    
    return cropped_df
    
    
    