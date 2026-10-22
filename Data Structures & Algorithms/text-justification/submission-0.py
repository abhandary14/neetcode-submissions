class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0

        i = 0

        while i < len(words):
            # length of the current line + length of the current word that we want to append + number of spaces that need to be there (minimum no. of required spaces = length of line - 1 == len(line))
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            
            else:
                extra_space = maxWidth - length
                # we need to greedily distribute space
                remainder = extra_space % max(1, (len(line) - 1)) # need at least one, can't divide by zero
                space = extra_space // max(1, (len(line) - 1))

                for j in range(max(1, len(line) - 1)): # this needs to execute at least once
                    line[j] += " " * space
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0
        
        # the for loop doesn't add the last line, so we need to add it beforehand
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)

        return res

