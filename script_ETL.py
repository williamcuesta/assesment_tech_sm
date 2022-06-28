


import os 
from sys import path
import pandas as pd
import pymysql

path.append(os.path.realpath('./'))

_host="localhost"
_user="sm"
_password="sm"
_db_name="prueba_sm"

try:
    _connection = pymysql.connect(host=_host, user=_user, passwd=_password)
    _cursor = _connection.cursor()
    _cursor.execute('''USE {}'''.format(_db_name))

    print ("connection with db -> [OK]")
except:
    print ("error with db")      

def _read_document(file_name):
    try:
        print (f'document name: {file_name}')
        return pd.read_csv(r'{}'.format(file_name))
    except:
        return None

def _save_data_users(df):# ------------------------------------------------------------------------------------------------------------------------------------------
    
    try:
        df_ = df.dropna() # remove nan values if found have in id file
        for index, row in df_.iterrows():
            _cursor.execute("INSERT INTO `PP_users` (`u`, `techniques`, `items`, `n_items`, `ratings`, `n_ratings`) VALUES (%s, %s, %s, %s, %s, %s)", 
            (row['u'], row['techniques'], row['items'], row['n_items'], row['ratings'], row['n_ratings']))

        _connection.commit()
        return
    except Exception as error:
        print(f'An exception whith save data users! {error}')
        return
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def _save_data_RAW_recipes(df):# ------------------------------------------------------------------------------------------------------------------------------------------
    
    try:
        df_ = df.dropna() # remove nan values if found have in id file
        for index, row in df_.iterrows():

            # if row['id'] is None:
            #     print ("found none")
            _cursor.execute("INSERT INTO `RAW_recipes` (`id`, `name`, `minutes`, `contributor_id`, `submitted`, `tags`, `nutrition`, `n_steps` , `steps`, `description`, `ingredients`, `n_ingredients`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (row['id'], row['name'], row['minutes'], row['contributor_id'], row['submitted'], row['tags'], row['nutrition'], row['n_steps'], row['steps'], row['description'], row['ingredients'], row['n_ingredients']))

        _connection.commit()
        return
    except Exception as error:
        print(f'An exception whith save data RAW_recipes! {error}')
        return
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def _save_data_PP_recipes(df):# ------------------------------------------------------------------------------------------------------------------------------------------
    
    try:
        df_ = df.dropna() # remove nan values if found have in id file
        for index, row in df_.iterrows():
            _cursor.execute("INSERT INTO `PP_recipes` (`i`, `id_`, `name_tokens`, `ingredient_tokens`, `steps_tokens`, `techniques`, `calorie_level`, `ingredient_ids`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
            (row['i'], row['id'], row['name_tokens'], row['ingredient_tokens'], row['steps_tokens'], row['techniques'], row['calorie_level'], row['ingredient_ids']))

            _connection.commit()
            return
    except Exception as error:
        print(f'An exception whith save data PP_recipes! {error}')
        return
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def _save_data_RAW_interactions(df):# ------------------------------------------------------------------------------------------------------------------------------------------
    
    try:
        df_ = df.dropna() # remove nan values if found have in id file
        for index, row in df_.iterrows():
            try:
                _cursor.execute("INSERT INTO `RAW_interactions` (`user_id`, `recipe_id`, `date`, `review`) VALUES (%s, %s, %s, %s)", 
                (row['user_id'], row['recipe_id'], row['date'], row['review']))
            except:
                _connection.commit()

        _connection.commit()
        _connection.close()
        return
    except Exception as error:
        _connection.commit()
        _connection.close()
        print (f"{row['user_id']}, {row['recipe_id']}, {row['date']}, {row['review']}")
        print(f'An exception whith save data RAW_interactions! {error}')
        return
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            

def main():
    df = _read_document('data_test/data_test/PP_users.csv') # >>>>>>>>>>>>>>>>>>>>>PP_users|
    if df is not None:
        print(f'_read_document PP_users ok')
        _save_data_users(df)

    df = _read_document('data_test/data_test/RAW_recipes.csv') # >>>>>>>>>>>RAW_recipes.csv|
    if df is not None:
        print(f'_read_document RAW_recipes ok')
        _save_data_RAW_recipes(df)

    df = _read_document('data_test/data_test/PP_recipes.csv') # >>>>>>>>>>>RAW_recipes.csv|
    if df is not None:
        print(f'_read_document PP_recipes ok')
        _save_data_PP_recipes(df)

    df = _read_document('data_test/data_test/RAW_interactions.csv') # >>>>>>>>>>>RAW_recipes.csv|
    if df is not None:
        print(f'_read_document RAW_interactions ok')
        _save_data_RAW_interactions(df)

    print("finish script")


if __name__ == '__main__':    
    main()