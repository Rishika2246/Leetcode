class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0
        for b in data:
            if need:
                if (b >> 6) != 0b10:
                    return False
                need -= 1
            else:
                if (b >> 7) == 0:
                    continue
                if (b >> 5) == 0b110:
                    need = 1
                elif (b >> 4) == 0b1110:
                    need = 2
                elif (b >> 3) == 0b11110:
                    need = 3
                else:
                    return False
        return need == 0