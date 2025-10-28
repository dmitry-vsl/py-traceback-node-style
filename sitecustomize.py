import traceback
import sys


def print_stderr(line):
    print(line, file=sys.stderr)


def js_like_traceback(exc_type, exc_value, exc_tb, level=0):
    if isinstance(exc_value, SyntaxError):
        traceback.print_exception(exc_value)
        return

    stack_summary = traceback.extract_tb(exc_tb)
    frames = stack_summary[::-1]
    if level == 0:
        print_stderr(f"{frames[0].filename}:{frames[0].lineno}:{frames[0].colno}")
        topmost = stack_summary.format_frame_summary(frames[0])
        print_stderr("\n".join(topmost.split("\n")[1:]))
    indent = " " * 2 * level
    cause = "[cause]: " if level > 0 else ""
    print_stderr(indent + cause + f"{exc_type.__name__}: {exc_value}")
    for frame in frames:
        print_stderr(
            indent
            + f"    at {frame.name} ({frame.filename}:{frame.lineno}:{frame.colno})"
        )

    cause = exc_value.__cause__
    if cause is not None:
        js_like_traceback(type(cause), cause, cause.__traceback__, level + 1)


sys.excepthook = js_like_traceback
