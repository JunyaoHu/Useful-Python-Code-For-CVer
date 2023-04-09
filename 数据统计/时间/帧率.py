"""
# 用途：帧率计算
"""

import time

frame_num = 20

start = time.time()

from tqdm import tqdm
for i in tqdm(range(10)):
    import random
    time.sleep(random.random())

print(f"fps (s): {frame_num/(time.time()-start):.4f}")

"""
# 输入示例
帧数10帧，每帧处理速度0-1秒之间。
# 输出示例
100%|██████████████████████████████████| 10/10 [00:05<00:00,  1.69it/s]
fps (f/s): 3.3401
"""