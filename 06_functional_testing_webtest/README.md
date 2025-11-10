# 06: Functional Testing Analysis

## Analysis

- Functional tests verify the application as a whole, including routing and view integration
- WebTest is used to simulate HTTP requests and inspect responses
- Test organization and structure are important for maintainability

## Extra Credit Answers

1. **What is the difference between unit tests and functional tests?**

   - Unit tests verify individual components in isolation, while functional tests verify the application as a whole.
   - Functional tests check the interaction between components and the correctness of workflows.

2. **Why do we need to add webtest as a development dependency?**

   - WebTest is not included in the standard library, so it must be added as a dependency.
   - It provides a way to simulate HTTP requests and inspect responses for functional testing.

3. **How do you run the functional tests for the application?**

   - Use the command `pytest` in the terminal, same as for unit tests.
   - Can specify options like `--cov` for coverage reporting.
   - Integrate with CI/CD pipelines for automated testing.

4. **What is the significance of the `DummyRequest` in the tests?**

   - `DummyRequest` is a test double that simulates an HTTP request.
   - Allows testing of views and routes without starting a real server.
   - Can be customized with parameters, headers, and other request attributes.

5. **How can you test different scenarios for a view function in functional tests?**

   - Use different request parameters or headers in the tests.
   - Mock dependencies or services used by the view.
   - Assert on the response status, headers, and body content.