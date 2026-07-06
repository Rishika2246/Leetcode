class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # One slot for the root

        for node in preorder.split(","):
            slots -= 1  # Current node occupies one slot

            if slots < 0:
                return False

            if node != "#":
                slots += 2  # Non-null node creates two child slots

        return slots == 0