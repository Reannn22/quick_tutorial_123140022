# 10: Handling Web Requests and Responses

## Analysis

- Request and response handling is based on the WebOb library
- Request parameters are accessed through `request.params`
- Response headers and body can be modified before returning the response

## Extra Credit Answers

1. **What is the role of the `request` object in a view?**

   - Represents the incoming HTTP request.
   - Provides access to request parameters, headers, and other attributes.

2. **How do you access query parameters in a view?**

   - Through the `request.params` dictionary-like object.
   - Example: `name = request.params.get('name')`.

3. **What is the purpose of the `Response` class?**

   - Represents the HTTP response to be sent to the client.
   - Allows setting the response status, headers, and body.

4. **How can you modify the response headers?**

   - By setting attributes on the `Response` object.
   - Example: `response.headers['X-Custom-Header'] = 'Value'`.

5. **What is the difference between `HTTPFound` and `Response`?**

   - `HTTPFound` is a subclass of `Response` for HTTP 302 redirects.
   - Use `HTTPFound` to redirect to a different URL.
