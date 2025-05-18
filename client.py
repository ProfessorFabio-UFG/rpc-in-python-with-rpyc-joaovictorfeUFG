import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print ("Lista inicial:", conn.root.exposed_value())
  print("Adicionando valores aleatórios:")
  for _ in range(5):
    n = random.randint(1, 10)
    conn.root.exposed_append(n)
    print(f"Adicionado: {n}")

  print("Lista atual:", conn.root.exposed_value())
  print("Soma:", conn.root.exposed_sum())
  print("Maior valor:", conn.root.exposed_max())

  # Remover o último item
  conn.root.exposed_pop()
  print("Após remover o último item:", conn.root.exposed_value())

  # Remover todos os valores da lista
  conn.root.exposed_clear()
  print("Após remover todos os valores da lista:", conn.root.exposed_value())
