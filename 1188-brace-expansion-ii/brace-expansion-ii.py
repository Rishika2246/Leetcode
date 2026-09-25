from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.s = expression
        self.i = 0
        result = sorted(self._parse_seq())
        return result

    def _parse_seq(self):
        # parse a sequence of terms (concatenation) until ',' or '}' or end
        seq_sets = []
        while self.i < len(self.s) and self.s[self.i] not in ',}':
            seq_sets.append(self._parse_term())
        # cartesian product of all terms in the sequence
        result = {""}
        for term_set in seq_sets:
            result = {a + b for a in result for b in term_set}
        return result

    def _parse_term(self):
        if self.s[self.i] == '{':
            self.i += 1  # consume '{'
            options = set()
            options |= self._parse_seq()
            while self.i < len(self.s) and self.s[self.i] == ',':
                self.i += 1  # consume ','
                options |= self._parse_seq()
            # now expect '}'
            self.i += 1  # consume '}'
            return options
        else:
            # single lowercase letter
            ch = self.s[self.i]
            self.i += 1
            return {ch}