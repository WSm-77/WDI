def vowel(ch):
    return 1 if ch in ['a', 'e', 'o', 'i', 'u', 'y'] else 0

def word(s1, s2):
    s1_vowel_cnt = 0
    s1_ascii_sum = 0
    for ch in s1:
        s1_vowel_cnt += vowel(ch)
        s1_ascii_sum += ord(ch)
    #end for
    n = len(s2)
    foundWord = ''
    def rek(index, s2_vowel_cnt, s2_ascii_sum, word2):
        if index == n:
            if s2_vowel_cnt == s1_vowel_cnt and s1_ascii_sum == s2_ascii_sum:
                nonlocal foundWord
                foundWord = word2
                return True
            else:
                return False
            #end if
        #end if
        return rek(index + 1, s2_vowel_cnt, s2_ascii_sum, '' + word2) or rek(index + 1, s2_vowel_cnt + vowel(s2[index]), s2_ascii_sum + ord(s2[index]), word2 + s2[index])
    #end def
    return (rek(0, 0, 0, ''), foundWord)

if __name__ == "__main__":
    s1 = "exe"
    s2 = "bulala"

    print(*word(s1, s2))