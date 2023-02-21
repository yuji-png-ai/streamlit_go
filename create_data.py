import pandas as pd
import numpy as np

# データを生成
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.cos(x)

# Pandasのデータフレームに変換
data = pd.DataFrame({'x': x, 'y': y})

# CSVファイルとして保存
data.to_csv('data.csv', index=False)
