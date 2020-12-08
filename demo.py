import consloadingbar, time

time.sleep(0.1)
print()
clb = consloadingbar.Bar(title='ProgressBar 1', taskCount=10, useColor=True)

for i in range(101):
    clb.progressBar(i, tasksDone=i//10)
    time.sleep(0.02)

time.sleep(0.1)
print()
clb = consloadingbar.Bar(title='ProgressBar 2', mainBarChar='#', endPointChars=['[', ']'])

start = time.time()
for i in range(101):
    percentageT = time.time() - start
    clb.progressBar(i, time_=percentageT)
    time.sleep(0.02)

time.sleep(0.1)
print()
clb = consloadingbar.Bar(title='ProgressBar 3', mainBarChar='▣', emptyBarChar='▢')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.1)
print()
clb = consloadingbar.Bar(title='ProgressBar 4', mainBarChar='◉', emptyBarChar='◯')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.1)
print()
clb = consloadingbar.Bar(title='ProgressBar 5', emptyBarChar='●')

for i in range(101):
    clb.progressBar(i)
    time.sleep(0.02)

time.sleep(0.1)
print()
clb = consloadingbar.Bar()
clb.counter(2, start=0, end=100, title='Counter 1')

time.sleep(0.1)
print()
clb.counter(2, start=100, end=0, title='Counter 2')

time.sleep(0.1)
print()
clb.spinner(time_=2, title='Spinner 1')

time.sleep(0.1)
print()
clb.spinner(time_=2, title='Spinner 2', phases=['◷', '◶', '◵', '◴'])

time.sleep(0.1)
print()
clb.spinner(time_=2, title='Spinner 3', phases=['◑', '◒', '◐', '◓'])

time.sleep(0.1)
print()
clb = consloadingbar.Bar()
clb.spinner(time_=2, title='Spinner 4', phases=['⎺', '⎻', '⎼', '⎽', '⎼', '⎻'])

time.sleep(0.1)
print()
clb.spinner(time_=4.7, title='Spinner 5', phases='preset')

time.sleep(0.1)
print()

for i in range(101):
    clb.progressChar(percentage=i, title='ProgressChar 1')
    time.sleep(0.01)

time.sleep(0.1)
print()

for i in range(101):
    clb.progressChar(percentage=i, title='ProgressChar 2', phases=['○', '◔', '◑', '◕', '●'])
    time.sleep(0.01)
