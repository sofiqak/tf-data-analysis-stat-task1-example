import pandas as pd
import numpy as np


chat_id = 917079889 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    sum_x = np.sum(x)
    L = (1/n * sum_x)/70
    return L # Ваш ответ
