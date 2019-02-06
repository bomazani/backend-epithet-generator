def configure_app():
    import os
    import dotenv
    import flask

    from flask import Flask
    app = Flask(__name__)

    PROJECT_ROOT = os.path.dirname(".")
    # PROJECT_ROOT = os.path.abspath('.') ?????
    
    # Use dotenv.load_dotenv(), os.path.join(), and the PROJECT_ROOT variable to load environment variables automatically from the .env file.
    dotenv.load_dotenv(os.path.abspath('.'))
    # dotenv.load_dotenv(PROJECT_ROOT) ?????

    # Instantiate and return an instance of Flask from the configure_app function.

    # Use the configure_app function to assign an instance of the Flask application to a variable labeled app.
app = configure_app()
