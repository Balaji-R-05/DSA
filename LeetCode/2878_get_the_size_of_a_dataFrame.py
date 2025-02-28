# 2878. Get the Size of a DataFrame

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# Time complexity: O(1)
# Space complexity: O(1)