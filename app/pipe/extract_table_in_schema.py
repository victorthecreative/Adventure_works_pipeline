import psycopg2
import pandas as pd
import os

def extract_tables (schema_name, table_name,cursor):
    cursor.execute(f"SELECT * FROM {schema_name}.{table_name}")
    ##num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    dataframe = pd.DataFrame(cursor.fetchall())
    if len(dataframe.columns) != 0:
        dataframe.columns = field_names
    else:
        print(f"A tabela {table_name} foi excluida por estar vazia")
    path_save = f'./{schema_name}/'
    file_path = os.path.join(path_save, f'{table_name}.csv')
    dataframe.to_csv(file_path, index=False) 
    
    return file_path