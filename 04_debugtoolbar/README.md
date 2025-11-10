# 04: Debug Toolbar Analysis

## Analysis

- Debug toolbar provides insights into requests, responses, and performance
- Integrates with Pyramid via configuration
- Setuptools extras used for optional dependencies

## Extra Credit Answers

1. **What is the purpose of `dev_requires` in setup.py?**

   - Lists development dependencies, like pyramid_debugtoolbar and pytest.
   - Installed with `pip install -e ".[dev]"`.
   - Keeps production environment clean.

2. **How do you install a package with extras using pip?**

   - Use the syntax `pip install -e ".[extra_name]"`.
   - Example: `pip install -e ".[dev]"` installs development dependencies.

3. **What is the difference between `pip install .` and `pip install -e .`?**

   - `pip install .` copies files to site-packages.
   - `pip install -e .` creates a symbolic link to the source code.
   - Editable installs reflect code changes immediately.

4. **How does the Debug Toolbar integrate with Pyramid?**

   - Configured via .ini file or programmatically in setup.py.
   - Provides a visual interface for debugging information.
   - Offers features like request/response inspection and SQL query analysis.

5. **What are the benefits of using `dev_requires` for development dependencies?**

   - Keeps production deployments smaller and faster.
   - Reduces security risks by not installing unnecessary packages.
   - Allows for a cleaner separation of concerns.