class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix_word = ''
        ind = word.find(ch)
        if ind == -1 or ind == 0:
            return word

        if ind == len(word) - 1:
            prefix_word += word[ind] + reverse_word(word[:ind])
        elif ch in word:
            prefix_word += word[ind] + reverse_word(word[:ind]) + word[ind+1:]
        return prefix_word

def reverse_word(strg):
    word_lst = list(strg)
    left = 0
    right = len(word_lst) - 1
    while left < right:
        word_lst[left], word_lst[right] = word_lst[right], word_lst[left]
        left += 1
        right -= 1
    return ''.join(word_lst)