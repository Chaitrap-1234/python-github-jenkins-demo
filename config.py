import os

def get_message():

    app_name = os.getenv("APP_NAME", "Unknown App")
    environment = os.getenv("ENVIRONMENT", "Development")
    owner = os.getenv("OWNER", "Unknown")

    return f"""
Application : {app_name}
Environment : {environment}
Owner       : {owner}
"""
