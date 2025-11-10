# 09: Organizing Views With View Classes

## Analysis

- View classes group related views and share configuration
- Class-level `@view_defaults` decorator sets defaults for all views in the class
- URL pattern handling and view predicates enable flexible routing

## Extra Credit Answers

1. **What is the purpose of the `@view_defaults` decorator?**

   - Sets default options for all views in the class, such as renderer and route name.

2. **How does the view class share state between views?**

   - Through instance variables set in the constructor (`__init__` method) of the view class.

3. **What is the role of the `full_name` property in the view class?**

   - Encapsulates the logic for constructing the full name from URL parameters.
   - Available to all views and templates as an attribute.

4. **How do view predicates work?**

   - View predicates are conditions that must be met for a view to be called.
   - Can match on request method, parameters, headers, and other attributes.

5. **What is the difference between `route_path` and `route_url`?**

   - `route_path`: Returns the path of the URL (e.g., `/howdy/First/Last`).
   - `route_url`: Returns the full URL, including scheme and host (e.g., `http://localhost:6543/howdy/First/Last`).
