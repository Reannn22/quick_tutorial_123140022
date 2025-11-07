# Student Information

Name: Reyhan Capri Moraga
NIM: 123140022

# Tutorial Sections Analysis

1. [Single-File Web Applications](#01-single-file-web-applications-analysis)
2. [Python Packages](#02-python-packages-analysis)
3. [Application Configuration](#03-application-configuration-analysis)
4. [Development with debugtoolbar](#04-debug-toolbar-analysis)
5. [Unit Tests and pytest](#05-unit-tests-and-pytest-analysis)
6. [Functional Testing](#06-functional-testing-analysis)
7. [Basic Web Handling](#07-basic-web-handling-analysis)
8. [HTML Generation With Templating](#08-html-generation-with-templating-analysis)
9. [View Classes](#09-view-classes-analysis)
10. [Web Requests and Responses](#10-web-requests-and-responses-analysis)
11. [URL Routing](#11-url-routing-analysis)
12. [Jinja2 Templating](#12-jinja2-templating-analysis)
13. [Static Assets](#13-static-assets-analysis)
14. [AJAX Development](#14-ajax-development-analysis)
15. [Advanced View Classes](#15-advanced-view-classes-analysis)
16. [Logging](#16-logging-analysis)
17. [Sessions](#17-sessions-analysis)
18. [Forms and Validation](#18-forms-and-validation-analysis)
19. [SQLAlchemy Databases](#19-sqlalchemy-databases-analysis)
20. [Authentication](#20-authentication-analysis)
21. [Authorization](#21-authorization-analysis)

---

# 01: Single-File Web Applications Analysis

## Background Summary

Pyramid can function as a microframework using a single-file module, while also scaling to larger applications. It implements WSGI standard and follows MVC pattern.

## Key Components Analysis

### 1. Application Structure

```python
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
```

- Uses Waitress as WSGI server
- Configurator for application setup
- Response for handling HTTP responses

### 2. Code Analysis

The key parts of the code:

```python
def hello_world(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')
```

This view function:

- Accepts a request parameter
- Prints debugging information
- Returns HTML response

```python
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
```

Configuration process:

- Sets up URL routing
- Connects view to route
- Creates WSGI application
- Starts server on port 6543

## Extra Credit Answers

1. `print('Incoming request')` vs `print 'Incoming request'`:

   - The parentheses version is Python 3 syntax
   - Print without parentheses is Python 2 legacy syntax

2. Return value alternatives:

   - HTML string: Would need to be wrapped in Response()
   - Integer sequence: Would raise a type error as Response expects string-like object

3. Invalid code (print xyz):

   - Raises NameError because xyz is undefined
   - Shows Pyramid's error handling capabilities

4. WSGI's "GI":
   - Modeled after CGI (Common Gateway Interface)
   - Provides standard interface between web servers and Python applications

---

# 02: Python Packages Analysis

## Background Summary

Python packages organize modules into namespaced units. Pyramid applications are typically structured as Python packages with a `setup.py` file for project management. This approach enables better organization, dependency management, and development workflow through tools like pip's editable installation mode.

## Key Components Analysis

### 1. Package Structure

```
package/
├── setup.py              # Project configuration
└── tutorial/             # Python package
    ├── __init__.py       # Makes directory a package
    └── app.py            # Application code
```

**Directory Organization:**

- **Project root (`package/`)**: Contains project-level files
- **Package directory (`tutorial/`)**: The actual Python package
- **`__init__.py`**: Special file that marks directory as a package
- **`app.py`**: Application logic module

### 2. setup.py Configuration

```python
from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
)
```

**Key Elements:**

- **setuptools**: Python's packaging library
- **name**: Project identifier ('tutorial')
- **install_requires**: Lists dependencies (pyramid, waitress)
- **Dependency management**: Automatically installs required packages

### 3. Development Mode Installation

```bash
$VENV/bin/pip install -e .
```

**What happens:**

- **`-e` flag**: Installs in "editable" or "development" mode
- **`.` parameter**: Refers to current directory
- **Effect**: Creates link to source code instead of copying
- **Benefit**: Code changes are immediately available without reinstalling

### 4. Package vs Project Distinction

**Python Package:**

- Directory with `__init__.py`
- Contains related Python modules
- Example: `tutorial/` directory

**Python Project:**

- Contains one or more packages
- Has `setup.py` for configuration
- Manages dependencies and metadata
- Example: `package/` directory with `setup.py`

## Code Analysis

### The **init**.py File

```python
# package
```

- Minimal content (just a comment)
- Primary purpose: marks directory as package
- Can be empty or contain initialization code
- Enables `import tutorial` statements

### Application Module (app.py)

The code remains identical to single-file version:

```python
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
```

**Key difference**: Now runs as module within package structure

## Advantages of Package Structure

### 1. Organization

- Separates project configuration from code
- Groups related modules together
- Scales better for larger applications

### 2. Dependency Management

- Automatic installation of requirements
- Version control for dependencies
- Easier collaboration (others can install with same deps)

### 3. Development Workflow

- Editable installation for active development
- No need to reinstall after code changes
- Package available system-wide in virtual environment

### 4. Professional Standards

- Follows Python community best practices
- Prepares for distribution (PyPI, etc.)
- Enables testing and documentation tools

## Important Notes

### Running as Script

```bash
python tutorial/app.py
```

**Why this is unusual:**

- Running module inside package directly is unconventional
- Done here for tutorial clarity
- Production apps use different entry points (console scripts, WSGI servers)
- Generally considered bad practice

### sys.path Consideration

- Package must be on Python's `sys.path`
- Development mode installation handles this automatically
- Allows imports from anywhere: `from tutorial import app`

## Working in Development Mode

**Traditional Installation:**

```bash
pip install .  # Copies files to site-packages
```

**Development Installation:**

```bash
pip install -e .  # Creates link to source
```

**Benefits of `-e` flag:**

- Edit code and see changes immediately
- No reinstall needed after modifications
- Perfect for active development
- Easy debugging and testing

## Extra Credit Answers

1. **What happens without `__init__.py`?**

   - Directory won't be recognized as package
   - Import statements will fail
   - Python 3.3+ has "namespace packages" but explicit `__init__.py` is clearer

2. **Can `__init__.py` contain code?**

   - Yes, it can contain initialization code
   - Often used for package-level imports
   - Executed when package is first imported
   - Example: `from .app import hello_world`

3. **Why use `setup.py` for small projects?**

   - Dependency management
   - Reproducible installations
   - Professional development workflow
   - Easy transition to larger projects

4. **Difference between `pip install .` and `pip install -e .`?**
   - Regular install: Copies files to site-packages
   - Editable install: Creates symbolic link
   - Editable allows real-time code changes
   - Regular install requires reinstall after changes

---

# 03: Application Configuration Analysis

## Background Summary

Pyramid separates configuration from code using `.ini` files, leveraging Python's Setuptools entry points. This approach uses the `pserve` command to bootstrap applications, providing a standardized way to configure WSGI servers, logging, and application settings. This configuration-driven approach distinguishes Pyramid from other Python web frameworks.

## Key Components Analysis

### 1. Entry Points in setup.py

```python
from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

**Entry Point Breakdown:**

- **`paste.app_factory`**: Standard entry point category for WSGI apps
- **`main`**: Name of this specific entry point
- **`tutorial:main`**: Points to `main` function in `tutorial` package
- **Purpose**: Tells Pyramid where to find the WSGI application factory

### 2. Configuration File Structure (development.ini)

```ini
[app:main]
use = egg:tutorial

[server:main]
use = egg:waitress#main
listen = localhost:6543
```

**Section Analysis:**

**[app:main]:**

- Defines the WSGI application configuration
- `use = egg:tutorial`: References the installed package entry point
- Pyramid looks up the `tutorial:main` entry point from setup.py

**[server:main]:**

- Configures the WSGI server
- `use = egg:waitress#main`: Specifies Waitress as WSGI server
- `listen = localhost:6543`: Sets host and port binding

### 3. Application Factory Pattern (**init**.py)

```python
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
```

**Function Signatures:**

**`main(global_config, **settings)`:\*\*

- **global_config**: Global configuration from .ini file (rarely used)
- **settings**: Keyword arguments from app section in .ini
- **Returns**: WSGI application instance

**Application Factory Pattern:**

- Function that creates and returns WSGI app
- Called once during server startup
- Allows dynamic configuration based on .ini settings

### 4. Bootstrap Process Flow

```
1. pserve development.ini
   ↓
2. Reads [app:main] section
   ↓
3. Finds "use = egg:tutorial"
   ↓
4. Looks up entry point in setup.py
   ↓
5. Finds "main = tutorial:main"
   ↓
6. Imports tutorial package
   ↓
7. Calls tutorial.main(global_config, **settings)
   ↓
8. Returns WSGI app
   ↓
9. Passes to [server:main] (Waitress)
   ↓
10. Server starts listening on localhost:6543
```

## Code Changes from Previous Step

### Removed: tutorial/app.py

- No longer needed with pserve
- Logic moved to `__init__.py`
- Eliminates direct script execution

### Modified: setup.py

```python
# Added entry_points section
entry_points={
    'paste.app_factory': [
        'main = tutorial:main'
    ],
},
```

### Modified: tutorial/**init**.py

```python
# Changed from:
if __name__ == '__main__':
    # bootstrap code

# To:
def main(global_config, **settings):
    # bootstrap code
    return config.make_wsgi_app()
```

**Key Differences:**

- No more `if __name__ == '__main__'`
- Removed direct `serve()` call
- Added factory function pattern
- Configuration passed as parameters

## Configuration File Benefits

### 1. Separation of Concerns

- Configuration separate from code
- Easy to modify without touching Python
- Different configs for dev/staging/production

### 2. WSGI Server Configuration

```ini
[server:main]
use = egg:waitress#main
listen = localhost:6543
```

- Centralized server settings
- Easy to switch WSGI servers
- Port and host configuration
- Can add workers, threads, timeouts

### 3. Python Logging Configuration

```ini
# (Not shown in minimal example)
[loggers]
keys = root, tutorial

[handlers]
keys = console

[formatters]
keys = generic
```

- Standard Python logging setup
- Configurable log levels
- Multiple handlers (console, file, etc.)
- Professional logging without code changes

### 4. Environment-Specific Configurations

```
development.ini  # Dev settings (debug on, auto-reload)
production.ini   # Prod settings (debug off, optimized)
testing.ini      # Test settings (test database)
```

## pserve Command

### Basic Usage

```bash
$VENV/bin/pserve development.ini
```

### With Auto-Reload

```bash
$VENV/bin/pserve development.ini --reload
```

**`--reload` Flag:**

- Monitors filesystem for changes
- Automatically restarts application
- Watches Python files, .ini files, templates
- Essential for development workflow
- **Do not use in production**

### Other Useful Flags

```bash
pserve development.ini --reload --verbose  # More logging
pserve development.ini -n 4                # Multiple processes
```

## Package Structure Evolution

**Before (Step 02):**

```
package/
├── setup.py
└── tutorial/
    ├── __init__.py    # Empty
    └── app.py         # All code here
```

**After (Step 03):**

```
ini/
├── setup.py           # Added entry_points
├── development.ini    # New configuration file
└── tutorial/
    └── __init__.py    # Contains main() factory
```

**Changes:**

- Removed `app.py`
- Added `development.ini`
- Moved code to `__init__.py`
- Added entry point in `setup.py`

## Why Move Code to **init**.py?

### Common Pyramid Convention

```python
# tutorial/__init__.py
def main(global_config, **settings):
    """Application factory"""
    config = Configurator(settings=settings)
    # ... configuration ...
    return config.make_wsgi_app()
```

**Advantages:**

- Package-level initialization
- Clear entry point for application
- Separates app creation from view logic
- Follows Pyramid community standards

**Alternative Approach:**

```python
# Could use tutorial/app.py instead
entry_points={
    'paste.app_factory': [
        'main = tutorial.app:main'
    ],
},
```

## Installation and Egg Info

### Running Installation

```bash
$VENV/bin/pip install -e .
```

**What Happens:**

- Checks dependencies in `setup.py`
- Installs missing packages
- Generates `tutorial.egg-info/` directory
- Registers entry points
- Creates development link

### Egg Info Directory

```
tutorial.egg-info/
├── PKG-INFO
├── SOURCES.txt
├── dependency_links.txt
├── entry_points.txt      # Contains our entry point
├── requires.txt
└── top_level.txt
```

**entry_points.txt contains:**

```
[paste.app_factory]
main = tutorial:main
```

## Extra Credit Answers

### 1. Could you do this in Python code without .ini files?

**Yes, absolutely!** Example:

```python
# Without .ini
if __name__ == '__main__':
    settings = {
        'pyramid.reload_templates': True,
        'pyramid.debug_authorization': False,
        'pyramid.debug_notfound': False,
    }

    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()

    serve(app, host='localhost', port=6543)
```

**Why use .ini then?**

- Easier for non-programmers to modify
- Standard format for deployment tools
- Cleaner separation of config and code
- Logging configuration in one place
- Industry best practice

### 2. Can we have multiple .ini files? Why?

**Yes!** Very common pattern:

```
development.ini     # Local development
production.ini      # Production server
testing.ini         # Automated tests
staging.ini         # Staging environment
```

**Why multiple configs?**

- Different database connections
- Different debug settings
- Different logging levels
- Different server configurations
- Different security settings

**Usage:**

```bash
pserve development.ini  # Development
pserve production.ini   # Production
pserve testing.ini      # Testing
```

### 3. Why didn't entry point mention **init**.py?

**Python Package Import Rules:**

```python
entry_points={
    'paste.app_factory': [
        'main = tutorial:main'  # Not tutorial.__init__:main
    ],
}
```

**Explanation:**

- `tutorial` refers to the **package**, not a module
- When you import a package, Python automatically imports `__init__.py`
- `tutorial:main` means "the `main` function in the `tutorial` package"
- Python knows to look in `__init__.py`
- This is standard Python import behavior

**Equivalent Imports:**

```python
from tutorial import main           # Looks in __init__.py
from tutorial.__init__ import main  # Explicitly, but unnecessary
```

### 4. What is `**settings`? What does `**` signify?

**Python's kwargs (Keyword Arguments):**

```python
def main(global_config, **settings):
    # settings is a dictionary
    pass
```

**The `**` operator:\*\*

- Collects all keyword arguments into a dictionary
- Called "kwargs" in Python
- Allows flexible parameter passing

**Example:**

```python
# Calling the function
main(config, debug=True, reload=True, db_url='sqlite:///test.db')

# Inside function, settings equals:
# {
#     'debug': True,
#     'reload': True,
#     'db_url': 'sqlite:///test.db'
# }
```

**From .ini file:**

```ini
[app:main]
use = egg:tutorial
pyramid.reload_templates = true
pyramid.debug_all = false
```

These become:

```python
settings = {
    'pyramid.reload_templates': 'true',
    'pyramid.debug_all': 'false'
}
```

**Usage in code:**

```python
def main(global_config, **settings):
    config = Configurator(settings=settings)  # Pass along
    # Or access individually:
    debug = settings.get('pyramid.debug_all', False)
```

## Summary of Benefits

### Configuration-Driven Approach

✅ Separate code from configuration
✅ Multiple environments (dev/prod/test)
✅ Standard Python logging setup
✅ Easy WSGI server switching
✅ No code changes for deployment
✅ Industry-standard PasteDeploy format

### pserve Benefits

✅ Auto-reload during development
✅ Standard command across Pyramid apps
✅ Manages WSGI server lifecycle
✅ Proper logging configuration
✅ Production-ready deployment pattern

---

# 04: Debug Toolbar Analysis

## Background Summary

The `pyramid_debugtoolbar` is a popular Pyramid add-on that provides debugging and introspection tools directly in the browser. It demonstrates how Pyramid add-ons work, how they integrate via configuration, and introduces Setuptools extras for optional dependencies. This toolbar significantly improves development productivity by providing error tracebacks, request inspection, and performance profiling.

## Key Components Analysis

### 1. Setuptools Extras in setup.py

```python
from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

dev_requires = [
    'pyramid_debugtoolbar',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

**Dependency Structure:**

**`install_requires`:**

- Core dependencies needed for the app to run
- Installed with: `pip install -e .`
- Required in all environments (dev/prod)
- Examples: pyramid, waitress

**`extras_require`:**

- Optional dependencies grouped by purpose
- Installed with: `pip install -e ".[dev]"`
- Environment-specific requirements
- Key = extra name, Value = list of packages

**Why Separate?**

- Production doesn't need debug tools
- Smaller production deployments
- Faster production installations
- Clear separation of concerns

### 2. Installing with Extras

```bash
$VENV/bin/pip install -e ".[dev]"
```

**Command Breakdown:**

- **`-e`**: Editable/development mode
- **`.`**: Current directory (package root)
- **`[dev]`**: Install the "dev" extra
- **`"..."`**: Quotes needed for shell interpretation

**What Gets Installed:**

```
pyramid          (from requires)
waitress         (from requires)
pyramid_debugtoolbar (from dev_requires)
```

**Alternative Installations:**

```bash
pip install -e .              # Core only
pip install -e ".[dev]"       # Core + dev extras
pip install -e ".[dev,test]"  # Multiple extras
```

### 3. Configuration via pyramid.includes

```ini
[app:main]
use = egg:tutorial
pyramid.includes =
    pyramid_debugtoolbar

[server:main]
use = egg:waitress#main
listen = localhost:6543
```

**pyramid.includes Explained:**

- Declarative configuration in .ini file
- Each line names a Pyramid add-on to include
- Executed during application startup
- Alternative to imperative `config.include()`

**How It Works:**

```
1. pserve reads development.ini
2. Finds pyramid.includes section
3. Imports pyramid_debugtoolbar
4. Calls its includeme() function
5. Toolbar configures itself into the app
```

### 4. Two Ways to Include Add-ons

**Declarative (in .ini file):**

```ini
pyramid.includes =
    pyramid_debugtoolbar
    pyramid_tm
    pyramid_jinja2
```

✅ No code changes needed
✅ Easy to enable/disable per environment
✅ Configuration-driven

**Imperative (in **init**.py):**

```python
def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_tm')
    # ... rest of configuration
    return config.make_wsgi_app()
```

✅ Programmatic control
✅ Conditional includes
✅ Required for some add-ons

## Pyramid Add-ons Explained

### What is a Pyramid Add-on?

**Definition:**

- Python package that extends Pyramid
- Follows specific conventions
- Has an `includeme()` function
- Configures itself when included

**Structure:**

```python
# Inside pyramid_debugtoolbar package
def includeme(config):
    """Called when add-on is included"""
    config.add_tween('pyramid_debugtoolbar.toolbar_tween_factory')
    config.add_route('debugtoolbar.static', '/_debug_toolbar/static/*path')
    # ... more configuration
```

### Popular Pyramid Add-ons

- **pyramid_debugtoolbar**: Development debugging
- **pyramid_jinja2**: Jinja2 templating
- **pyramid_tm**: Transaction management
- **pyramid_mailer**: Email sending
- **pyramid_beaker**: Session management
- **pyramid_exclog**: Exception logging

### How Add-ons Integrate

```
Your App         Add-on
   ↓               ↓
   config.include('pyramid_debugtoolbar')
   ↓
   Calls add-on's includeme(config)
   ↓
   Add-on configures:
   - Routes
   - Views
   - Tweens (middleware)
   - Settings
   ↓
   Integrated into your app
```

## Debug Toolbar Features

### 1. Visual Toolbar Interface

```
┌─────────────────────────────────┐
│  Your Web Application           │
│                                 │
│  [Content Here]                 │
│                                 │  ┌──────────┐
│                                 │  │ Pyramid  │ ← Click to open
│                                 │  │   ⚙️     │
│                                 └──────────┘
└─────────────────────────────────┘
```

**Toolbar Panels:**

- **Request/Response**: HTTP headers, status
- **Performance**: Timing information
- **SQLAlchemy**: Database queries (if using)
- **Routes**: Registered routes
- **Tweens**: Active middleware
- **Introspection**: Application structure

### 2. Error Handling

**Before Debugtoolbar:**

```
Internal Server Error
The server encountered an internal error.
```

**With Debugtoolbar:**

```
Traceback (most recent call last):
  File "tutorial/__init__.py", line 6, in hello_world
    return xResponse('<body><h1>Hello World!</h1></body>')
NameError: name 'xResponse' is not defined

[Interactive Debugger]
>>> request
<Request at 0x...>
>>> Response
<class 'pyramid.response.Response'>
```

### 3. Interactive Debugger

- Click screen icon on traceback lines
- Inspect variables at that point in code
- Execute Python expressions
- Test fixes before editing code

### 4. HTML Injection

```html
<!-- Your original HTML -->
<body>
  <h1>Hello World!</h1>
</body>

<!-- Becomes (with toolbar) -->
<body>
  <h1>Hello World!</h1>
  <!-- Toolbar HTML/CSS/JS injected here -->
  <div id="pDebug">...</div>
</body>
```

**Important Note:**

- Injects before closing `</body>` tag
- May cause CSS/JS conflicts in rare cases
- Can be disabled by commenting out in .ini

## Configuration Management

### Development Configuration

```ini
# development.ini
[app:main]
use = egg:tutorial
pyramid.includes =
    pyramid_debugtoolbar  # Enabled for development
pyramid.reload_templates = true
```

### Production Configuration

```ini
# production.ini
[app:main]
use = egg:tutorial
# pyramid.includes =
#     pyramid_debugtoolbar  # DISABLED for production
pyramid.reload_templates = false
```

**Benefits:**

- No code changes between environments
- Just use different .ini file
- Safe production deployment
- Easy to toggle features

## Extra Credit Answers

1. **Why use `dev_requires` instead of `requires`?**

**Reasons for Separation:**

**Production Concerns:**

```python
# BAD: Everything in requires
requires = [
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar',  # ❌ Not needed in production
    'pytest',                 # ❌ Not needed in production
    'ipdb',                   # ❌ Not needed in production
]
```

**Better Approach:**

```python
# GOOD: Separated by purpose
requires = [
    'pyramid',     # ✅ Core dependency
    'waitress',    # ✅ Production server
]

dev_requires = [
    'pyramid_debugtoolbar',  # ✅ Development only
    'pytest',                # ✅ Testing only
    'ipdb',                  # ✅ Debugging only
]
```

**Advantages:**

1. **Smaller Production Deployments**

   - Less disk space
   - Faster deployments
   - Fewer security risks

2. **Security**

   - Debug tools expose sensitive info
   - Shouldn't be in production
   - Attack surface reduction

3. **Performance**

   - Debug tools add overhead
   - Slower request processing
   - Memory usage

4. **Clarity**

   - Clear what's optional
   - Self-documenting dependencies
   - Easy to understand purpose

5. **Flexibility**

   ```bash
   # Developer installs
   pip install -e ".[dev]"


   # CI/CD installs
   pip install -e ".[test]"


   # Production installs
   pip install .
   ```

**Common Extras Categories:**

```python
extras_require={
    'dev': [
        'pyramid_debugtoolbar',
        'pyramid_ipython',
    ],
    'test': [
        'pytest',
        'pytest-cov',
        'WebTest',
    ],
    'docs': [
        'sphinx',
        'sphinx_rtd_theme',
    ],
}
```

### 2. Introduce a Bug and Use Interactive Debugger

**Original Code:**

```python
def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')
```

**Buggy Code:**

```python
def hello_world(request):
    return xResponse('<body><h1>Hello World!</h1></body>')
    #      ^ NameError: undefined variable
```

**What Happens:**

**In Browser:**

```
NameError: name 'xResponse' is not defined

Traceback (most recent call last):
  File ".../tutorial/__init__.py", line 6, in hello_world
    return xResponse('<body><h1>Hello World!</h1></body>')

[Local Variables]
request = <Request GET http://localhost:6543/>
```

**Using the Interactive Debugger:**

Click the screen icon (🖥️) on the error line to get an interactive Python shell:

```python
>>> # Inspect the request object
>>> request
<Request at 0x7f8b3c2d1e50 GET http://localhost:6543/>

>>> # Check request attributes
>>> request.method
'GET'

>>> request.path
'/'

>>> request.params
<NoVars: Not a form request>

>>> # Verify Response is available
>>> Response
<class 'pyramid.response.Response'>

>>> # Test the fix
>>> Response('<body><h1>Hello World!</h1></body>')
<Response at 0x... 200 OK>

>>> # Check what variables are available
>>> dir()
['Response', '__builtins__', 'request', ...]

>>> # Inspect the configuration
>>> request.registry.settings
{'pyramid.includes': '...', ...}
```

**What You Can Discover:**

1. **Request Information:**

   ```python
   >>> request.url
   'http://localhost:6543/'

   >>> request.headers
   {'Host': 'localhost:6543', 'User-Agent': '...', ...}

   >>> request.environ
   {...}  # Full WSGI environment
   ```

2. **Available Imports:**

   ```python
   >>> Response
   <class 'pyramid.response.Response'>

   >>> Configurator
   NameError  # Not imported in this scope
   ```

3. **Test Fixes:**

   ```python
   >>> # Try the correct code
   >>> resp = Response('<body><h1>Hello World!</h1></body>')
   >>> resp.status_code
   200
   >>> resp.content_type
   'text/html; charset=UTF-8'
   ```

4. **Explore the Framework:**

   ```python
   >>> request.registry
   <Registry ...>

   >>> request.matched_route
   <Route 'hello' ...>

   >>> request.route_url('hello')
   'http://localhost:6543/'
   ```

5. **Debug Complex Issues:**

   ```python
   >>> # Check if variable exists
   >>> 'xResponse' in dir()
   False

   >>> # Find similar names
   >>> [x for x in dir() if 'Response' in x]
   ['Response']
   ```

## Best Practices

### 1. Environment-Specific Configuration

```bash
# Development
pserve development.ini --reload

# Production (no toolbar)
pserve production.ini
```

### 2. Security

❌ **NEVER enable in production:**

```ini
# production.ini - BAD!
pyramid.includes =
    pyramid_debugtoolbar  # ❌ Exposes sensitive data
```

✅ **Only in development:**

```ini
# development.ini - GOOD!
pyramid.includes =
    pyramid_debugtoolbar  # ✅ Safe for local dev
```

### 3. Troubleshooting

If toolbar causes issues:

```ini
# Temporarily disable
# pyramid.includes =
#     pyramid_debugtoolbar
```

### 4. Performance

- Toolbar adds overhead
- Not suitable for performance testing
- Disable when benchmarking

## Summary

### Pyramid Add-ons

✅ Extend Pyramid functionality
✅ Follow includeme() convention
✅ Configure via .ini or code
✅ Modular and reusable

### Debug Toolbar Benefits

✅ Rich error tracebacks
✅ Interactive debugger
✅ Request/response inspection
✅ Performance profiling
✅ Easy to enable/disable

### Setuptools Extras

✅ Optional dependencies
✅ Environment-specific installs
✅ Smaller production deployments
✅ Clear dependency purposes

---

# 05: Unit Tests and pytest Analysis

## Background Summary

Testing is fundamental to software quality - "Untested code is broken code." Pyramid has maintained a commitment to testing with 100% test coverage from its earliest releases. While Python includes unittest in its standard library, the Pyramid community prefers pytest for its enhanced functionality and convenience. This tutorial introduces unit testing without being pedantic about test-driven development (TDD), focusing on practical testing to catch major issues during development.

## Key Components Analysis

### 1. Adding pytest as Development Dependency

**Updated setup.py:**

```python
from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',  # ← New addition
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

**Why pytest in dev_requires:**

- Testing is a development-time activity
- Not needed in production deployments
- Keeps production environment lean
- Part of the development workflow

**Installation Command:**

```bash
$VENV/bin/pip install -e ".[dev]"
```

This installs:

- All `requires` packages (pyramid, waitress)
- All `dev_requires` packages (pyramid_debugtoolbar, pytest)
- The tutorial package in editable mode

### 2. Test File Structure (tutorial/tests.py)

```python
import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
```

**Code Breakdown:**

**Imports:**

```python
import unittest  # Python's standard testing framework
from pyramid import testing  # Pyramid's testing helpers
```

**Test Class:**

```python
class TutorialViewTests(unittest.TestCase):
    # Inherits from unittest.TestCase
    # Groups related tests together
    # Provides assertion methods
```

**setUp Method:**

```python
def setUp(self):
    self.config = testing.setUp()
```

- Called before each test method
- Creates fresh test configuration
- Isolates tests from each other
- `self.config` is a Configurator instance

**tearDown Method:**

```python
def tearDown(self):
    testing.tearDown()
```

- Called after each test method
- Cleans up test configuration
- Ensures no state leaks between tests
- Important for test isolation

### 3. The test_hello_world Test Method

```python
def test_hello_world(self):
    from tutorial import hello_world

    request = testing.DummyRequest()
    response = hello_world(request)
    self.assertEqual(response.status_code, 200)
```

**Step-by-Step Analysis:**

**1. Import Inside Test:**

```python
from tutorial import hello_world
```

- Why not at module level?
- Avoids import side effects
- Maintains test isolation
- Each test gets clean imports
- Module-level code runs only once
- State can leak between tests
- Import side effects affect all tests
- Example: `from tutorial import hello_world`

**Real-World Example:**

```python
# tutorial/__init__.py
import os

# This runs at import time
DATABASE_URL = os.getenv('DATABASE_URL', 'default.db')
connection = connect_to_database(DATABASE_URL)

def hello_world(request):
    # Uses the module-level connection
    return Response('Hello')

# tests.py - Top-level import
from tutorial import hello_world  # Connection created NOW

class TestCase1(unittest.TestCase):
    def test_one(self):
        # Uses connection from import time
        pass

class TestCase2(unittest.TestCase):
    def test_two(self):
        # Still uses SAME connection from import time
        # Can't test with different DATABASE_URL
        pass

# tests.py - Import inside test
class TestCase1(unittest.TestCase):
    def test_one(self):
        os.environ['DATABASE_URL'] = 'test1.db'
        from tutorial import hello_world  # Fresh import, fresh connection
        pass

class TestCase2(unittest.TestCase):
    def test_two(self):
        os.environ['DATABASE_URL'] = 'test2.db'
        from tutorial import hello_world  # Different connection
        pass
```

**Performance Note:**

- Python caches imports in `sys.modules`
- Subsequent imports from cache are fast
- The performance hit is negligible
- Test isolation is worth it
- When Top-Level Import is OK:

```python
# Testing utilities, not application code
import unittest
from pyramid import testing  # ✅ Framework code, no side effects

# Third-party libraries
import pytest  # ✅ No side effects
from lxml import html  # ✅ No side effects

# Your application code
class Tests(unittest.TestCase):
    def test_something(self):
        from tutorial import my_view  # ✅ Application code, import inside
```

## Pyramid Testing Helpers

### 1. testing.setUp()

```python
config = testing.setUp()
```

**What it does:**

- Creates a new Configurator instance
- Provides isolated test configuration
- Allows adding test-specific routes/views
- Returns the config object

**Usage:**

```python
def setUp(self):
    self.config = testing.setUp()
    # Can add test-specific configuration:
    # self.config.add_route('test_route', '/test')
```

### 2. testing.tearDown()

```python
testing.tearDown()
```

**What it does:**

- Cleans up configuration created by setUp()
- Resets global Pyramid state
- Ensures test isolation
- Prevents test interference

**Usage:**

```python
def tearDown(self):
    testing.tearDown()
```

### 3. testing.DummyRequest()

```python
request = testing.DummyRequest()
```

**What it provides:**

- Fake HTTP request object
- Has all standard request attributes
- Customizable for test scenarios
- No web server required

**Customization Examples:**

```python
# Basic request
request = testing.DummyRequest()

# With params
request = testing.DummyRequest(params={'name': 'value'})

# With POST data
request = testing.DummyRequest(post={'field': 'data'})

# With matched route
request = testing.DummyRequest()
request.matched_route = DummyRoute('route_name')

# With custom attributes
request = testing.DummyRequest()
request.user = MockUser()
```

### 4. When setUp/tearDown Are Actually Needed

**Current Example:**

```python
def setUp(self):
    self.config = testing.setUp()  # Created but not used

def tearDown(self):
    testing.tearDown()

def test_hello_world(self):
    # Doesn't use self.config
    from tutorial import hello_world
    request = testing.DummyRequest()
    response = hello_world(request)
    self.assertEqual(response.status_code, 200)
```

**Note from tutorial:** "Our use of pyramid.testing.setUp() and pyramid.testing.tearDown() aren't actually necessary here."

**When They ARE Necessary:**

```python
def setUp(self):
    self.config = testing.setUp()
    # Adding configuration that view needs
    self.config.add_route('user', '/users/{id}')
    self.config.add_settings({'db.url': 'sqlite:///:memory:'})

def test_view_needs_config(self):
    from tutorial import user_view

    request = testing.DummyRequest()
    request.matched_route = DummyRoute('user', '/users/123')

    # View uses config to look up settings or routes
    response = user_view(request)
    self.assertEqual(response.status_code, 200)
```

## Unit Testing Principles

### 1. Test Isolation (Units)

```python
from tutorial import hello_world  # ✅ Import inside

# vs.

from tutorial import hello_world  # ❌ Import at module level
```

**Why import inside tests?**

- Prevents import side effects from affecting other tests
- Each test gets clean module state
- Module-level code runs only once
- State can leak between tests
- Import side effects affect all tests
- Example: `from tutorial import hello_world`

**Real-World Example:**

```python
# tutorial/__init__.py
import os

# This runs at import time
DATABASE_URL = os.getenv('DATABASE_URL', 'default.db')
connection = connect_to_database(DATABASE_URL)

def hello_world(request):
    # Uses the module-level connection
    return Response('Hello')

# tests.py - Top-level import
from tutorial import hello_world  # Connection created NOW

class TestCase1(unittest.TestCase):
    def test_one(self):
        # Uses connection from import time
        pass

class TestCase2(unittest.TestCase):
    def test_two(self):
        # Still uses SAME connection from import time
        # Can't test with different DATABASE_URL
        pass

# tests.py - Import inside test
class TestCase1(unittest.TestCase):
    def test_one(self):
        os.environ['DATABASE_URL'] = 'test1.db'
        from tutorial import hello_world  # Fresh import, fresh connection
        pass

class TestCase2(unittest.TestCase):
    def test_two(self):
        os.environ['DATABASE_URL'] = 'test2.db'
        from tutorial import hello_world  # Different connection
        pass
```

**Performance Note:**

- Python caches imports in `sys.modules`
- Subsequent imports from cache are fast
- The performance hit is negligible
- Test isolation is worth it
- When Top-Level Import is OK:

```python
# Testing utilities, not application code
import unittest
from pyramid import testing  # ✅ Framework code, no side effects

# Third-party libraries
import pytest  # ✅ No side effects
from lxml import html  # ✅ No side effects

# Your application code
class Tests(unittest.TestCase):
    def test_something(self):
        from tutorial import my_view  # ✅ Application code, import inside
```

## Summary

### Testing Guidelines:

- ✅ Write tests as you develop
- ✅ Test the contract (expected behavior)
- ✅ Keep tests fast and isolated
- ✅ Import application code inside tests
- ✅ Use descriptive test names
- ✅ One assertion per test (generally)
- ✅ Test both success and failure cases

### Test Organization:

```
tutorial/
├── __init__.py
├── views.py
└── tests.py         # or tests/
                     #     ├── test_views.py
                     #     ├── test_models.py
                     #     └── test_utils.py
```

### Running Tests in Development:

```bash
# Quick check during development
pytest tutorial/tests.py -q

# With coverage
pytest --cov=tutorial

# Watch mode (with pytest-watch)
ptw tutorial/

# In CI/CD pipeline
pytest --junitxml=report.xml
```

---

# 06: Functional Testing Analysis

## Background Summary

Unit tests (like in step 5) are excellent for testing individual functions in isolation. However, unit tests **do not verify** if all the application components (like routing, views, and templates) are wired together and working correctly.

**Functional testing** bridges this gap. We use the **WebTest** library to simulate HTTP requests (like GET or POST) against our entire WSGI application. WebTest runs the full application stack—from routing through view execution and response rendering—but does it in-memory **without needing to run an actual HTTP server**. This makes it incredibly fast, fast enough to be run alongside our unit tests.

## Key Components Analysis

### 1. Dependency Update (setup.py)

We add `webtest` as a development dependency. This is logical because, like `pytest`, WebTest is only needed during development and testing, not in a production environment.

**setup.py:**

```python
# ... (requires list remains the same)

# List of dependencies installed via `pip install -e ".[dev]"`
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',  # <-- Added
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,  # <-- 'dev' extra now includes webtest
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

After updating this file, we run `$VENV/bin/pip install -e ".[dev]"` to install the new `webtest` package.

### 2. Test File Update (tutorial/tests.py)

We **add a new test class** to our existing `tutorial/tests.py` file. This file now contains _both_ types of tests: unit and functional.

```python
import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home
        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visit', response.body)

    def test_hello(self):
        from .views import hello
        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go back', response.body)

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)
    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', res.body)
    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<h1>Hi Hello View', res.body)
```

- Unit tests call views directly and check for expected content
- Functional tests use WebTest to simulate HTTP requests and check responses

## Analysis

- Views and their registrations are now separated from startup code.
- `config.scan('.views')` finds all views decorated with `@view_config`.
- Two URLs: `/` and `/howdy`, each linking to the other.
- The route name, URL, and view function name can all be different.
- `@view_config` (declarative) and `config.add_view` (imperative) both register views; choice is a matter of taste.

## Extra Credit Answers

1. **What does the dot in `.views` signify?**

   - The dot means "relative import" from the current package, so `config.scan('.views')` scans the `views` module in the same package.

2. **Why might `assertIn` be a better choice in testing the text in responses than `assertEqual`?**

   - `assertIn` checks for the presence of a substring, making tests less brittle to formatting changes or extra content. `assertEqual` requires an exact match, which can fail if the response contains additional HTML or whitespace.

3. **Views, View Configuration, and Debugging View Configuration**
   - Views are functions that handle requests. Configuration can be done imperatively (`config.add_view`) or declaratively (`@view_config`). Debugging view configuration is easier with decorators and scanning, as it keeps view logic and registration together.

---

# 07: Basic Web Handling With Views Analysis

## Background Summary

In Pyramid, views are the main way to handle web requests and return responses. Previously, everything (view function, registration, route, and WSGI launcher) was in one file. Now, views are moved to a separate `views.py` module, and the configurator scans this module for decorators that register views. This approach organizes code better and allows declarative configuration using decorators.

## Key Components Analysis

### 1. Application Startup (`tutorial/__init__.py`)

```python
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()
```

- Adds two routes: `'home'` and `'hello'`
- Scans the `views` module for view registrations via decorators

### 2. Views Module (`tutorial/views.py`)

```python
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'name': 'Home View'}

@view_config(route_name='hello', renderer='home.pt')
def hello(request):
    return {'name': 'Hello View'}
```

- Uses `@view_config` decorator for declarative view registration
- Each view returns a simple HTML response with a link to the other view

### 3. Updated Tests (`tutorial/tests.py`)

```python
import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home
        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import hello
        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual('Hello View', response['name'])

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<h1>Hi Hello View', res.body)
```

- Unit tests call views directly and check for expected content
- Functional tests use WebTest to simulate HTTP requests and check responses

## Analysis

- Views and their registrations are now separated from startup code.
- `config.scan('.views')` finds all views decorated with `@view_config`.
- Two URLs: `/` and `/howdy`, each linking to the other.
- The route name, URL, and view function name can all be different.
- `@view_config` (declarative) and `config.add_view` (imperative) both register views; choice is a matter of taste.

## Extra Credit Answers

1. **What does the dot in `.views` signify?**

   - The dot means "relative import" from the current package, so `config.scan('.views')` scans the `views` module in the same package.

2. **Why might `assertIn` be a better choice in testing the text in responses than `assertEqual`?**

   - `assertIn` checks for the presence of a substring, making tests less brittle to formatting changes or extra content. `assertEqual` requires an exact match, which can fail if the response contains additional HTML or whitespace.

3. **Views, View Configuration, and Debugging View Configuration**
   - Views are functions that handle requests. Configuration can be done imperatively (`config.add_view`) or declaratively (`@view_config`). Debugging view configuration is easier with decorators and scanning, as it keeps view logic and registration together.

---

# 08: HTML Generation With Templating Analysis

## Background Summary

Most web frameworks avoid embedding HTML directly in code. Instead, they use a templating system to generate HTML. Pyramid encourages replaceability and does not mandate a specific template language, but supports Jinja2, Mako, and Chameleon. In this step, we use `pyramid_chameleon` to render HTML from template files.

## Key Components Analysis

### 1. Enable pyramid_chameleon

Add `pyramid_chameleon` to `install_requires` in `setup.py`:

```python
requires = [
    'pyramid',
    'pyramid_chameleon',
    'waitress',
]
```

Include it in the configurator in `tutorial/__init__.py`:

```python
def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()
```

### 2. Views Use Renderers

Move HTML out of views and use templates:

```python
from pyramid.view import view_config

@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'name': 'Home View'}

@view_config(route_name='hello', renderer='home.pt')
def hello(request):
    return {'name': 'Hello View'}
```

### 3. Template File (`home.pt`)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Quick Tutorial: ${name}</title>
  </head>
  <body>
    <h1>Hi ${name}</h1>
  </body>
</html>
```

### 4. Development Configuration

Set `pyramid.reload_templates = true` in `development.ini` for auto-reloading templates.

### 5. Updated Tests

Unit tests now check returned data, not HTML:

```python
def test_home(self):
    from .views import home
    request = testing.DummyRequest()
    response = home(request)
    self.assertEqual('Home View', response['name'])

def test_hello(self):
    from .views import hello
    request = testing.DummyRequest()
    response = hello(request)
    self.assertEqual('Hello View', response['name'])
```

Functional tests check rendered HTML:

```python
def test_home(self):
    res = self.testapp.get('/', status=200)
    self.assertIn(b'<h1>Hi Home View', res.body)

def test_hello(self):
    res = self.testapp.get('/howdy', status=200)
    self.assertIn(b'<h1>Hi Hello View', res.body)
```

## Analysis

- Views now focus on returning data, not HTML.
- The `@view_config` decorator specifies a renderer (template file).
- Both views use the same template.
- Tests focus on data contracts for unit tests and HTML output for functional tests.

## Extra Notes

- Templates are easier to debug and maintain.
- Pyramid supports multiple template systems via add-ons.
- You can switch template engines as needed.

Templates, Debugging Templates, and Available Add-On Template System Bindings.

---

# 09: Organizing Views With View Classes

## Background

So far our views have been simple, free-standing functions. Many times your views are related to one another. They may consist of different ways to look at or work on the same data, or be a REST API that handles multiple operations. Grouping these views together as a view class makes sense:

- Group views.
- Centralize some repetitive defaults.
- Share some state and helpers.

In this step we just do the absolute minimum to convert the existing views to a view class. In a later tutorial step, we'll examine view classes in depth.

## Objectives

- Group related views into a view class.
- Centralize configuration with class-level `@view_defaults`.

## Steps

First, copy the results of the previous step:

```bash
cd ..; cp -r templating view_classes; cd view_classes
$VENV/bin/pip install -e .
```

Our `view_classes/tutorial/views.py` now has a view class with our two views:

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}
```

Our unit tests in `view_classes/tutorial/tests.py` don't run, so let's modify them to import the view class, and make an instance before getting a response:

```python
import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.hello()
        self.assertEqual('Hello View', response['name'])

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<h1>Hi Hello View', res.body)
```

Now run the tests:

```bash
$VENV/bin/pytest tutorial/tests.py -q
....
4 passed in 0.34 seconds
```

Run your Pyramid application with:

```bash
$VENV/bin/pserve development.ini --reload
```

Open http://localhost:6543/ and http://localhost:6543/howdy in your browser.

## Analysis

To ease the transition to view classes, we didn't introduce any new functionality. We simply changed the view functions to methods on a view class, then updated the tests.

In our `TutorialViews` view class, you can see that our two view functions are logically grouped together as methods on a common class. Since the two views shared the same template, we could move that to a `@view_defaults` decorator at the class level.

The tests needed to change. Obviously we needed to import the view class. But you can also see the pattern in the tests of instantiating the view class with the dummy request first, then calling the view method being tested.

## Defining a View Callable as a Class

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}
```

- `view_config`: Decorator to configure views
- `view_defaults`: Class-level decorator for shared configuration
- `TutorialViews`: View class to group related views
- `__init__(self, request)`: Constructor to initialize request
- `home(self)`: Method to handle home view
- `hello(self)`: Method to handle hello view

**Benefits:**

- Group related views
- Centralize configuration
- Share state and helpers

**Next Steps:**

- Explore view classes in depth
- Learn about class-based views, view methods, and advanced patterns

---

# 10: Handling Web Requests and Responses

Web applications handle incoming requests and return outgoing responses. Pyramid makes working with requests and responses convenient and reliable.

## Objectives

- Learn the background on Pyramid's choices for requests and responses.
- Grab data out of the request.
- Change information in the response headers.

## Background

Developing for the web means processing web requests. As this is a critical part of a web application, web developers need a robust, mature set of software for web requests and returning web responses.

Pyramid has always fit nicely into the existing world of Python web development (virtual environments, packaging, cookiecutters, first to embrace Python 3, and so on). Pyramid turned to the well-regarded WebOb Python library for request and response handling. In our example above, Pyramid hands hello_world a request that is based on WebOb.

## Steps

First we copy the results of the view_classes step:

```bash
cd ..; cp -r view_classes request_response; cd request_response
$VENV/bin/pip install -e .
```

Simplify the routes in `request_response/tutorial/__init__.py`:

```python
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('plain', '/plain')
    config.scan('.views')
    return config.make_wsgi_app()
```

We just need one view in `request_response/tutorial/views.py`:

```python
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return HTTPFound(location='/plain')

    @view_config(route_name='plain')
    def plain(self):
        name = self.request.params.get('name', 'No Name Provided')

        body = 'URL %s with name: %s' % (self.request.url, name)
        return Response(
            content_type='text/plain',
            body=body
        )
```

Update the tests in `request_response/tutorial/tests.py`:

```python
import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual(response.status, '302 Found')

    def test_plain_without_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'No Name Provided', response.body)

    def test_plain_with_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.GET['name'] = 'Jane Doe'
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'Jane Doe', response.body)

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_plain_without_name(self):
        res = self.testapp.get('/plain', status=200)
        self.assertIn(b'No Name Provided', res.body)

    def test_plain_with_name(self):
        res = self.testapp.get('/plain?name=Jane%20Doe', status=200)
        self.assertIn(b'Jane Doe', res.body)
```

Now run the tests:

```bash
$VENV/bin/pytest tutorial/tests.py -q
.....
5 passed in 0.30 seconds
```

Run your Pyramid application with:

```bash
$VENV/bin/pserve development.ini --reload
```

Open http://localhost:6543/ in your browser. You will be redirected to http://localhost:6543/plain.

Open http://localhost:6543/plain?name=alice in your browser.

## Analysis

In this view class, we have two routes and two views, with the first leading to the second by an HTTP redirect. Pyramid can generate redirects by returning a special object from a view or raising a special exception.

In this Pyramid view, we get the URL being visited from `request.url`. Also, if you visited http://localhost:6543/plain?name=alice, the name is included in the body of the response:

```
URL http://localhost:6543/plain?name=alice with name: alice
```

Finally, we set the response's content type and body, then return the response.

We updated the unit and functional tests to prove that our code does the redirection, but also handles sending and not sending `/plain?name`.

## Extra credit

Could we also raise `HTTPFound(location='/plain')` instead of returning it? If so, what's the difference?

- Yes, you can either return or raise `HTTPFound`. Returning it is more common in Pyramid, but raising works as well. Raising is useful if you want to interrupt processing and immediately redirect, especially in more complex logic.

Request and Response Objects, generate redirects

# 11: Dispatching URLs To Views With Routing

Routing matches incoming URL patterns to view code. Pyramid's routing has a number of useful features.

## Background

Writing web applications usually means sophisticated URL design. We just saw some Pyramid machinery for requests and views. Let's look at features that help in routing.

Previously we saw the basics of routing URLs to views in Pyramid.

- Your project's "setup" code registers a route name to be used when matching part of the URL
- Elsewhere a view is configured to be called for that route name.

Why do this twice? Other Python web frameworks let you create a route and associate it with a view in one step. As illustrated in Routes need relative ordering, multiple routes might match the same URL pattern. Rather than provide ways to help guess, Pyramid lets you be explicit in ordering. Pyramid also gives facilities to avoid the problem. It's relatively easy to build a system that uses implicit route ordering with Pyramid too. See The Groundhog series of screencasts if you're interested in doing so.

## Objectives

- Define a route that extracts part of the URL into a Python dictionary.
- Use that dictionary data in a view.

## Steps

First we copy the results of the view_classes step:

```bash
cd ..; cp -r view_classes routing; cd routing
$VENV/bin/pip install -e .
```

Our `routing/tutorial/__init__.py` needs a route with a replacement pattern:

```python
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/howdy/{first}/{last}')
    config.scan('.views')
    return config.make_wsgi_app()
```

We just need one view in `routing/tutorial/views.py`:

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return {
            'name': 'Home View',
            'first': first,
            'last': last
        }
```

We just need one template in `routing/tutorial/home.pt`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${name}</title>
</head>
<body>
<h1>${name}</h1>
<p>First: ${first}, Last: ${last}</p>
</body>
</html>
```

Update `routing/tutorial/tests.py`:

```python
import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.matchdict['first'] = 'First'
        request.matchdict['last'] = 'Last'
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual(response['first'], 'First')
        self.assertEqual(response['last'], 'Last')

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/howdy/Jane/Doe', status=200)
        self.assertIn(b'Jane', res.body)
        self.assertIn(b'Doe', res.body)
```

Now run the tests:

```bash
$VENV/bin/pytest tutorial/tests.py -q
..
2 passed in 0.39 seconds
```

Run your Pyramid application with:

```bash
$VENV/bin/pserve development.ini --reload
```

Open http://localhost:6543/howdy/amy/smith in your browser.

## Analysis

In `__init__.py` we see an important change in our route declaration:

```python
config.add_route('hello', '/howdy/{first}/{last}')
```
With this we tell the configurator that our URL has a "replacement pattern". With this, URLs such as `/howdy/amy/smith` will assign `amy` to `first` and `smith` to `last`. We can then use this data in our view:

```python
self.request.matchdict['first']
self.request.matchdict['last']
```
`request.matchdict` contains values from the URL that match the "replacement patterns" (the curly braces) in the route declaration. This information can then be used anywhere in Pyramid that has access to the request.

## Extra credit

What happens if you go to the URL http://localhost:6543/howdy? Is this the result that you expected?

- You will get a 404 Not Found error, because the route expects both `first` and `last` segments in the URL. This is expected: Pyramid only matches the route if all required segments are present.

Weird Stuff You Can Do With URL Dispatch

# 12: Templating With jinja2

We just said Pyramid doesn't prefer one templating language over another. Time to prove it. Jinja2 is a popular templating system, used in Flask and modeled after Django's templates. Let's add `pyramid_jinja2`, a Pyramid add-on which enables Jinja2 as a renderer in our Pyramid applications.

## Objectives

- Show Pyramid's support for different templating systems.
- Learn about installing Pyramid add-ons.

## Steps

In this step let's start by copying the view_class step's directory from a few steps ago.

```bash
cd ..; cp -r view_classes jinja2; cd jinja2
```

Add `pyramid_jinja2` to our project's dependencies in `setup.py`:

```python
from setuptools import setup

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_jinja2',
    'waitress',
]

# List of dependencies installed via `pip install -e ".[dev]"`
# by virtue of the Setuptools `extras_require` value in the Python
# dictionary below.
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

Install our project and its newly added dependency.

```bash
$VENV/bin/pip install -e .
```

We need to include `pyramid_jinja2` in `jinja2/tutorial/__init__.py`:

```python
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()
```

Our `jinja2/tutorial/views.py` simply changes its renderer:

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}
```

Add `jinja2/tutorial/home.jinja2` as a template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: {{ name }}</title>
</head>
<body>
<h1>Hi {{ name }}</h1>
</body>
</html>
```

Now run the tests:

```bash
$VENV/bin/pytest tutorial/tests.py -q
....
4 passed in 0.40 seconds
```

Run your Pyramid application with:

```bash
$VENV/bin/pserve development.ini --reload
```

Open http://localhost:6543/ in your browser.

## Analysis

Getting a Pyramid add-on into Pyramid is simple. First you use normal Python package installation tools to install the add-on package into your Python virtual environment. You then tell Pyramid's configurator to run the setup code in the add-on. In this case the setup code told Pyramid to make a new "renderer" available that looked for `.jinja2` file extensions.

Our view code stayed largely the same. We simply changed the file extension on the renderer. For the template, the syntax for Chameleon and Jinja2's basic variable insertion is very similar.

## Extra credit

- Our project now depends on `pyramid_jinja2`. We installed that dependency manually. What is another way we could have made the association?
  - By adding it to `install_requires` in `setup.py` and running `pip install -e .`, the dependency is installed automatically.

- We used `config.include` which is an imperative configuration to get the Configurator to load `pyramid_jinja2`'s configuration. What is another way we could include it into the config?
  - By adding `pyramid_jinja2` to the `pyramid.includes` setting in the `.ini` file, you can include it declaratively.

Jinja2 homepage, and pyramid_jinja2 Overview

---

# 13: CSS/JS/Images Files With Static Assets

Of course the Web is more than just markup. You need static assets: CSS, JS, and images. Let's point our web app at a directory where Pyramid will serve some static assets.

## Objectives

- Publish a directory of static assets at a URL.
- Use Pyramid to help generate URLs to files in that directory.

## Steps

First we copy the results of the view_classes step:

```bash
cd ..; cp -r view_classes static_assets; cd static_assets
$VENV/bin/pip install -e .
```

We add a call `config.add_static_view` in `static_assets/tutorial/__init__.py`:

```python
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_static_view(name='static', path='tutorial:static')
    config.scan('.views')
    return config.make_wsgi_app()
```

We can add a CSS link in the `<head>` of our template at `static_assets/tutorial/home.pt`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${name}</title>
    <link rel="stylesheet"
          href="${request.static_url('tutorial:static/app.css') }"/>
</head>
<body>
<h1>Hi ${name}</h1>
</body>
</html>
```

Add a CSS file at `static_assets/tutorial/static/app.css`:

```css
body {
    margin: 2em;
    font-family: sans-serif;
}
```

We add a functional test that asserts that the newly added static file is delivered:

```python
def test_css(self):
    res = self.testapp.get('/static/app.css', status=200)
    self.assertIn(b'body', res.body)
```

Now run the tests:

```bash
$VENV/bin/pytest tutorial/tests.py -q
....
5 passed in 0.50 seconds
```

Run your Pyramid application with:

```bash
$VENV/bin/pserve development.ini --reload
```

Open http://localhost:6543/ in your browser and note the new font.

## Analysis

We changed our WSGI application to map requests under http://localhost:6543/static/ to files and directories inside a static directory inside our tutorial package. This directory contained `app.css`.

We linked to the CSS in our template. We could have hard-coded this link to `/static/app.css`. But what if the site is later moved under `/somesite/static/`? Or perhaps the web developer changes the arrangement on disk? Pyramid gives a helper that provides flexibility on URL generation:

```
${request.static_url('tutorial:static/app.css')}
```
This matches the `path='tutorial:static'` in our `config.add_static_view` registration. By using `request.static_url` to generate the full URL to the static assets, you both ensure you stay in sync with the configuration and gain refactoring flexibility later.

## Extra credit

There is also a `request.static_path` API. How does this differ from `request.static_url`?

- `request.static_url` generates a full URL (including scheme, host, and path) to the static asset, suitable for use in HTML templates.
- `request.static_path` generates only the path portion (e.g., `/static/app.css`), which can be useful in some contexts where only the path is needed.

Static Assets, Preventing HTTP Caching, and Influencing HTTP Caching

---

# 14: AJAX Development Analysis

(Coming Soon)

## Key Components Analysis

### 1. AJAX Requests

(To be filled)

### 2. JSON Responses

(To be filled)

---

# 15: Advanced View Classes Analysis

(Coming Soon)

## Key Components Analysis

### 1. Advanced Patterns

(To be filled)

### 2. View Decorators

(To be filled)

---

# 16: Logging Analysis

(Coming Soon)

## Key Components Analysis

### 1. Logging Configuration

(To be filled)

### 2. Log Levels

(To be filled)

---

# 17: Sessions Analysis

(Coming Soon)

## Key Components Analysis

### 1. Session Management

(To be filled)

### 2. Session Storage

(To be filled)

---

# 18: Forms and Validation Analysis

(Coming Soon)

## Key Components Analysis

### 1. Form Handling

(To be filled)

### 2. Validation Rules

(To be filled)

---

# 19: SQLAlchemy Databases Analysis

(Coming Soon)

## Key Components Analysis

### 1. Database Models

(To be filled)

### 2. ORM Operations

(To be filled)

---

# 20: Authentication Analysis

(Coming Soon)

## Key Components Analysis

### 1. Authentication Setup

(To be filled)

### 2. User Management

(To be filled)

---

# 21: Authorization Analysis

(Coming Soon)

## Key Components Analysis

### 1. Permission System

(To be filled)

### 2. Access Control

(To be filled)
