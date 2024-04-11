import psycopg2

def return_table_in_schema(schema_name,cursor):
    cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema_name}'")
    
    table_names = cursor.fetchall()
    
    tables = []
    
    for table_name in table_names:
        name = table_name[0]
        tables.append(name)
    
    return tables