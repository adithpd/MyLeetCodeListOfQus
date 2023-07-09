class Solution:
  def groupAnagrams(self, strs):
    from collections import defaultdict
    dict = defaultdict(list)

    for str in strs:
      key = ''.join(sorted(str))
      dict[key].append(str)

    return dict.values()