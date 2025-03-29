class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(bed) - 1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                # plant a flower
                bed[i] = 1
                # increment count fo each flower planted
                count += 1

        return count >= n
        