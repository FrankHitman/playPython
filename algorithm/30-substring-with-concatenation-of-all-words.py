# Constraints:
# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

class Solution:
    # solution from https://www.youtube.com/watch?v=-wlDdMmaYwI&ab_channel=CodingNinja
    # when submitted on leetcode, got "Time Limit Exceeded"
    # 8003ms runtime
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        hashmap_w = {}
        for i in words:
            hashmap_w[i] = hashmap_w.get(i, 0) + 1
        word_len = len(words[0])
        window_len = word_len * len(words)
        res = []
        for i in range(len(s) - word_len + 1):
            hashmap_s = {}
            j = i
            while j < i + window_len:
                cur_word = s[j:j + word_len]
                if cur_word not in hashmap_w.keys():
                    break
                hashmap_s[cur_word] = hashmap_s.get(cur_word, 0) + 1
                if hashmap_s[cur_word] > hashmap_w[cur_word]:
                    break
                j += word_len
            if j == i + window_len:
                res.append(i)
        return res

    # solution is inspired by https://www.youtube.com/watch?v=jSto0O4AJbM&ab_channel=NeetCode
    # when submitted on leetcode, got "Time Limit Exceeded", the #179 testcase is s="aaa..." words=["a","a","a"...]
    def findSubstring_my(self, s: str, words: list[str]) -> list[int]:
        step = len(words[0])
        if len(s) < (step * len(words)):
            return []
        hashmap_w = dict()
        hashmap_s = dict()
        for i in words:
            if i not in hashmap_w.keys():
                hashmap_w[i] = 1
                hashmap_s[i] = 0
            else:
                hashmap_w[i] += 1
        target_items = len(hashmap_w)
        have_items = 0

        start = 0
        stop = start + step
        match_list = []
        while stop <= len(s):
            match_start = start
            while stop <= len(s) and s[start:stop] in hashmap_w.keys():
                hashmap_s[s[start:stop]] += 1
                if hashmap_s[s[start:stop]] == hashmap_w[s[start:stop]]:
                    have_items += 1
                elif hashmap_s[s[start:stop]] > hashmap_w[s[start:stop]]:
                    # reset start pointer
                    start = match_start
                    self.reset_hashmap(hashmap_s)
                    break
                if have_items == target_items:
                    match_list.append(match_start)
                    # reset start pointer to find another matched permutation
                    start = match_start
                    self.reset_hashmap(hashmap_s)
                    break
                start += step
                stop = start + step
                # preprocessing the next judgement to reset hashmap and pointer
                if s[start:stop] not in hashmap_w.keys():
                    start = match_start
                    self.reset_hashmap(hashmap_s)
                    break

            start += 1
            stop = start + step
            have_items = 0
            # self.reset_hashmap(hashmap_s)
        return match_list

    def reset_hashmap(self, m):
        for key in m.keys():
            m[key] = 0

    # other people's solution with 101ms runtime
    def findSubstring3(self, s: str, words: list[str]) -> list[int]:
        if not words or not s:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = {}

        # Create a frequency map for words
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        # Check each possible window in the string, outer for only loop word_length times
        for i in range(word_length):
            left = i
            count = 0
            temp_word_count = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in word_count:
                    temp_word_count[word] = temp_word_count.get(word, 0) + 1
                    count += 1

                    # instead of break to loop from the beginning, reducing runtime
                    while temp_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        temp_word_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == len(words):
                        result.append(left)
                else:
                    temp_word_count.clear()
                    count = 0
                    left = j + word_length

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
    print(sol.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
    print(sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]))
    print(sol.findSubstring3(s="aaaaaa", words=['a', 'a', 'a']))

# output
# [0, 9]
# []
# [6, 9, 12]
# [8]
# [0, 1, 2, 3]