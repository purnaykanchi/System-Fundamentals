class FullyAssociativeCache:
    def __init__(self, size):
        self.size=size
        self.cache={}
    def access_memory(self, address):
        if address in self.cache:
         return True
        else:
             if len(self.cache)>=self.size:
                lru_key=min(self.cache, key=self.cache.get)
                del self.cache[lru_key]
                self.cache[address]=True
        return False
cache_size_fully_associative = 4
cache_fully_associative = FullyAssociativeCache(cache_size_fully_associative)
memory_addresses = [0, 1, 2, 3, 0, 4, 1, 5]
for address in memory_addresses:
    if cache_fully_associative.access_memory(address):
        print(f"Cache hit for address{address}")
    else:
        print(f"Cache miss for address{address}")