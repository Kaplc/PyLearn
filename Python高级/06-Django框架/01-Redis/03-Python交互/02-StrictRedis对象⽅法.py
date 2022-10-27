from redis import StrictRedis
import redis
"""
string: set, setex, mset, append, get, mget, key, 

keys: exists, type, delete, expire, getrange, ttl

hash: hset, hmset, hkeys, hget, hmget, hvals, hdel

list: lpush, rpush, linsert, lrange, lset, lrem

set:  sadd, smembers, srem

zset: zadd, zrange, zrangebyscore, zscore, zrem, zremrangebyscore
"""
if __name__ == '__main__':
    # 通过init创建对象，指定参数host、port与指定的服务器和端⼝连接，
    # host默认为localhost，port默认为6379，db默认为0
    sr = StrictRedis(
        host="127.0.0.1",
        port=6379,
        db=0
    )
    # 等效StrictRedis
    sr2 = redis.Redis()
    # string
    res1 = sr.get("str")
    res2 = sr2.get("str2")
    sr.set("str4", "333")
    print(res1.decode("utf-8"))
    print(res2)
