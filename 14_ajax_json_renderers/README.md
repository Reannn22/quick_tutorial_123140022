# 14: AJAX Development With JSON Renderers

## Analysis

- JSON renderers convert Python data to JSON and set the response content type
- Pyramid provides a built-in JSON renderer, and custom renderers can be created
- AJAX views can be easily implemented using JSON renderers

## Extra Credit Answers

1. **What is the purpose of the JSON renderer?**

   - Converts Python data to JSON format.
   - Sets the response content type to `application/json`.

2. **How do you define a view that returns JSON?**

   - Use the `@view_config` decorator with the `renderer='json'` option.
   - Return a Python dictionary or list from the view.

3. **What are the benefits of using JSON for AJAX responses?**

   - Lightweight and easy to parse in JavaScript.
   - Native support in Python with the `json` module.
   - Can represent complex data structures.

4. **How can you customize the JSON rendering process?**

   - By extending the built-in JSON renderer or creating a custom renderer.
   - Can define custom serialization logic for specific types.

5. **What is the difference between `json.dumps` and `json.dump`?**

   - `json.dumps`: Serializes an object to a JSON formatted string.
   - `json.dump`: Serializes an object and writes it to a file-like object.