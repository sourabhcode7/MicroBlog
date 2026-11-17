#!flask/bin/python
from app import app
app.run(debug=True)

# By default, it runs locally at:

# http://127.0.0.1:5000/

# debug=True

# This enables Flask's debug mode.

# It provides two important features:
# 1. Automatic reloading: When you modify your Python code, Flask automatically restarts the development server.
# 2. Debugging: When an error occurs, Flask displays a detailed debugging page in the browser.
#note it will still work without the debug = true