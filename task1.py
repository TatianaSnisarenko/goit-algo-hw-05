class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value) -> bool:
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            self.size += 1
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    self.size += 1
                    return True
            self.table[key_hash].append(key_value)
            self.size += 1
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    removed_value = pair[1]
                    del self.table[key_hash][index]
                    self.size -= 1
                    return removed_value
        return None

    def get_size(self):
        return self.size
