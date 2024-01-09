# Constraints:
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output = []
        line_length = 0
        line_remain = []
        for i in range(len(words)):
            line_length += len(words[i])
            if line_length > maxWidth:
                blank_length = maxWidth - (line_length - len(words[i]) - 1)
                if len(line_remain) > 1:
                    prefix_num = len(line_remain) - 1
                    average_blank = blank_length // prefix_num
                    mod_blank = blank_length % prefix_num
                    line_str = ""
                    for j in line_remain:
                        if j != line_remain[-1]:
                            if mod_blank > 0:
                                line_str += words[j] + " " * (average_blank + 1) + " "
                            else:
                                line_str += words[j] + " " * (average_blank + 1)
                            mod_blank -= 1
                        else:
                            line_str += words[j]
                else:
                    line_str = words[line_remain[0]] + " " * (blank_length)

                output.append(line_str)
                line_remain = [i]
                line_length = len(words[i]) + 1  # +1 means at leat one blank

            else:
                line_remain.append(i)
                line_length += 1  # +1 means at leat one blank

        # last line is still remain in line_remain
        last_line_str = ""
        for item in line_remain:
            if item != line_remain[-1]:
                last_line_str += words[item] + " "
            else:
                remain_blank = maxWidth - len(last_line_str) - len(words[item])
                last_line_str += words[item] + " " * remain_blank
        output.append(last_line_str)
        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
    print(sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
    print(sol.fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
               "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
