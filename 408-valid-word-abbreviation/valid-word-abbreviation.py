class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0
        while abbr_ptr < len(abbr) and word_ptr < len(word):
            # check if abbreviation is a digit
            if abbr[abbr_ptr].isdigit():
                # check for leading zeros
                if abbr[abbr_ptr] == '0':
                    return False 

                # get the number
                number = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    number = number * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                
                # move word pointer by amount in number
                word_ptr += number
            else:
            # check if abbreviation is a string
                # if character don't match return False
                if word_ptr >= len(word) or word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr += 1
                abbr_ptr += 1
        return word_ptr == len(word) and abbr_ptr == len(abbr)
            

        