class MyHashSet:

    def __init__(self):

        self.hash_set = {}

    def add(self, key: int) -> None:

        self.hash_set[key] = True

    def remove(self, key: int) -> None:

        if self.hash_set.get(key):
            del self.hash_set[key]

    def contains(self, key: int) -> bool:

        if self.hash_set.get(key):
            return True
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)