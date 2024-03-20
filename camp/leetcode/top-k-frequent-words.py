class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res =[]
        count = Counter(words)
        bucket =defaultdict(list)

        mxf =1
        for key, val in count.items():
            mxf =max(mxf, val)
            bucket[val].append(key)
        print(bucket)

        for ky in range(mxf, 0, -1):
            bucket[ky].sort()
            res.extend(bucket[ky])

            if len(res) >= k:
                return res[:k]
            