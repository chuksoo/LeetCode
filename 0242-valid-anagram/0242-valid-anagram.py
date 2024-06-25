class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for item in s.lower():
            s_dict[item] = s_dict.get(item, 0) + 1
        for val in t.lower():
            t_dict[val] = t_dict.get(val, 0) + 1
        return (s_dict == t_dict)
        