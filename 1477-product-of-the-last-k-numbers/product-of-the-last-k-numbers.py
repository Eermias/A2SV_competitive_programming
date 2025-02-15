class ProductOfNumbers:

    def __init__(self):
        self.last_zero = float('inf')
        self.product = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.product.append(1)
        else:
            self.product.append(num)

        self.last_zero += 1
        if num == 0:
            self.last_zero = 1
        
        if len(self.product) > 1:
            self.product[-1] *= self.product[-2]
        
    def getProduct(self, k: int) -> int:
        if k >= self.last_zero:
            return 0
        return self.product[-1] // self.product[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)