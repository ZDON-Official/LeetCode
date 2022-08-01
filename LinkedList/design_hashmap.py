class MyHashMap:

    def __init__(self):
        self.hash = [None]*(pow(10,6)+1)

    def put(self, key: int, value: int) -> None:
        try:
            self.hash[key] = value
        except:
            pass

    def get(self, key: int) -> int:
        val = self.hash[key]
        print(val)
        
        if val != None:
            return val
        else:
            return -1
        
    def remove(self, key: int) -> None:
        try:
            self.hash[key] = None
        except:
            pass