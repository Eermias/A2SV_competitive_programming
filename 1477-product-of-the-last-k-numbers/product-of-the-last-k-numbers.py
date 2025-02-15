class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
        else:
            self.product.append(num)
            self.product[-1] *= self.product[-2]
        
    def getProduct(self, k: int) -> int:
        if k >= len(self.product):
            return 0
        return self.product[-1] // self.product[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)