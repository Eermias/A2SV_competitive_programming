class Node:
    def __init__(self, next = None, prev = None, val = 0, key = -1):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapp = {} #key : node
        self.cache = Node() 
        self.tail = self.cache
        

    def get(self, key: int) -> int:
        if key in self.mapp:
            node = self.mapp[key]
            if self.tail != self.mapp[key]:
                behind = self.mapp[key].prev
                forward = self.mapp[key].next
                behind.next = forward
                forward.prev = behind

                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            return node.val
        else:
            return -1



        

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            node = self.mapp[key]
            node.val = value
            if node != self.tail:
                behind = self.mapp[key].prev
                forward = self.mapp[key].next
                behind.next = forward
                forward.prev = behind

                self.tail.next = node
                node.prev = self.tail
                self.tail = node
        else:
            if self.capacity == 0:
                #remove the LRU Cache
                remove = self.cache.next
                if remove == self.tail:
                    self.tail = self.cache
                    self.cache.next = None
                else:
                    self.cache.next = remove.next
                    remove.next.prev = self.cache

                ke = remove.key
                self.mapp.pop(ke)
                #print(self.mapp)

                self.capacity += 1

            #add the new cache
            new_node = Node(None, self.tail, value, key)
            self.tail.next = new_node
            self.tail = new_node
            self.mapp[key] = new_node

            self.capacity -= 1


            

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)