# 16: Collecting Application Info With Logging Analysis

## Analysis

- Uses standard Python logging module
- Configuration defined in development.ini
- Debug toolbar integrates logging output
- Messages can be filtered by level (DEBUG, INFO, etc.)
- Logs show timestamp, level, module, and thread information

## Extra Credit Answers

1. What's the difference between root logger and tutorial logger?

   - Root logger: Parent logger for all loggers, catches all unhandled messages
   - Tutorial logger: Specific to the tutorial package, can have different settings

2. What are the logging levels in order of severity?

   - DEBUG: Detailed information for debugging
   - INFO: General information about program execution
   - WARNING: Indicate a potential problem
   - ERROR: A more serious problem
   - CRITICAL: Program may not be able to continue

3. How do handler and formatter work together?

   - Handler: Determines where log messages go (console, file, etc.)
   - Formatter: Determines how log messages look (timestamp, level, etc.)

4. Why use **name** for the logger?
   - Creates logger with module's name
   - Enables hierarchical logging configuration
   - Makes it easy to filter logs by module