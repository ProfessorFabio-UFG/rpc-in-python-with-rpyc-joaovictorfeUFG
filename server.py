import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  # soma todos os valores do array
  def exposed_sum(self):
    return sum(self.value)

  # Remove todos os valores do array
  def exposed_clear(self):
    self.value = []
    return self.value

  # Remove o último item do array (se houver)
  def exposed_pop(self):
    if self.value:
        self.value.pop()
    return self.value

  # Retorna o maior valor do array
  def exposed_max(self):
    if self.value:
        return max(self.value)
    return None

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

