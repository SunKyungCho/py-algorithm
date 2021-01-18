def solution(nums: list, target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums_map.get(num), nums_map[target - num]


if __name__ == '__main__':
    nums = [2, 5, 5, 11]
    target = 10
    print(solution(nums, target))
