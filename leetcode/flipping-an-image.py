class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        for row_idx in range(row):
            l, r = 0, col - 1
            while l < r:
                image[row_idx][l], image[row_idx][r] = image[row_idx][r], image[row_idx][l]
                l += 1
                r -= 1

        for r in range(row):
            for c in range(col):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0

        return image 