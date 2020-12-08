# ConsLoadingBar Documentation

## Creator: FlameChain

### Maintainers: FlameChain

Github Link: [flamechain/Modules/](https://github.com/flamechain/ConsLoadingBar)

PyPi Link: [project/ConsLoadingBar](https://pypi.org/project/ConsLoadingBar)

![pypi](https://shields.io/pypi/v/consloadingbar.svg)

Description: A module to make easy progress bars with lots of customizability and a built-in demo class to show whats possible.

Backwards Compatible Since: 3.0.0

___

## 1.0 Contents

- [1.0 Contents](#10-contents)
- [2.0 New Changes](#20-new-changes)
- [3.0 ConsLoadingBar.Bar()](#30-consloadingbarbar)
  - [3.1 Parameters](#31-parameters)
  - [3.2 Description](#32-description)
  - [3.3 BarLength](#33-barlength)
  - [3.4 UseETACalculation](#34-useetacalculation)
  - [3.5 TaskCount](#35-taskcount)
  - [3.6 MainBarChar](#36-mainbarchar)
  - [3.7 ProgressPointBarChar](#37-progresspointbarchar)
  - [3.8 EndPointChars](#38-endpointchars)
  - [3.9 Title](#39-title)
  - [3.10 UseColor](#310-useColor)
  - [3.11 EmptyBarChar](#311-emptybarchar)
  - [3.12 MaxValue](#312-maxvalue)
  - [3.13 MaxValueLabel](#313-maxvaluelabel)
- [4.0 Using](#40-using)
  - [4.1 ProgressBar()](#41-progressbar)
  - [4.2 Start()](#42-start)
  - [4.3 End()](#43-end)
  - [4.4 Spinner()](#44-spinner)
  - [4.5 Counter()](#45-counter)
  - [4.6 ProgressChar()](#46-progresschar)
- [5.0 ConsLoadingBar.SimulateTasks()](#50-consloadingbarsimulatetasks)
  - [5.1 Parameters (SimulateTasks)](#51-parameters-simulatetasks)
  - [5.2 Example](#52-example)
- [6.0 Advanced Features](#60-advanced-features)
  - [6.1 lazyLoad](#61-lazyLoad)
  - [6.2 *args](#62-simulatetasks-args)
  - [6.3 **kwargs](#63-simulatetasks-kwargs)
  - [6.4 UseETACalculation](#64-useetacalculation)
- [7.0 Threading](#70-threading)
  - [7.1 Threading.Thread](#71-threadingthread)
  - [7.2 Concurrent.Futures](#72-concurrentfutures)
- [8.0 Generating Tasks](#80-generating-tasks)
  - [8.1 Pre-Loaded Tasks](#81-pre-loaded-tasks)
  - [8.2 Random Tasks](#82-random-tasks)
- [9.0 Known Issues](#90-known-issues)
- [10.0 Future Big Updates](#100-future-updates)
- [11.0 Version Log](#110-version-log)
  - [11.1 Modern Versions](#111-modern-versions)
  - [11.2 Early Stage Version](112-early-stage-versions)

___

## 2.0 New Changes

- 2.0.2 [Revised new README](./README.md)
- 2.0.1 [New README](./README.md)
- 2.0.0 Revised methods and added many features
- 1.3.1 [Major patch update](#90-known-issues)

> Notice: Please report any bugs directly to me and they will be acknowledged and added to this page. Add them to the issues page [here](https://github.com/flamechain/ConsLoadingBar/issues).

___

## 3.0 consloadingbar.Bar()

### 3.1 Parameters

| Param Name | Description | Type | Default |
|-|-|:-:|-|
| barLength | The __length, in characters__, that the bar progress bar expands. This only includes the moving part of the bar. | integer | 20
| useETACalculation | Used with the [SimulateTasks()](#50-consloadingbarsimulatetasks) class, and changes overall delay on the visual based on prior delay. Used when threading. | boolean | False |
| taskCount | The __total amount of tasks__ used. If not specified there will be not tasks indicator with the bar. | integer | None
| mainBarChar | Used for the moving bar. Often '#' is used. | string | '█'
| progressPointBarChar | Used for the front character of the bar. Often '>' is used. | string | '█'
| endPointChars | List with 2 indices, the front and last character of the bar. Often '[' and ']' is used. | list | ['&#124;', '&#124;']
| title | What the title is for the progress bar while running. | string | 'Running Tasks...' |
| useColor | If you want to have some color in on the bar. | boolean | False |
| emptyBarChar | Used for the other part of the bar that has not been reached. | string | ' ' |
| maxValue | Max value for progressBar() to reach. | float | 100 |
| maxValueLabel | Label or Unit for the max value. | string | '%' |

### 3.2 Description

This class takes advantage of the python '\r' or 'replace' ending to make a moving progress bar. Its called simply:

```python
import consloadingbar

lb = consloadingbar.Bar(args)
```

### 3.3 barLength

The length if the moving status bar indicator. In this example its set to 20 using the block character:

```txt
|████████████████████|
```

### 3.4 useETACalculation

When enabled this will estimate how long it will take, based on how long prior tasks took. Sometimes not accurate. Read more about using this [here](#64-useetacalculation).

### 3.5 taskCount

This is used just for the indicator on the bar to show how many tasks there are. There is no checking if the number of tasks is equal to this value. Both examples use a value of 5:

```txt
|                    |   0%  [tasks=0/5]
```

```txt
|████████████████████| 100%  [tasks=5/5]
```

The top example is before the tasks have started, and the bottom example is after its done. Unlike the eta box, it stays after the tasks are finished.

### 3.6 mainBarChar

This is simply the character used for the bar:

```txt
|████████████████████| 100%
```

```txt
|####################| 100%
```

The top example uses the default block character, and the bottom one used a pound.

### 3.7 progressPointBarChar

This is the head of the current bar status:

```txt
|██████████          |  50%
```

```txt
|#########>          |  50%
```

The top example is the default, and the bottom uses the greater than symbol. The bottom also uses the pound as the barChar because it looks better, and would most likely be used with that more often.

### 3.8 endPointChars

This is a list with the bounds of the bar. The default is the pipe, but with any other character for the bar, e.g. '#', square brackets are more commonly used:

```txt
[####################] 100%
```

### 3.9 title

Title for the progress bar while running. The default is 'Running Tasks...', but it could be anything.

```txt
Running Tasks...
        |██████████          |  50%
```

### 3.10 useColor

Boolian used if you want to have some color. Currently color param only applies to the base class, not the [SimulateTasks()](#50-consloadingbarsimulatetasks) class, hence an error message on [SimulateTasks()](#50-consloadingbarsimulatetasks) is always red. Default to off because its purely visual and personal preference. This color appears when the [end()](#43-end) method is called:

<pre>
<span style="color:green">Finished</span>
        |████████████████████| <span style="color:green">100%</span>
</pre>

And also when the lazyLoad progress bar is being updated, the knew progress is green until its to the right point.

### 3.11 emptyBarChar

The empty character for the bar:

Default:

```txt
|██████████          |  50%
```

Possible:

```txt
|◉◉◉◉◉◉◉◉◉◉◯◯◯◯◯◯◯◯◯◯|  50%
```

### 3.12 maxValue

Used for progressBar(), and it is the max value. Noramally 100, but it could be something else for a game bar or something like that.

```python
clb = consloadingbar.Bar(maxValue=50):
```

```txt
|████████████████████| 50%
```

### 3.13 maxValueLabel

Used well with maxValue:

```python
clb = consloadingbar.Bar(maxValue=20, maxValueLabel=' Health')
clb.progress(10)
```

```txt
|██████████          | 10 Health
```

___

## 4.0 Using

### 4.1 progressBar()

For this you can call the class like mentioned above, and then use the progress method to change the status of the bar. This is an example using only default values, and setting the status of the bar to 100%.

```python
import consloadingbar

clb = consloadingbar.Bar()
clb.progressBar(100)
```

```txt
|████████████████████| 100%
```

You can also add tasks to the bar by adding thath parameter to the [Bar()](#30-consloadingbarbar), and then telling the progress method how many tasks are done.

```python
clb = consloadingbar.Bar(taskCount=10)

for i in range(11):
    percent = i * 10
    clb.progressBar(percent, tasksDone=i)
```

In this example, every iteration the bar's completion goes up by 10%, and 1 task finishes. Here is the result of the bar after completion.

```txt
Finished
        |████████████████████| 100%  [tasks=10/10]
```

To use the eta, just specify how long its been since starting. The eta gets automatically calculated from there.

```python
import consloadingbar, time

clb = consloadingbar.Bar(taskCount=10)
startTime = time.time()

for i in range(11):
    percent = i * 10
    currentTime = time.time() - startTime

    clb.progressBar(percent, time_=currentTime, tasksDone=i)

    time.sleep(0.1)
```

In this example, we use the time module to calculate how many seconds have passed. Then we simple pass how much time has elapsed into the bar. This is what the bar would look like at iteration 6, just over half way. Notice how we also used time.sleep() to make it look more real.

```txt
|████████████        |  60%  [eta=00:04.36] [tasks=6/10]
```

You can also use ``returnString=True`` to get the output as a string instead of a print statement.

### 4.2 start()

This method is most similar to the [end()](#43-end) method. It shows an empty progress bar.

```txt
Running...
        |                    |   0%  [tasks=0/5]
```

### 4.3 end()

What this does is it just prints the consloadingbar with all values maxed out, and eta gone (if there was one).

```python
clb = consloadingbar.Bar(taskCount=5)

clb.end()
```

```txt
Finished
        |████████████████████| 100%  [tasks=5/5]
```

### 4.4 spinner()

This was made to replace the old start() method. This shows a title, and a spinning circle that either goes until stopped using threading, or stops after a specified time.

```python
clb.spinner(time_=2)
```

```txt
Loading /
```

This simple code example will run this spinning circle loading indicator for 2 seconds, then it stops itself. Read more on threading it externally [here](#72-concurrentfutures).

You can also use ``returnString=True`` to get the output as a string instead of a print statement.

### 4.5 counter()

This counts up or down. This example will go up to 100, then back down to 0:

```python
clb = consloadingbar.Bar()

clb.counter(2, start=0, end=100)
clb.counter(2, start=100, end=0)
```

### 4.6 progressChar()

Used like spinner(), but has sense of completion.

```python
for i in range(101):
    clb.progressChar(percentage=i, title='ProgressChar 1')
    time.sleep(0.01)
```

Percentage is the percentage complete.

___

## 5.0 consloadingbar.SimulateTasks()

### 5.1 Parameters (SimulateTasks)

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| eta | Changes overall delay on the visual. Not exact, only average. Based on seconds | True | 15 |
| barLength | The length, in characters, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20 |
| *args | Used if you want to add more params for a list of tasks. | True ||
| **kwargs | Used if you want to specify tasks without specfing other params. | True ||

All parameters have been explained above in the [Bar()](#30-consloadingbarbar) parameters section. These values go directly into that class.

### 5.2 Example

This has been shown above, but here are a couple examples of the output it could print.

Start

```txt
Loading Tasks /
```

Middle

```txt
Running Tasks...
        |███████████████     |  79%  [eta=00:07.07] [tasks=4/5]
```

End

```txt
Finshed
        |████████████████████| 100%  [tasks=5/5]
```

___

## 6.0 Advanced Features

### 6.1 lazyLoad

This is a parameter to the progress method. All of progress's methods will we listed here.

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| percentage | __Current percentage__ you want the bar to show. | False |
| time_ | How long has __elapsed since the start__ of the bar. Used for eta. | True | None |
| tasksDone | How many __tasks are complete__. Used for visualization | True | 0 |
| lazyLoad | Used for dynamic animation. | True | None |

lazyLoad is at the bottom because its hardest to use. Basically progress will return a value if this is not None, and then you put that value back into progress.

```python
past = 0
past = lb.progress(0, lazyLoad=past)

time.sleep(1)
past = lb.progress(50, lazyLoad=past)

time.sleep(1)
past = lb.progress(100, lazyLoad=past)
```

Each second it will jump up by 50 percent, but the bar will update each character with a tiny delay, so it appears to go up more slowly, instead of a sudden jump.

> Note: The [__progressBar()__](#41-progressbar) method only returns when __lazyLoad__ is specified, thats why the past variable needed to be defined first so it could be used for the first iteration. Likewise at the end, the past var is not doing anything, just a placeholder for the return value.

### 6.2 SimulateTasks() *args

This is a parameter in the [SimulateTasks()](#50-consloadingbarsimulatetasks) class that lets you put in custom test-cases. Here is an example of how its used:

> Note: The first 2 values aren't tasks, just there so *args gets properly evaluated.

```python
lb.SimulateTasks(15, 20, 50, 20, 30)
```

In this example there are 3 custom tasks. The first one takes 50%, the next takes 20%, and the last takes the final 30%. If these values are greater than the total, then an error will be raised.

```python
lb.SimulateTasks(15, 20, 50, 50, 10)
```

```txt
Value Error: Your custom tasks exceded the total (150 > 100)
```

If these values are less than, it will prompt a warning for 2 seconds, and then contiue the program as normal.

<pre>
<span style="color:red">Warning: Your custom tasks did not reach the total (50 < 100)
The Program will continue but there may be errors.</span>
</pre>

### 6.3 SimulateTasks() **kwargs

This is used for the same reason as [*args](#62-simulatetasks-args), but if you would rather specify before other params. This only works if you use the correct keyword, args:

```python
consloadingbar.SimulateTasks(args=[50, 30, 20])
```

This example would create a custom task list with 50%, 30%, and 20%. You can still use *args like normal.

### 6.4 useETACalculation

This is enabled when threading with real tasks. It uses prior data to estimate how long the rest will take. Not always accurate. This is by default turned off, but is turned on in [SimulateTasks()](#50-consloadingbarsimulatetasks). It just enables this code in the main class:

```python
time.sleep((float(eta) / (100-percentage)))
```

___

## 7.0 Threading

This section will mainly just go over how the [SimulateTasks()](#50-consloadingbarsimulatetasks) class worked. You can always look at the code yourself [here](./consloadingbar.py).

> Note: The [SimulateTasks()](#50-consloadingbarsimulatetasks) class is an example class without strict formatting, so it may be more difficult to read.

### 7.1 threading.Thread

In the [SimulateTasks()](#50-consloadingbarsimulatetasks) class it uses the threading and concurrent modules. This section will go over just where it used the threading module to make it apear like its estimating eta without know how long the tasks will take.

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

> Note: The 15 comes from the default estimatedTotalTime parameter for the [SimulateTasks()](#50-consloadingbarsimulatetasks) class.

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

### 7.2 concurrent.futures

This is used only in 1 area as well to simply get a return value from a function, where the threading module has no easy way to do that. This is just to run a 'loading' popup while the tasks are being generated. Most of the delay is artifical.

```python
stop_threads = False
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(loadtasks)

    if self.estimatedTotalTime > 5:
        future2 = executor.submit(lb.progressCircle, lambda: stop_threads)

    tasks = future.result()
    stop_threads = True
```

This uses the same technique to have the function stop itself. Next we will look at the function that actaully makes the random tasks. Notice how the [progressCircle()](#44-progresscircle) method is being used. This is the second way it can be used, the first explained [here](#44-progresscircle).

## 8.0 Generating Tasks

### 8.1 Pre-Loaded Tasks

If you use the optional *args parameter, you can classify your own tasks. See [here](#62-simulatetasks-args). You can also use **kwargs instead. See [here](#63-simulatetasks-kwargs).

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
            future = executor.submit(lb.progressCircle, lambda: stop_threads)
            time.sleep(1)
            stop_threads = True
```

If you go over the total, then it stops the program. If the custom tasks go below, it prompts an error but continues. You can read a little more on this [here](#62-simulatetasks-args).

### 8.2 Random Tasks

> Note: This is all part of the [SimulateTasks()](#50-consloadingbarsimulatetasks) example class to show whats possible with this module, and to prove that this module can be used in real world application.

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

___

## 9.0 Known Issues

> Note: This bug log only contains bugs going back to version 1.1.6

| Version | Bug ID | Description | Status | Fix Date |
|-|-|-|:-:|:-:|
| 2.0.1 | 015 | ProgressCircle() printed raw string, not formatted | Fixed | 12/06/20 |
| 1.3.0 | 014 | Title doesn't have 1 space padding | Fixed | 12/04/20 |
| 1.3.0 | 013 | Only 1 block character is in allowedChars | Fixed | 12/04/20 |
| 1.3.0 | 012 | TaskCount isn't converted to int or positive | Fixed | 12/04/20 |
| 1.3.0 | 011 | If *args is specified as list, gives TypeError | Fixed | 12/04/20 |
| 1.3.0 | 010 | 0 barLength has a length of 1 not 0 | Fixed | 12/04/20 |
| 1.3.0 | 009 | Ints are checked if positive or not | Fixed | 12/04/20 |
| 1.3.0 | 008 | If invalid param, program runs anyway and gives AttributeError | Fixed | 12/04/20 |
| 1.3.0 | 007 | ProgressCircle() doesn't print when not threaded | Fixed | 12/04/20 |
| 1.3.0 | 006 | Title for progressBar isn't sanitized | Fixed | 12/04/20 |
| 1.2.7 | 004 | PiP not finding package, has bad files | Fixed | 12/03/20 |
| 1.2.2 | 004 | SimulateTasks() runs when using import | Fixed | 12/02/20 |
| 1.2.0 | 003 | lazyLoad sometimes has random prints. | Fixed | 12/03/20 |
| 1.1.8 | 002 | lazyLoad would freeze program | Fixed | 12/02/20 |
| 1.1.6 | 001 | time_ param in progress() method froze program if over 100 | Fixed | 12/01/20 |

___

## 10.0 Future Updates

> Note: These release dates aren't offical and are only estimations

| Version | Planned Changes |
|-|:-:|
| 3.0.0 | Ability to have multiple threads run at the same time internally, and externally |

___

## 11.0 Version Log

### 11.1 Modern Versions

| Version | New Changes | Release Date |
|-|-|:-:|
| 3.0.0 | Changed naming for the last time (hopefully) and added 2 new methods, and changed progressCircle to [spinner()](#44-spinner)
| 2.0.5 | Fixed bug | 12/07/20 |
| 2.0.4 | Added returnString param to [progressBar()](#41-progressbar) and [progressCircle()](#44-spinner) to return string instead of print | 12/06/20 |
| 2.0.3 | Unstable | 12/06/20 |
| 2.0.2 | Changed README and fixed bug | 12/06/20 |
| 2.0.1 | Added links to README, removed old section | 12/06/20 |
| 2.0.0 | Added new params and customability! Also moved major documentation into speperate docs, and replaced README with a gif and quick start guide, and changed version numbering system | 12/06/20 |
| 1.3.1 | Major patch update. [Fixed many bugs](#90-known-issues) | 12/03/20 |
| 1.3.0 | Final version of [progressCircle()](#44-spinner) method | 12/03/20 |
| 1.2.9 | [SimulateTasks()](#50-consloadingbarsimulatetasks) would run when initilizing Bar() | 12/03/20 |
| 1.2.8 | Bug fixes | 12/03/20 |
| 1.2.7 | Replaced [start()](#42-start) method with [progressCircle()](#44-spinner) to allow for more customization, [start()](#42-start) method is now like the [end()](#43-end) method for the beginning; Also added more title customization including placement | 12/03/20 |
| 1.2.6 | Added email and website to [pypi page](https://pypi.org/project/ConsLoadingBar) | 12/03/20 |
| 1.2.5 | Setup tokens so updates are easier and more frequent | 12/02/20 |
| 1.2.4 | Tweaks to documentation for more clarity | 12/02/20 |
| 1.2.3 | Converted module to offical PyPi / PiP package | 12/02/20 |
| 1.2.2 | Minor tweaks to eta calculation, fixed documentation mistakes | 12/02/20 |
| 1.2.1 | Added Quick Start Guide to documentation, revised doc-strings in consloadingbar.py | 12/02/20 |
| 1.2.0 | Changed all param names to be more clear, and removed some useless ones. Overall easier to use. | 12/02/20 |
| 1.1.9 | Added colors to [end()](#43-end) method, and [lazyLoad](#61-lazyLoad). Added color param to [Bar()](#30-consloadingbarbar) class so the user has the ability to toggle color mode. | 12/02/20 |
| 1.1.8 | [SimulateTasks()](#50-consloadingbarsimulatetasks) has an *args param to accept custom pre-set tasks. Updated all doc-strings and added technical comments. | 12/01/20 |
| 1.1.7 | [SimulateTasks()](#50-consloadingbarsimulatetasks) no longer has nested functions, and doesn't have its own redundent [start()](#42-start) method. Also added title param to all methods so printing the title is built in. | 12/01/20 |
| 1.1.6 | Created [Bug Log](#90-known-issues) | 12/01/20 |
| 1.1.5 | Created [Version Log](#110-version-Log) | 12/01/20 |
| 1.1.4 | Bug fixes | 12/01/20 |
| 1.1.3 | Released Documentation 1.0 | 11/30/20 |
| 1.1.2 | Bug fixes | 11/30/20 |
| 1.1.1 | Bug fixes | 11/30/20 |
| 1.1.0 | Added [SimulateTasks()](#50-consloadingbarsimulatetasks) class to main module | 11/29/20 |
| 1.0.2 | Bug fixes | 11/29/20 |
| 1.0.1 | Converted [SimulateTasks()](#50-consloadingbarsimulatetasks) to class form | 11/28/20 |
| 1.0.0 | Inital Release | 11/27/20 |

### 11.2 Early Stage Versions

| Stage | Version ID | New Changes | Release Date |
|:-:|-|-|:-:|
| beta | 3.0 | Threading with eta estimation | 11/27/20 |
| beta | 2.0 | Tasks visual and ability to detect them | 11/26/20
| beta | 1.3 | Various big fixes | 11/26/20
| beta | 1.2 | Loading bar now has eta display | 11/26/20 |
| beta | 1.1 | Loading bar with percent of completion | 11/25/20 |
| beta | 1.0 | Dynamic loading bar | 11/25/20 |
| alpha | 1.2 | Eta calculator | 11/25/20 |
| alpha | 1.1 | Class form | 11/25/20 |
| alpha | 1.0 | First version, only progress method as single function | 11/24/20 |
