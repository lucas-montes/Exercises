from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for pos_an in strs:
            sor_pos_an = "".join(sorted(pos_an))
            if sor_pos_an in seen:
                seen[sor_pos_an].append(pos_an)
            else:
                seen[sor_pos_an] = [pos_an]

        return list(seen.values())
