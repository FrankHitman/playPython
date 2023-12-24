class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        gas_length = len(gas)
        remain_gas = 0
        for i in range(gas_length):
            remain_gas = remain_gas + gas[i] - cost[i]
        if remain_gas < 0:
            return -1
        start_index = 0
        while start_index < gas_length:
            if gas[start_index] >= cost[start_index] and gas[start_index] > 0:
                index = start_index
                current_gas = 0
                while (index - start_index) <= gas_length:
                    if gas[index % gas_length] + current_gas < cost[index % gas_length]:
                        # inspired by https://leetcode.com/problems/gas-station/description/comments/1745609
                        # Hint: if you start from station a and stuck at b, then you can't get to b from any station between a and b.
                        start_index = index
                        break
                    else:
                        current_gas += gas[index % gas_length] - cost[index % gas_length]
                        index += 1

                if index - start_index >= gas_length:
                    return start_index
            start_index += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(sol.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    print(sol.canCompleteCircuit(gas=[0, 0, 0, 2], cost=[0, 0, 1, 0]))

# topic is from https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150
# idea is inspired from https://leetcode.com/problems/gas-station/description/comments/1745609
# output
# 3
# -1
# 3