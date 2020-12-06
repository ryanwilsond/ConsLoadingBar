import consloadingbar, time

time.sleep(0.05)
print()
clb = consloadingbar.Bar(title='ProgressBar 1', taskCount=10)

start = time.time()
for i in range(101):
    currentT = time.time() - start
    clb.progressBar(i, time_=currentT, tasksDone=i//10)
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar(title='ProgressBar 2', mainBarChar='#', endPointChars=['[', ']'])

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar(title='ProgressBar 3', mainBarChar='▣', emptyBarChar='▢')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar(title='ProgressBar 4', mainBarChar='◉', emptyBarChar='◯')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar(title='ProgressBar 5', emptyBarChar='●')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar()
clb.progressCircle(time_=2, title='ProgressCircle 1')

time.sleep(0.05)
print()
clb = consloadingbar.Bar(phases=['◷', '◶', '◵', '◴'])
clb.progressCircle(time_=2, title='ProgressCircle 2')

time.sleep(0.05)
print()
clb = consloadingbar.Bar(phases=['◑', '◒', '◐', '◓'])
clb.progressCircle(time_=2, title='ProgressCircle 3')

time.sleep(0.05)
print()
clb = consloadingbar.Bar(phases=['⎺', '⎻', '⎼', '⎽', '⎼', '⎻'])
clb.progressCircle(time_=2, title='ProgressCircle 4')

time.sleep(0.05)
print()
clb = consloadingbar.Bar()

for i in range(101):
    clb.progressCircle(char=i, title='ProgressCircle 5')
    time.sleep(0.02)

time.sleep(0.05)
print()
clb = consloadingbar.Bar()

num = 100
while num >= 0:
    clb.progressCircle(char=num, title='ProgressCircle 6')
    time.sleep(0.02)
    num = num - 1

time.sleep(0.05)
print()
clb = consloadingbar.Bar(phases=[' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'])

for i in range(9):
    clb.progressCircle(status=i, title='ProgressCircle 7')
    time.sleep(0.4)

time.sleep(0.05)
print()
clb = consloadingbar.Bar(phases=['○', '◔', '◑', '◕', '●'])

for i in range(5):
    clb.progressCircle(status=i, title='ProgressCircle 8')
    time.sleep(0.4)
