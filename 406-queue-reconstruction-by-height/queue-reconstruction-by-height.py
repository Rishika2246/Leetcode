class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # __define-ocg__
        people.sort(key=lambda x: (-x[0], x[1]))

        varOcg = []

        for person in people:
            varOcg.insert(person[1], person)

        return varOcg