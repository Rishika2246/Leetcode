from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        L = len(beginWord)
        
        # Pattern mapping
        patterns = defaultdict(list)
        for word in wordSet:
            for i in range(L):
                patterns[word[:i] + '*' + word[i+1:]].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                
                for nei in patterns[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
                
                patterns[pattern] = []  # optimization
        
        return 0