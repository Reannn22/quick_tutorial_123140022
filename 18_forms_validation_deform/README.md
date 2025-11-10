# 18: Forms and Validation with Deform Analysis

## Analysis

- Uses Deform library for form generation and validation
- Colander schemas define form structure and validation rules
- Forms support rich widgets like WYSIWYG editors
- Self-posting forms pattern for handling GET/POST
- Static assets managed through asset specifications

## Extra Credit Answers

1. **How do self-posting forms work?**

   - Same URL handles both GET and POST requests
   - GET displays empty form, POST processes submission
   - Validation errors redisplay form with error messages
   - Successful submission redirects to new page

2. **What is the role of Colander schemas?**

   - Define form field types and validation rules
   - Map form data to Python objects
   - Support custom widgets and validators
   - Enable reuse of validation logic

3. **How does Deform handle static assets?**

   - Uses asset specifications to locate resources
   - Automatically includes required CSS/JS
   - Manages dependencies between widgets
   - Provides resource registry for custom widgets

4. **What is the form validation pattern?**

   - Check if form was submitted (POST)
   - Validate form data against schema
   - Re-render form if validation fails
   - Process data and redirect if valid

5. **Why use widget resources?**

   - Ensures required CSS/JS is loaded
   - Manages dependencies between widgets
   - Provides consistent styling
   - Supports rich UI components