import time
from pipe.conect_data_base import conect_postgres
from pipe.extract_table_in_schema import extract_tables
from pipe.list_schema import list_schema
from pipe.list_table import return_table_in_schema


if __name__ == "__main__":
  cursor = conect_postgres('mentoria_eng_adventure_works','mentoria_eng_adventure_works_user','dpg-cnti0n0l6cac73d68p4g-a.oregon-postgres.render.com','IrVhx4ACTOKR5DxYsOgud6Rv6DQQ4ZRW','5432')
  try:
      names_schema = list_schema(cursor)

      for schema_name in names_schema:
          schema = schema_name
          tables = return_table_in_schema(f"{schema}",cursor)
          for table in tables:
              table_query = table
              extract_tables(schema, table_query,cursor)

              time.sleep(1)  # Espera por 1 segundo entre cada iteração
  except:
      print(f'erro no schema {schema} e na tabela {table_query}')
      pass