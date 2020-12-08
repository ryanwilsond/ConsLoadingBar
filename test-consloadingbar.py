import consloadingbar, time, concurrent.futures

success = 0
error = 0

try:
    clb = consloadingbar.Bar(title='test')
    assert clb.progressBar(0) == print('test |                    |   0%')
    success += 1
except: error += 1

try:
    clb = consloadingbar.Bar(mainBarChar='▓', title='test')
    assert clb.progressBar(1) == print('test |▓                   |   0%')
    success += 1
except: error += 1

try:
    clb = consloadingbar.Bar(taskCount=-1.1)
    error += 1
except ValueError: success += 1

try:
    assert clb.spinner(time_=0) == print('Loading |')
    success += 1
except: error += 1

try:
    clb = consloadingbar.SimulateTasks(0, args=[50, 50])
    success += 1
except: error += 1

try:
    clb = consloadingbar.Bar(title='test\033[F')
    error += 1
except: success += 1

try:
    clb = consloadingbar.Bar()
    for i in range(101):
        clb.progressChar(i)
    assert clb.progressChar(100) == print('Loading █')
    success += 1
except: error += 1

try:
    clb = consloadingbar.Bar()
    clb.counter(0.01, 0, 100)
    print()
    clb.counter(0.01, 100, 0)
    assert clb.counter(0.01, 100, 100) == print('Loading 100')
    success += 1
except: error += 1

print(f"{success, error}")
