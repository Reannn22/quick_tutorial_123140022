# 11: Dispatching URLs To Views With Routing

## Analysis

- Routing matches incoming URLs to the appropriate view based on configuration
- Pyramid allows explicit ordering of routes to avoid ambiguity
- Route patterns can extract parts of the URL as parameters

## Extra Credit Answers

1. **What is the purpose of the `add_route` method?**

   - Registers a new route with a name and pattern.
   - Associates the route with a specific view or view class.

2. **How does Pyramid match incoming URLs to routes?**

   - Compares the incoming URL against the registered route patterns.
   - Extracts parameters from the URL based on the pattern.

3. **What is the role of the `matchdict` attribute in the request?**

   - Contains the extracted parameters from the matched route.
   - Accessible in the view through `request.matchdict`.

4. **How can you define optional parameters in a route pattern?**

   - By using a question mark `?` after the parameter name in the pattern.
   - Example: `/howdy/{first}/{last}?` makes `last` optional.

5. **What happens if no route matches the incoming URL?**

   - Pyramid returns a 404 Not Found response.
   - The request is passed to the next application in the WSGI stack, if any.