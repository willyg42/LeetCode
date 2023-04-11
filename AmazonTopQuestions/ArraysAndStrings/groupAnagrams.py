from collections import defaultdict


def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagram_map[sorted_s].append(s)
    return list(anagram_map.values())


if __name__ == '__main__':
      assert(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == [["eat","tea","ate"],["tan","nat"],["bat"]]