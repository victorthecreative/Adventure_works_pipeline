import psycopg2
import os

def list_schema(cursor):
    cursor.execute("SELECT schema_name FROM information_schema.schemata")

    schema_names = cursor.fetchall()

    names_schema = []

    for schema_name in schema_names:
        name = schema_name[0]
        names_schema.append(name)
        
    remove_list = ['sa', 'pu','pr','hr','pe','public', 'information_schema', 'pg_catalog' ]
    for i in remove_list:
        names_schema.remove(i)    

    for name in names_schema:
        dir_name = name
        if not os.path.exists(f"./{dir_name}"):
            os.makedirs(f"./{dir_name}")
            print(f'pasta {dir_name} foi criada')
        else:
            print(f"Pasta {dir_name} ja existe")
    
    return names_schema