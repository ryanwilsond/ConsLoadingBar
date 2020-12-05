# v1.3.1
import time, random, concurrent.futures, threading, termcolor, sys

class Bar:
    def __init__(self, barLength=20, useETACalculation=False, taskCount=None, mainBarChar='█', progressPointBarChar='█', endPointChars=['|', '|'], title='Running Tasks...\n', useColor=False):
        '''
        ### Description

        Loading/Progress bar for general use. Use SimulateTasks() to see this used in a way possible.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | barLength | True | Length of bar in characters. |
        | useETACalculation | True | Boolean if you want the program to automatically sleep. |
        | taskCount | True | Amount of tasks to get done, just for visualization. |
        | mainBarChar | True | The character that the bar is made of. Default = █, but # is also common. |
        | progressPointBarChar | True | Head of the bar, usally same as barChar or >. |
        | endPointChars | True | List with start bar and end bar bracket. [] is common, || is default. |
        | title | True | Title that shows up for the progress bar. Actaully gets prinited using the start() method. |
        | useColor | True | Color mode on or off, default to off. |

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        error = ValueError(termcolor.colored('Check params and try again', 'red'))
        okChars = ['|', ' ', '[', ']', '█', '▓', '▒', '░', '║', '#', '$', '^', '&', '*', '(', ')', '-', '+', '=',' !', '@', '{', '}', '/', '`', '~', '0', '.']
        otherChars = ['\n', '\t']
        try:
            if useColor:
                self.green = 'green'
                self.red = 'red'
            else:
                self.green = 'white'
                self.red = 'white'

            self.barLength = int(barLength)
            if self.barLength < 0:
                raise error
            if taskCount != None:
                self.taskCount = int(taskCount)
                if self.taskCount < 0:
                    raise error
            else:
                self.taskCount = taskCount
            for letter in title:
                if (letter.isalnum()) | (letter in okChars) | (letter in otherChars):
                    pass
                else:
                    raise error
            self.title = title
            self.total = 100
            self.percChar = '%'
            self.useETACalculation = bool(useETACalculation)

        except:
            raise error

        if mainBarChar in okChars:
            self.mainBarChar = mainBarChar
        else:
            raise error
        if progressPointBarChar in okChars:
            self.progressPointBarChar = progressPointBarChar
        else:
            raise error
        if (endPointChars[0] in okChars) & (endPointChars[1] in okChars):
            self.endPointChars = endPointChars
        else:
            raise error

    def start(self):
        '''
        ### Description

        Shows bar with 0% completion.

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        if '\n' in self.title:
            print(self.title, end='')
            title = '\t'
        else:
            title = self.title + ' '

        if self.taskCount == None:
            print('%s%s%s%s   0%%' % (title, self.endPointChars[0], ' ' * self.barLength, self.endPointChars[1]), end='\r')
        else:
            print('%s%s%s%s   0%%  [tasks=0/%s]' % (title, self.endPointChars[0], ' ' * self.barLength, self.endPointChars[1], self.taskCount), end='\r')

    def progressBar(self, current, time_=None, tasksDone=0, pastBar=None):
        '''
        ### Description

        The loading bar itself. Doesn't iterate itself.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | current | False | Current percentage that the bar has completed. |
        | time_ | True | How long its taken so far. Used for calculating eta. |
        | tasksDone | True | Amount of tasks done, just for visualization. |
        | pastBar | True | Used if you don't have threading, but want a nice animation to get to current percent. |

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        # Generates Bar Format
        percent = float(current) * 100 / self.total
        bar = self.mainBarChar * int(percent/100 * self.barLength - 1)
        if len(bar) != 0:
            bar = bar + self.progressPointBarChar
        spaces  = ' ' * (self.barLength - len(bar))
        space = ' ' * (5 - len(str(percent)))

        # Creates an eta (if possible)
        try:
            eta = str(round((time_ * (100/current)) - time_, 2))
            eta, et2 = eta.split('.')
            et3 = '00'

            while int(eta) > 59:
                eta = str(int(eta) - 60)
                et3 = str(int(et3) + 1)

            if len(et2) == 1:
                et2 = et2 + '0'
            if len(eta) == 1:
                eta = '0' + eta
            if len(et3) == 1:
                et3 = '0' + et3

            eta = ':'.join([str(et3), str(eta)])
            eta = '.'.join([str(eta), str(et2)])

        except:
            eta = '00:00.00'

        useTitle = False
        if '\n' not in self.title:
            useTitle = True
            title = self.title
        else:
            title = '\t'
        # pastBar fork
        if pastBar != None:
            temp1 = 1
            temp2 = pastBar
            string_ = None
            while len(bar) > pastBar:
                string_ = '%s %s%s%s%s%s %s%d%s  [eta=%s] [tasks=%s/%s]' % (title, self.endPointChars[0], self.mainBarChar * temp2, termcolor.colored(self.mainBarChar * temp1, self.green),
                (spaces + (" " * (len(bar)-pastBar-1))), self.endPointChars[1], space, percent, self.percChar, eta, tasksDone, self.taskCount)
                print(string_, end='\r')
                pastBar += 1
                temp1 += 1
                time.sleep(0.05)

            if string_ != None:
                string_ = string_.replace(self.mainBarChar, termcolor.colored(self.mainBarChar, 'white'))
                print(string_, end='\r')
            return len(bar)

        # Prints all values it has
        else:
            if (time_ == None) & (self.taskCount == None):
                print('%s %s%s%s%s %s%d%s' % (title, self.endPointChars[0], bar, spaces, self.endPointChars[1], space, percent, self.percChar), end='\r')
            elif (time_ == None) & (self.taskCount != None):
                print('%s %s%s%s%s %s%d%s  [tasks=%s/%s]' % (title, self.endPointChars[0], bar, spaces, self.endPointChars[1], space, percent, self.percChar, tasksDone, self.taskCount), end='\r')
            elif (time != None) & (self.taskCount == None):
                print('%s %s%s%s%s %s%d%s  [eta=%s]' % (title, self.endPointChars[0], bar, spaces, self.endPointChars[1], space, percent, self.percChar, eta), end='\r')
            elif (time != None) & (self.taskCount != None):
                print('%s %s%s%s%s %s%d%s  [eta=%s] [tasks=%s/%s]' % (title, self.endPointChars[0], bar, spaces, self.endPointChars[1], space, percent, self.percChar, eta, tasksDone, self.taskCount), end='\r')
            eta_, eta2_ = eta.split(':')

            while int(eta_) != 0:
                eta_ = int(eta_) - 1
                eta2_ = float(eta2_) + 60

            if self.useETACalculation: # Used if enabled
                if (eta2_ == 0) | (self.total-current == 0):
                    time.sleep(0.01)
                else:
                    time.sleep((float(eta2_)/(self.total-current)))
    
    def progressCircle(self, stop=False, time_=None, title='Loading'):
        '''
        ### Description

        Shows a rotating circle progress thing.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | time_ | True | If used runs until time runs out. |
        | title | True | Prints what the bar should print |
        | stop | True | Used with threading rather than waiting time. |

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        percsyms = ['|', '/', '-', '\\']

        def func(stop=False):  
            j = 0
            while True:
                if stop():
                    break

                print('%s %s' % (title, percsyms[j]), end='\r')

                j += 1
                if j == 4:
                    j = 1

                time.sleep(0.2)

        if time_ == None:
            j = 0
            while True:
                if stop():
                    break

                print('%s %s' % (title, percsyms[j]), end='\r')

                j += 1
                if j == 4:
                    j = 1

                time.sleep(0.2)

        else:
            stop_threads = False
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(func, lambda: stop_threads)
                time.sleep(time_)
                stop_threads = True

    def end(self, tasks=None, title='Finished\n'):
        '''
        ### Description

        Shows full bar complete, and removes eta and shows all tasks complete (if any).

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | tasks | True | Optional param if you want to use external tasks. |
        | title | True | Title that prints when the progress bar is done. |

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        bar  = self.mainBarChar * self.barLength

        if tasks == None:
            total_tasks = self.taskCount
        else:
            total_tasks = tasks
        
        if '\n' in self.title:
            title = title.split('\n')
            title = ''.join(title)
            print("\033[F" + termcolor.colored(title, self.green), end='\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\r')
        else:
            print(termcolor.colored(title, self.green), end='')

        # Puts in all values at max
        temp = ' '
        if '\n' in self.title:
            temp = '\t'
        if total_tasks == None:
            print(f'{temp}{self.endPointChars[0]}{bar}{self.endPointChars[1]}', end='')
            print(termcolor.colored(' 100' + self.percChar, self.green) + '\t\t')
        else:
            print(f'{temp}{self.endPointChars[0]}{bar}{self.endPointChars[1]}', end='')
            print(termcolor.colored(' 100' + self.percChar + f'  [tasks={total_tasks}/{total_tasks}]', self.green) + '\t\t')

class SimulateTasks:
    def __init__(self, estimatedTotalTime=15, barLength=20, *args, **kwargs):
        '''
        ### Description

        Custom use of Bar() class

        ### Params
        
        | Name | Optional | Description |
        |-|:-:|-|
        | estimatedTotalTime | True | Bar() eta param, used for average time. |
        | barLength | True | Length of the bar in characters. |
        | *args | True | If you want to use external task values for unit testing. |
        | **kwargs | True | Used if you want to specify a list like args=[] |

        PyPi Link: https://pypi.org/project/ConsLoadingBar

        Github Link: https://github.com/flamechain/ConsLoadingBar
        '''
        self.barLength = barLength
        self.estimatedTotalTime = estimatedTotalTime
        self.total = 100
        self.tasks = args
        if kwargs:
            self.tasks = kwargs['args']
        self.simulateTasks()

    def simulateTasks(self):
        # Checks if pre-loaded tasks (*args) and then generates tasks if not
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
                lb = Bar(self.barLength)
                lb.progressCircle(time_=2)
        else:
            stop_threads = False
            lb = Bar(self.barLength)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.loadtasks)
                if self.estimatedTotalTime > 5:
                    future2 = executor.submit(lb.progressCircle, lambda: stop_threads)
                tasks = future.result()
                stop_threads = True

        start_time = time.time()
        lb = Bar(self.barLength, taskCount=len(tasks), useETACalculation=True, useColor=True)
        current = 0

        def runprogress(perc, done, stop):
            i = perc
            while True:
                if stop():
                    break
                if i > 99:
                    i = random.randint(75, 90)

                total_time = time.time() - start_time
                lb.progressBar(i, total_time, done)
                i += 1

        # Creates inital speed for progress bar
        lb.start()
        totaltime = time.time() - start_time
        total = 0
        lb.progressBar(total, totaltime)
        time.sleep(0.005*self.estimatedTotalTime)
        totaltime = time.time() - start_time
        lb.progressBar(total+1, totaltime)

        # Runs each task
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

        # Ends
        time.sleep(0.1)
        lb.end((len(tasks)))

    def loadtasks(self):
        # Picks how many tasks to make
        ntasks = random.randint(2, 5)
        tasks = []
        totalperc = self.total

        for i in range(ntasks):
            # Creates tasks
            if ntasks == 1:
                j = 100
            else:
                j = random.randint(2, 6) * 10
                j *= (random.randint(95, 105) / 100)

            # Tweaks tasks so they sum to total
            totalperc -= j
            while totalperc < 0:
                j -= 1
                totalperc += 1
                for ii in range(len(tasks)):
                    if tasks[ii] < 5:
                        continue
                    else:
                        tasks[ii] = tasks[ii] - 1
                        totalperc += 1

            # Gives remaining percent to most recent task
            if i == ntasks-1:
                if totalperc != 0:
                    tasks[-1] += totalperc

            j = round(j, 1)
            tasks.append(j)

            if self.estimatedTotalTime > 5:
                time.sleep((random.randint(25, 75)/100)*(self.estimatedTotalTime/10))

        # Returns tasks in a list
        for i in range(len(tasks)):
            tasks[i] = round(tasks[i], 1)

        return tasks
