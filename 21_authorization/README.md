# 21: Protecting Resources With Authorization Analysis

## Analysis

- Access Control Lists (ACLs) define permissions on resources
- Security policies determine user permissions
- Root factory provides context for authorization
- Forbidden views handle unauthorized access
- Groups and principals manage user roles

## Extra Credit Answers

1. **What's the difference between user and principal?**

   - User: Authenticated identity (e.g., 'editor')
   - Principal: Security token (e.g., 'group:editors', Everyone)
   - Users can have multiple principals
   - Principals determine permissions

2. **Can database replace GROUPS data store?**

   - Yes, query database for user groups
   - Cache results for performance
   - Update effective_principals method
   - Maintain same authorization interface

3. **Is renderer required for @forbidden_view_config?**

   - No, can return any response
   - Renderer helps with error page templates
   - Can customize forbidden response
   - Common to show login form

4. **How to enhance forbidden experience?**

   - Custom error templates
   - Clear error messages
   - Alternative authentication options
   - Redirect to appropriate pages

5. **How to store security in database?**

   - Create ACL models
   - Load permissions dynamically
   - Cache ACL lookups
   - Update via admin interface

6. **How to vary security by context?**

   - Different ACLs per resource type
   - Hierarchical permissions
   - Context-specific factories
   - URL-based security rules