# 프로그래머스
# 힙(Heap)
# 더 맵게

import heapq

def solution(scoville: list, K: int) -> int:
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 0:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        hot = first + (second * 2)
        heapq.heappush(scoville, hot)
        count = count + 1
    return -1


if __name__ == '__main__':
    scoville = [1, 2, 3,]
    K = 4
    result = solution(scoville, K)
    print(result)
    # print(result == 2)
