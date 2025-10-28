import unittest
import subprocess
import sys
import os
import textwrap


def run(code):
    code = textwrap.dedent(code)
    env = os.environ.copy()
    env.update({"PYTHONPATH": "."})
    result = subprocess.run(
        [sys.executable, "-c", code], env=env, capture_output=True, text=True
    )
    return result.stderr


class TestJsLikeTraceback(unittest.TestCase):
    def test(self):
        code = """
          def foo():
            bar()

          def bar():
            try:
              1/0
            except Exception as e:
              raise ValueError('Division error') from e

          foo()
        """
        code = textwrap.dedent(code)

        expected = """
         <string>:9:4
             raise ValueError('Division error') from e
         
         ValueError: Division error
             at bar (<string>:9:4)
             at foo (<string>:3:2)
             at <module> (<string>:11:0)
           [cause]: ZeroDivisionError: division by zero
               at bar (<string>:7:4)
        """
        expected = textwrap.dedent(expected).lstrip()

        result = run(code)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
