class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxtypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total_units = 0

        for boxtype in sorted_boxtypes:
            if truckSize == 0:
                break

            min_boxtype = min(boxtype[0], truckSize)
            total_units += (min_boxtype * boxtype[1])
            truckSize -= min_boxtype

        return total_units
        