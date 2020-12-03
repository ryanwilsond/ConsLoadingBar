# 2 ConsLoadingBar Documentation

## Creator: FlameChain

Github Link: [flamechain/Modules/](https://github.com/flamechain/Modules)

### Version: 1.2.2

Description: Extra documentation with larger and more specific examples. This mainly goes over how the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) method words, and how you can make it from scratch.

___

## 2.1 Contents

> Note: Links to README file link to ./README.md so if your not on the github version, take this [link](https://github.com/flamechain/Modules/).

- [1.0 Main Documentation](./README.md) |
- [2.0 Secondary Documentation](#2-consloadingbar-documentation)
- [2.1 Contents](#21-contents)
- [2.2 Threading](#22-threading)
  - [2.2.1 threading.Thread](#221-threadingthread)
  - [2.2.2 concurrent.futures](#222-concurrentfutures)
- [2.3 Generating Tasks](#23-generating-tasks)
  - [2.3.1 Pre-Loaded Tasks](#231-pre-loaded-tasks)
  - [2.3.2 Random Tasks](#232-random-tasks)
- [2.4 Print Statements](#24-print-statements)
- [2.5 Start() Method](#25-start)
- [2.6 End() Method](#26-end)

___

## 2.2 Threading

This section will mainly just go over how the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) class worked. You can always look at the code yourself [here](./consloadingbar.py).

> Note: The [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) class is an example class without strict formatting, so it may be more difficult to read.

### 2.2.1 threading.Thread

In the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) class it uses the threading and concurrent modules. This section will go over just where it used the threading module to make it apear like its estimating eta without know how long the tasks will take.

```python
def runprogress(perc, done, stop):
    i = perc
    while True:
        if stop():
            break
        if i > 99:
            i = random.randint(75, 90)

        total_time = time.time() - start_time
        lb.progress(i, total_time, done)
        i += 1
```

First we make a function that just goes up by 1 percent every iteration. The base speed is initilized like so:

```python
start_time = time.time()
totaltime = time.time() - start_time

lb.progress(total, totaltime)
time.sleep(0.005*self.estimatedTotalTime)
lb.progress(total+1, totaltime)
```

This code puts a 0.005*15 delay, or 0.075 second delay between 1 percent, telling the progress method that on average it should go up 13% per second. This was found to be a good baseline.

> Note: The 15 comes from the default eta parameter for the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) class.

The actaully threading comes in here. It runs the runprogress() method as 1 thread, and sleeps on the other, or the 'main' thread.

```python
for i in range(len(tasks)):
    if i == 0:
        total = 1
    else:
        total += tasks[i-1]

    stop_threads = False
    t = threading.Thread(target=runprogress, args=(total, i, lambda: stop_threads))
    t.start()
    time.sleep(random.randint(1, 5)*(self.estimatedTotalTime/10))
    stop_threads = True
    t.join()
```

What this does is it creates a loop that will go through every fake task (sleeping). It will start the progress bar, and reset it to the task finished percent when the task is done. After 1 or 2 tasks the progress bar does the math to find the overall average, and sets a good pace. In addition, if the progress bar ever gets to 100% before the tasks are finished, it resets to an average of 83%

### 2.2.2 concurrent.futures

This is used only in 1 area as well to simply get a return value from a function, where the threading module has no easy way to do that. This is just to run a 'loading tasks' popup while the tasks are being generated. Most of the delay is artifical.

```python
stop_threads = False
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(loadtasks)

    if self.estimatedTotalTime > 5:
        future2 = executor.submit(start, lambda: stop_threads)

    tasks = future.result()
    stop_threads = True
```

This uses the same technique to have the function stop itself. Next we will look at the function that actaully makes the random tasks.

## 2.3 Generating Tasks

### 2.3.1 Pre-Loaded Tasks

If you use the optional *args parameter, you can classify your own tasks. See [here](./README.md#182-simulatetasks-args).

If you do use this option, there is custom error-handling to make sure nothing brakes. In this example 'self.tasks' was pre-specified in the initializer to equal a list of *args. That is why it checks to see if the list is empty.

```python
if len(self.tasks) > 0:

    tasks = self.tasks
    total_ = 0

    for i in tasks:
        total_ += i

    if self.total < total_:
        return print('Value Error: Your custom tasks exceded the total (%s > %s)' % (total_, self.total))

    elif self.total > total_:

        print(termcolor.colored(f'Warning: Your custom tasks did not reach the total ({total_} < {self.total})', 'red'))

        print(termcolor.colored('The Program will continue but there may be errors.', 'red'), end='\n\n')

        time.sleep(2)
        stop_threads = False
        lb = Bar(self.barLength, self.estimatedTotalTime)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(lb.start, lambda: stop_threads)
            time.sleep(1)
            stop_threads = True
```

If you go over the total, then it stops the program. If the custom tasks go below, it prompts an error but continues. You can read a little more on this [here](./README.md#182-simulatetasks-args).

### 2.3.2 Random Tasks

> Note: This is all part of the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) example class to show whats possible with this module, and to prove that this module can be used in real world application.

Heres a list in order of what the the method loadtasks() is doing.

1. Chooses how many tasks there should be, anywhere between 2 and 5
1. Creates those tasks that take up a random percent of the total, anywhere bewteen 20 and 60 percent
1. Loops through and slowly ticks down each task after all are created to make sure they sum up to 100
1. Appends each percent that each task takes to a list, and returns that list.

This is why the code example above has:

```python
future = executor.submit(loadtasks)
tasks = future.result()
```

Now lets go over each step and how its implemented.

- Choose how many tasks there should be

```python
ntasks = random.randint(2, 5)
```

- Creates those tasks that take up a random percent of the total

> Note: Total param has been removed, so its hardcoded to 100. PercChar has also been removed and hardcoded to '%'.

```python
totalperc = self.total

for i in range(ntasks):
    if ntasks == 1:
        j = 100
    else:
        j = random.randint(2, 6) * 10
        j *= (random.randint(95, 105) / 100)

    totalperc -= j
```

- Loops through and slowly ticks down each tasks after all are created to make sure they sum up to 100

This part also rounds each percent to an integer, because the progress bar doesn't support floats (yet).

```python
while totalperc < 0:
    j -= 1
    totalperc += 1
    for ii in range(len(tasks)):
        if tasks[ii] < 5:
            continue
        else:
            tasks[ii] = tasks[ii] - 1
            totalperc += 1

if i == ntasks-1:
    if totalperc != 0:
        tasks[-1] += totalperc

j = round(j, 1)
tasks.append(j)
```

- Appends each percent that each task takes to a list, and returns that list

This part in the code also has some artifical delay to make the 'loading tasks' indicator show up for more than 0.001 seconds. This is not required so its not shown in this example.

```python
tasks = []

for i in range(len(tasks)):
    tasks[i] = round(tasks[i], 1)

return tasks
```

## 2.4 Print Statements

The only other thing in the [SimulateTasks()](./README.md#17-consloadingbarsimulatetasks) class that wasn't included was the print statements. It starts by using the [start()](#25-start) method. The reason this is a method is because the '/' character next to the 'Loading Tasks' rotates in a circle. The code for this can be seen [here](#25-start).

```txt
Loading Tasks /
```

```txt
Running Tasks...
        |███████████████     |  79%  [eta=00:07.07] [tasks=4/5]
```

The end just calls the [end()](#26-end) method, which as explained in the main documentation, is just a progress bar with all values maxed out.

```txt
Finshed
        |████████████████████| 100%  [tasks=5/5]
```

## 2.5 start()

This start method is very simple, and is coded like this:

```python
def start(self, stop=False, title='Loading Tasks'):
    percsyms = ['|', '/', '-', '\\']

    j = 0
    while True:
        if stop():
            break

        print('%s %s' % (title, percsyms[j]), end='\r')

        j += 1
        if j == 4:
            j = 1

        time.sleep(0.2)

    print(self.title)
```

Notice that this requires to be stopped by an outside peice of code, so this is not a one-off method that you can just run, un-like [end()](#26-end).

## 2.6 end()

This method is simply called like this:

```python
lb.end()
```

The code for this method is here:

```python
def end(self, taskCount=None, title='Finished'):
    bar  = self.mainBarChar * self.barLength

    if taskCount == None:
        taskCount = self.taskCount

    print("\033[F" + termcolor.colored(title, self.green) + "\t\t\t\t\t\t\t\t")

    if taskCount == None:
        print(f'\t{self.endPointChars[0]}{bar}{self.endPointChars[1]}', end='')
        print(termcolor.colored(' 100%%' + self.green))
    else:
        print(f'\t{self.endPointChars[0]}{bar}{self.endPointChars[1]}', end='')
        print(termcolor.colored(' 100%%' + f'  [tasks={taskCount}/{taskCount}]', self.green))
```

This method has the color integration as mentioned [here](./README.md#1510-usecolor).

> Note: All code examples here don't have comments to save space. If you want to view the full code, click [here](https://github.com/flamechain/Modules/blob/main/consloadingbar.py).

___

<sub>Documentation Version 2.6 - Module Version 1.2.2 - Release 8</sub>
