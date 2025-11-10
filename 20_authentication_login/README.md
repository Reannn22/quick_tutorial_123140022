# 20: Logins with Authentication Analysis

## Analysis

- Uses bcrypt for secure password hashing
- Authentication policy manages user identity
- Cookie-based authentication via AuthTktCookieHelper
- Login/logout views handle user sessions
- Configuration-driven security settings

## Extra Credit Answers

1. **Can database authentication replace in-memory USERS?**

   - Yes, replace USERS dictionary with database queries
   - Use SQLAlchemy models for user storage
   - Hash passwords before storing in database
   - Maintain same security interface

2. **What user information is available per request?**

   - request.authenticated_userid contains user ID
   - Security policy adds identity to request
   - Session can store additional user data
   - Debug with pdb to inspect request attributes

3. **How does the security policy work?**

   - Implements authentication interface
   - Manages cookie-based user sessions
   - Validates user credentials
   - Provides remember/forget functionality

4. **Why use bcrypt for passwords?**

   - One-way hashing with salt
   - Industry-standard password security
   - Protects against rainbow table attacks
   - Configurable work factor for security

5. **What's the role of security configuration?**

   - Defines secret key for cookie signing
   - Configures authentication policy
   - Sets up security routes
   - Separates security from code