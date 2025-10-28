# Format Python Tracebacks in Node.js Style

Consider the following program:
```
def foo():
  bar()

def bar():
  try:
    1/0
  except Exception as e:
    raise ValueError('Division error') from e

foo()
```

When run, it outputs a traceback:
```
Traceback (most recent call last):
  File "/private/tmp/test.py", line 6, in bar
    1/0
    ~^~
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/private/tmp/test.py", line 10, in <module>
    foo()
    ~~~^^
  File "/private/tmp/test.py", line 2, in foo
    bar()
    ~~~^^
  File "/private/tmp/test.py", line 8, in bar
    raise ValueError('Division error') from e
ValueError: Division error
```

Using this script, you can format the traceback output to match Node.js styling. It's vim-friendly—you can position your cursor on a line and press `gF` to jump to the exact location (file, line, and column):
```
/private/tmp/test.py:8:4
    raise ValueError('Division error') from e

ValueError: Division error
    at bar (/private/tmp/test.py:8:4)
    at foo (/private/tmp/test.py:2:2)
    at <module> (/private/tmp/test.py:10:0)
  [cause]: ZeroDivisionError: division by zero
      at bar (/private/tmp/test.py:6:4)

```

## How to Install

- Create a directory (for example, `/Users/someuser/js_like_traceback`)
- Save the file `./sitecustomize.py` to that directory
- Set PYTHONPATH in your `~/.profile`:
  ```
  export PYTHONPATH="/Users/someuser/js_like_traceback"
  ```

That's it! The `./sitecustomize.py` file will be automatically loaded and will customize how tracebacks are printed in your Python programs.
