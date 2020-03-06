from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums, k):
        # nums_count = {}
        # for n in nums:
        #     if not nums_count.get(n):
        #         nums_count[n] = 1
        #     else:
        #         nums_count[n] += 1
        # for key in nums_count.keys():
        #     nums_count[key] = 1 / nums_count[key]
        # # 使用优先队列
        # q = PriorityQueue()
        # for key, value in nums_count.items():
        #     print(key, value)
        #     q.put((value, key))
        #
        # answer = [key for value, key in [q.get() for _ in range(k)]]
        # return answer

        # from collections import Counter
        # import heapq
        # counts = Counter(nums)
        # heap = [(value, key) for key, value in counts.items()]
        # return [key for value, key in heapq.nlargest(k, heap)]

        # import operator
        # freq = {}
        # for i in nums:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1
        # sorted_freq = dict(sorted(freq.items(), key=operator.itemgetter(1), reverse=True))
        # return list(sorted_freq.keys())[0:k]

        # from collections import Counter
        # cntr = Counter(nums)
        # x = sorted(set(nums), key=lambda x: -cntr[x])
        # return x[:k]

        # from collections import defaultdict
        # import heapq
        # result = []
        # my_dict = defaultdict(int)
        # for num in nums:
        #     my_dict[num] += 1
        # hp = [(-value, key) for key, value in my_dict.items()]
        # heapq.heapify(hp)
        # for i in range(k):
        #     ele = heapq.heappop(hp)
        #     result.append(ele[1])
        # return result

        # most pythonic
        # from collections import Counter as ct
        # return [el[0] for el in ct(nums).most_common(k)]

        import heapq
        from collections import Counter
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


class Solution2:
    def heap(self, i, h):
        if 2 * i <= self.n:
            if self.d[h[i]] < self.d[h[2 * i]]:
                a = h[i]
                h[i] = h[2 * i]
                h[2 * i] = a
                self.heap(2 * i, h)
        if 2 * i + 1 <= self.n:
            if self.d[h[i]] < self.d[h[2 * i + 1]]:
                a = h[i]
                h[i] = h[2 * i + 1]
                h[2 * i + 1] = a
                self.heap(2 * i + 1, h)
        return

    def delete(self, h):
        h[1] = h[self.n]
        self.n -= 1
        self.heap(1, h)
        return

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.d = {}
        for i in nums:
            if (i not in self.d):
                self.d[i] = 1
            else:
                self.d[i] += 1

        self.n = len(self.d)
        h = [0] * (self.n + 1)
        j = 1
        for i in self.d:
            h[j] = i
            j += 1

        i = int(self.n / 2)
        while (i >= 1):
            self.heap(i, h)
            i -= 1
        sol = []
        for i in range(1, k + 1):
            sol.append(h[1])
            self.delete(h)
        return sol

    # nums = [11, 22, -1, 11]


nums = [5, 3, 1, 1, 1, 3, 73, 1]
s = Solution()
print(s.topKFrequent(nums, 2))
