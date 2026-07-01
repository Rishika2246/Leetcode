from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        L = len(beginWord)
        
        # Pattern mapping
        patterns = defaultdict(list)
        for word in wordSet:
            for i in range(L):
                patterns[word[:i] + '*' + word[i+1:]].append(word)
        
        # BFS (store parents only)
        parents = defaultdict(list)
        level = {beginWord}
        visited = set()
        found = False
        
        while level and not found:
            next_level = set()
            visited |= level
            
            for word in level:
                for i in range(L):
                    pattern = word[:i] + '*' + word[i+1:]
                    
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            if nei == endWord:
                                found = True
                            
                            parents[nei].append(word)
                            next_level.add(nei)
            
            level = next_level
        
        # DFS (build paths backwards)
        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for p in parents[word]:
                dfs(p, path + [p])
        
        if found:
            dfs(endWord, [endWord])
        
        return res