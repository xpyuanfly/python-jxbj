import time

task = 100
scale = 10
start_time = time.time()

for i in range(1, 101):
    time.sleep(0.1)
    left = '*' * int((i / scale))
    right = '.' * int((task - i) / scale)
    ratio = (i/task) * 100
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'
          .format(ratio, left, right, time.time()-start_time), end='')
