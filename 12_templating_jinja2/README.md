# 12: Templating With jinja2

## Analysis

- Jinja2 is a popular templating system that can be used with Pyramid
- Templates are defined in separate files with a `.jinja2` extension
- Template syntax is similar to Chameleon, with variable insertion using `{{ }}`

## Extra Credit Answers

1. **What is the purpose of the `pyramid_jinja2` package?**

   - Enables Jinja2 templating in Pyramid applications.
   - Must be installed and included in the configuration.

2. **How do you define a template in Jinja2?**

   - Create a file with a `.jinja2` extension and define the HTML structure with embedded Python expressions.

3. **What are the benefits of using a templating system?**

   - Separates presentation logic from business logic.
   - Improves code organization and maintainability.
   - Allows for easier testing and debugging.

4. **How can you switch between different template systems in Pyramid?**

   - Install the desired template system package (e.g., `pyramid_jinja2`).
   - Include it in the configuration and specify the template file extension.

5. **What is the difference between `render_template` and `render_to_response`?**

   - `render_template`: Renders a template and returns the result as a string.
   - `render_to_response`: Renders a template and returns a `Response` object.
