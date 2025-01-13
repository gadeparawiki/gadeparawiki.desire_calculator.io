import numpy as np
import re
from pyscript import document

# シミュレーション回数
iteration = 100

# 目標の女神の思いの個数
# URとUTRなどに分かれている場合は分けて指定。例：[150, 100]
target_desire_list = [60, 100, 100]

# 祈願1回あたりの獲得アイテムと確率
items = ['book1', 'stone', 'gold', 'book2', 'grace', 'desire', 'ticket']
probability = [0.24, 0.14, 0.14, 0.23, 0.08, 0.11, 0.06]

# 9%で2倍、2%で5倍と仮定
magnification = [1, 2, 5]
magnification_probability = [0.89, 0.09, 0.02]

# ランダムで倍率を返す関数
def choice_magnification():
  return np.random.choice(magnification, 1, p=magnification_probability)[0]

def calc_pray_count(event):
  # htmlからの入力処理
  input_text = document.querySelector("#required_desire")
  target_desire_list = [int(d) for d in re.split('[, ]', input_text.value) if d != '']
  print(target_desire_list)

  # 祈願カウンタ
  count = 0
  # 女神の思いカウンタ
  desire_count = 0

  for _ in range(iteration):
    for target_desire in target_desire_list:
      desire_count = 0
      while desire_count < target_desire:
        count+=1
        if count % 10 == 0:
          desire_count += 5 * choice_magnification()
        elif np.random.choice(items, 1, p=probability)[0] == 'desire':
          desire_count += 2 * choice_magnification()

  print(f'{count/iteration}回')
  output_div = document.querySelector("#output")
  output_div.innerText = f'実行結果：{count/iteration}回'
