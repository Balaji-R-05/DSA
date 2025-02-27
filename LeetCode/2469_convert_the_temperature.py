from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 9/5) + 32
        return [kelvin, fahrenheit]
    
# Time complexity: O(1)
# Space complexity: O(1)

