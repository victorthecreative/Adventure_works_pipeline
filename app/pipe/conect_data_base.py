import psycopg2

def conect_postgres(database, user,host,password,port):
  """
  Função para se conectar ao banco postgres usando o psycopg2
  
  args: 
    database (str): Nome do banco de dados que vamos nos conectar
    user (str): Usuário que vamos usar para conectar ao banco
    hot (str): Host de conexão com o banco
    password (str): Senha para nos conectarmos ao banco
    port(str): Porta que usaremos na conexão 
  
  return: cursor para realizar as queryes
  """
  conn = psycopg2.connect(database = f"{database}", 
                          user = f"{user}", 
                          host= f"{host}",
                          password = f"{password}",
                          port = f"{port}"  )

  cursor = conn.cursor()
  
  return cursor

if __name__ == '__main__':
  cursor = conect_postgres('mentoria_eng_adventure_works','mentoria_eng_adventure_works_user','dpg-cnti0n0l6cac73d68p4g-a.oregon-postgres.render.com','IrVhx4ACTOKR5DxYsOgud6Rv6DQQ4ZRW','5432')
  cursor.execute("SELECT schema_name FROM information_schema.schemata")
  schema_name = cursor.fetchall()
  print(schema_name)