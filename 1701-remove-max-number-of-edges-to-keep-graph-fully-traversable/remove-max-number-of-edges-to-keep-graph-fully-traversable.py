class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def union(alice, node1, node2):
            parent = alice_parent if alice else bob_parent
            size = alice_size if alice else bob_size

            root1, root2 = find(alice, node1), find(alice, node2)
            if root1 != root2:
                if size[root1] >= size[root2]:
                    parent[root2] = root1
                    size[root1] += size[root2]
                else:
                    parent[root1] = root2
                    size[root2] += size[root1]

        def find(alice, node):
            parent = alice_parent if alice else bob_parent
            while node != parent[node]:
                temp = parent[node]
                node = parent[temp]
            return node
        
        alice_parent = {i : i for i in range(1, n + 1)}
        alice_size = {i : 1 for i in range(1, n + 1)}
        bob_parent = {i : i for i in range(1, n + 1)}
        bob_size = {i : 1 for i in range(1, n + 1)}

        edges.sort(reverse = True)
        removed = 0
        for typ, node1, node2 in edges:
            if typ == 3:
                if (find(True, node1) == find(True, node2) and
                    find(False, node1) == find(False, node2)):
                    removed += 1
                else:
                    union(True, node1, node2)
                    union(False, node1, node2)
            elif typ == 1:
                if find(True, node1) == find(True, node2):
                    removed += 1
                else:
                    union(True, node1, node2)
            else:
                if find(False, node1) == find(False, node2):
                    removed += 1
                else:
                    union(False, node1, node2)
        
        alice, bob = set(), set()
        for i in range(1, n + 1):
            alice.add(find(True, i))
            bob.add(find(False, i))
        
        if len(alice) == len(bob) == 1:
            return removed
        return -1
                

    