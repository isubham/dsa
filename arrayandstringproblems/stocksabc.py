from typing import List

def maxProfit(self, prices: List[int]) -> int:
    """
    -
      -
        -
    """
    currentMinimum, currentMinimumIndex, currentMaximum, currentMaximumIndex = prices[0], 0, prices[0], 0

    for position, price in enumerate(prices):
        if position == 0:
            continue
        else:
            if price < currentMinimum:
                currentMinimum = price
                currentMinimumIndex = position
                # reset the currentMaxium
                currentMaximum = price
                currentMaximumIndex = position

            if price > currentMaximum:
                currentMaximum = price
                currentMaximum = position
    return currentMaximum - currentMinimum if currentMinimum < currentMaximum else 0



def test():
    print(maxProfit([7,1,5,3,6,4]) == 5)