class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for cut in range(len(word) + 1):
                prefix = word[:cut]
                suffix = word[cut:]

                # If prefix is palindrome, reversed suffix can go before word
                if prefix == prefix[::-1]:
                    candidate = suffix[::-1]
                    if candidate in index and index[candidate] != i:
                        result.append([index[candidate], i])

                # If suffix is palindrome, reversed prefix can go after word
                # cut != len(word) prevents duplicate pairs
                if cut != len(word) and suffix == suffix[::-1]:
                    candidate = prefix[::-1]
                    if candidate in index and index[candidate] != i:
                        result.append([i, index[candidate]])

        return result