# Progress Indicators for Python

![pypi](https://shields.io/pypi/v/consloadingbar.svg)

![demo](./progressbar.gif)

GitHub Page: [flamechain/ConsLoadingBar](https://github.com/flamechain/ConsLoadingBar)

Full Docs: [flamechain/ConsLoadingBar/Documentation.md](https://github.com/flamechain/ConsLoadingBar/blob/main/Documentation.md)

## Quick-Start Guide

```python
import consloadingbar, time # import time for later use

lb = consloadingbar.Bar()
```

There are 3 different types of indicators to chose from:

- ``progressBar``
- ``progressCircle``
- ``progressStack``

### progressBar()

You params from the Bar() class to customize this. This means you can change what characters to use including the empty chars, see the demo above.

You can also specify taskCount, and eta.

```python
lb = consloadingbar.Bar(useColor=True, taskCount=10)

start = time.time()

for i in range(101):
    currentTime = time.time() - start
    lb.progress(i, time_=currentTime, tasksDone=i//10)
    time.sleep(0.01)
```

You can call the start() method to show an empty bar, and the end() method to show a full bar:

<pre>
<span style="color:green">Finished</span>
        |████████████████████| <span style="color:green">100%</span>
</pre>

### progressCircle()

This is used to show a spinner go round in a circle pattern. See demo above. To call just tell it when to stop using time, or stop() param.

```python
lb.progressCircle(time_=2) # Will run for 2 seconds
```

___

## Installation

Install via pip using `pip install ConsLoadingBar`.

```bash
pip install ConsLoadingBar
```

To make sure you have the current version you can use this command instead:

```bash
pip install --upgrade ConsLoadingBar
```

You can also directly call the module from python:

```bash
python3 -m pip install ConsLoadingBar
```

___

## License

ConsLoadingBar is licensed under the MIT License

___

<sub>Documentation Version 3.0 - Module Version 2.0.0 - PyPi Release 8</sub>
