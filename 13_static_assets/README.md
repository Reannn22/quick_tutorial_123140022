# 13: CSS/JS/Images Files With Static Assets

## Analysis

- Static assets like CSS, JS, and images can be served by Pyramid
- `add_static_view` method maps a URL path to a directory of static files
- `request.static_url` helper generates URLs to static assets

## Extra Credit Answers

1. **What is the purpose of the `add_static_view` method?**

   - Maps a URL path to a directory of static files.
   - Serves static assets like CSS, JS, and images.

2. **How do you link to a static file in a template?**

   - Use the `request.static_url` helper to generate the URL.
   - Example: `<link rel="stylesheet" href="${request.static_url('tutorial:static/app.css') }"/>`.

3. **What is the difference between `request.static_url` and `request.static_path`?**

   - `request.static_url`: Generates a full URL (including scheme, host, and path) to the static asset.
   - `request.static_path`: Generates only the path portion (e.g., `/static/app.css`).

4. **How can you prevent caching of static assets by the browser?**

   - Set appropriate cache control headers in the response.
   - Use versioned URLs for static assets.

5. **What are some best practices for managing static assets in a web application?**

   - Organize assets in a logical directory structure.
   - Use versioning or hashing in filenames to manage caching.
   - Minify and concatenate assets for production.
