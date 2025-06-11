# app.py
from flask import Flask, render_template_string
import os

# Initialize the Flask application
app = Flask(__name__)

# Basic HTML template for the web page
# This template will display the greeting message from an environment variable.
# It also includes a confirmation message about HTTPS.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Greeting App</title>
    <!-- Tailwind CSS CDN for basic styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom styles for the app */
        body {
            font-family: 'Inter', sans-serif; /* Using Inter font */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Full viewport height */
            background-color: #f0f4f8; /* Light background color */
            color: #334155; /* Default text color */
        }
        .container {
            background-color: #ffffff; /* White container background */
            padding: 2.5rem; /* Ample padding */
            border-radius: 1rem; /* Rounded corners for the container */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* Soft shadow */
            text-align: center; /* Center align text */
            max-width: 90%; /* Max width for responsiveness */
            width: 500px; /* Fixed width for larger screens */
        }
        h1 {
            color: #1e293b; /* Darker heading color */
            margin-bottom: 1.5rem; /* Space below heading */
            font-weight: 800; /* Extra bold */
            font-size: 2.5rem; /* Larger font size */
        }
        p {
            color: #475569; /* Paragraph text color */
            line-height: 1.6; /* Improved readability */
            font-size: 1.25rem; /* Larger paragraph font */
            font-style: italic; /* Italic for the greeting */
        }
        .secure-note {
            margin-top: 2rem; /* Space above note */
            font-size: 0.9rem; /* Smaller font for note */
            color: #64748b; /* Grey text for note */
            background-color: #e2e8f0; /* Light background for note */
            padding: 0.75rem; /* Padding for note */
            border-radius: 0.5rem; /* Rounded corners for note */
            border-left: 4px solid #3b82f6; /* Blue left border for emphasis */
        }
        /* Responsive adjustments */
        @media (max-width: 640px) {
            .container {
                padding: 1.5rem;
            }
            h1 {
                font-size: 2rem;
            }
            p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Secure App!</h1>
        <p>"{{ greeting_message }}"</p>
        <div class="secure-note">
            This application is designed to be served securely over HTTPS.
            Please check your browser's address bar for the padlock icon!
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """
    Renders the home page of the application.
    It retrieves the 'GREETING_MESSAGE' from environment variables.
    """
    # Attempt to retrieve the greeting message from environment variables.
    # If the variable is not found (e.g., during local testing without Key Vault setup),
    # a default message is used. This is useful for debugging.
    greeting_message = os.environ.get('GREETING_MESSAGE', 'Default Message: Secure greeting not yet configured or loaded from Key Vault.')
    
    # Render the HTML template, passing the greeting message.
    return render_template_string(HTML_TEMPLATE, greeting_message=greeting_message)

if __name__ == '__main__':
    # Run the Flask application.
    # The host '0.0.0.0' makes the app accessible from any IP address (important for Docker/App Service).
    # The port is taken from the 'PORT' environment variable if available, otherwise defaults to 5000.
    # debug=True enables debugging features (e.g., auto-reloading, interactive debugger)
    # but should be set to False in production environments for security.
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
