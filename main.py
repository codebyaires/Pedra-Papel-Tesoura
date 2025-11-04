import redis 

r = redis.Redis(host='10.1.69.134', port=6379, db=0)
r.ping()

# cria uma sala

# r.hset("2367", "p1", "")
r.hset("2367", "p2", "1")

# mostra resultados
dados = r.hgetall("2367")