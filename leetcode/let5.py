"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成

"""


# 判断数组下标对应的两个字符是否相同
def check(s, start_index, end_index):
    if s[start_index] == s[end_index]:
        return True
    return False


if __name__ == '__main__':
    s = 'babad'

    letter_dict = {}
    index_dict = {}
    letter_len = 0

    for letter in s:
        index = 0
        # 当字母不在字典中时，将字母作为key，value为None
        if letter not in letter_dict:
            letter_dict[letter] = index
            index_dict[index] = letter
        # 当key冲突时，说明出现重复，校验中间是否相同
        else:
            check_res = check(s, letter_dict[letter], index)

            # 获取两者之间的长度
            letter_len = index - letter_dict[letter]
        # print(letter)

        # 数组下标向后移动以为
        index += 1