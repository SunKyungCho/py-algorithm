

#
# https://leetcode.com/problems/richest-customer-wealth/
#

def maximumWealth(accounts):
    maximum = -1
    for account in accounts:
        maximum = max(sum(account), maximum)
    return maximum


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    result = maximumWealth(accounts)
    print(result == 6)