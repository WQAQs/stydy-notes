'''
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，
返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

'''
## 1.暴力解法，leetcode超时
import operator
def findAnagrams(s,p):
    def check(subs,p):
        m = len(subs)
        n = len(p)
        if m != n:return False
        for char in p:
            if p.count(char) != subs.count(char):
                return False
        return True
    m = len(s)
    n = len(p)
    res = []
    l = 0
    while l <= m - n:
        if check(s[l:l+n],p):
            res.append(l)
        l += 1
    return res

if __name__ == "__main__":
    res = findAnagrams("cbaebabacd","abc")
    res
    str = "asdfas"
    res = str.count("as")
    res
    # def check1(subs,p):
    #     m = len(subs)
    #     n = len(p)
    #     if m != n:return False
    #     freqm = [0 for i in range(256)]
    #     freqn = [0 for i in range(256)]
    #     for char in subs:
    #         freqm[ord(char)] += 1
    #     for char in p:
    #         freqn[ord(char)] += 1
    #     return operator.eq(freqm,freqn)
