# 03: Application Configuration Analysis

## Analysis

- Configuration separated from code
- Uses .ini files for settings
- Entry points define application behavior
- pserve command bootstraps the app

## Extra Credit Answers

1. **What is the role of `global_config` in the `main` function?**

   - `global_config` is a placeholder for global settings, rarely used in practice.
   - Allows passing of configuration options from the .ini file.
   - Can be ignored if not needed.

2. **How are settings passed from .ini file to the application?**

   - Via `**settings` in the `main` function signature.
   - Unpacked as keyword arguments in `Configurator`.
   - Available as `settings` in the application.

3. **What is the purpose of the `entry_points` in setup.py?**

   - Defines entry points for the application.
   - Tells Pyramid where to find the WSGI application factory.
   - Used by the `pserve` command to bootstrap the app.

4. **How does Pyramid find the WSGI application factory?**

   - Looks for the `main` function in the specified module.
   - The module is determined by the `entry_points` in setup.py.
   - Default is `tutorial:main` for the `tutorial` package.

5. **What is the effect of the `use` directive in the .ini file?**

   - Specifies the application and server to use.
   - `egg:tutorial` refers to the installed package entry point.
   - `egg:waitress#main` specifies Waitress as the WSGI server.