"""
# 用途：时间计算
"""

import time

start = time.time()

print(f"time: {time.time()-start}")

for i in range(int(1e6)):
    continue

print(f"time: {time.time()-start}")

"""
# 输入示例
无
# 输出示例
time: 0.0
time: 0.014991998672485352
"""