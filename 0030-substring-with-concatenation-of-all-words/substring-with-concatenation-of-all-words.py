class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        from collections import Counter
        word_map = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            curr_map = {}
            count = 0
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                
                if word in word_map:
                    curr_map[word] = curr_map.get(word, 0) + 1
                    count += 1
                    
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        res.append(left)
                else:
                    curr_map.clear()
                    count = 0
                    left = j + word_len
        
        return res