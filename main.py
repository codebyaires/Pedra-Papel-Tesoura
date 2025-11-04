import redis 

# Mude sua linha de conexão para isto:
r = redis.Redis(host='10.1.69.134', port=6379, db=0, decode_responses=True)
r.ping()

# cria uma sala

# r.hset("2367", "p1", "")
r.hset("2367", "p2", "3")

# mostra resultados
dados = r.hgetall("2367")
print(dados)