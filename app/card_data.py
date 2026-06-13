import pandas as pd

def read_df(interval_selection):
    df = pd.read_csv(f'app/interval_data/{interval_selection}.csv')
    df.index += 1    
    return df

def row_count(interval_selection):
    '''
    Purpose: 
        To get the total number of cards of the database.
        (Used to determine the total initial number of cards at the start of the game.)
    
    :param interval_selection: This is used as the table name of the database.
    '''
    #df = pd.read_csv(f'app/interval_data/{interval_selection}.csv')
    df = read_df(interval_selection)
    total_rows = len(df)
    return total_rows

def select_card(card_id, interval_selection):
    '''
    Purpose: To select a specific card from the database.
    
    :param card_id: The row number used locate the card info in the database.
    :param interval_selection: This is used as the table name of the database.
    '''
    
    df = read_df(interval_selection)
    row = df.loc[card_id]
    row = row.tolist()
    print(card_id)
    return row