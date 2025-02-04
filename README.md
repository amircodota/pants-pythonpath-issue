# pants-pythonpath-issue

This repo is a simple repro to demonstrate an issue I'm having with running python tests using pants.

I have a customized directory structure, and running a pex binary works as expected, but running tests fails to import depndencies.

## TLDR

Running `pants run services/service1:binary` works as expected

```
> pants run services/service1:binary
Hello, World!
```

However,

```
pants test ::
```

Results in import error

```
> pants test ::
10:02:07.53 [INFO] Initializing scheduler...
10:02:07.57 [INFO] Initializing Nailgun pool for 32 processes...
10:02:09.12 [INFO] Scheduler initialized.
10:02:10.51 [ERROR] Completed: Run Pytest - services/service1/tests/test_logic.py:../tests - failed (exit code 1).
============================= test session starts ==============================
platform linux -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: /tmp/pants-sandbox-HSJJm4
collected 1 item

services/service1/tests/test_logic.py F                                  [100%]

=================================== FAILURES ===================================
_______________________________ test_get_message _______________________________

    def test_get_message():
        print(f"PYTHONPATH = {os.environ.get('PYTHONPATH', 'No PYTHONPATH')}")
    
>       from service1.logic import get_message
E       ModuleNotFoundError: No module named 'service1'

services/service1/tests/test_logic.py:7: ModuleNotFoundError
----------------------------- Captured stdout call -----------------------------
PYTHONPATH = No PYTHONPATH
- generated xml file: services.service1.tests.test_logic.py@tests.xml -
=========================== short test summary info ============================
FAILED services/service1/tests/test_logic.py::test_get_message - ModuleNotFoundError: No module named 'service1'
============================== 1 failed in 0.03s ===============================



✕ services/service1/tests/test_logic.py:../tests failed in 0.18s.
```

## Project Structure

The project is built from two python packages, `library1` and `service1`.
`service1` depends on `library1`.

Each package has the following tree

```
- package
  - src
    - package
      - __init__.py
      - *.py
  - tests
    - test_*.py
```

To allow this, I've set "src" and "tests" to be root patterns in pants.toml.

Indeed, when I run `pants roots` I get
```
pants roots
.
services/service1/src
services/service1/tests
shared/library1/src
```

## Another issue

When I got started, I kept running into an error with both `pants run` and `pants test`

```
Engine traceback:
  in `run` goal

NoSourceRootError: No source root found for `services/service1`. See https://www.pantsbuild.org/2.23/docs/using-pants/key-concepts/source-roots for how to define source roots.
```

To fix it, I also added `/` to the root_patterns, but maybe it is the wrong fix?