def configure_app():
    import os
    import dotenv
    import flask

    from flask import Flask
    app = Flask(__name__)

    PROJECT_ROOT = os.path.abspath('.')
    env_path = os.path.join(PROJECT_ROOT, '.env')
    dotenv.load_dotenv(env_path)

    return

    
app = configure_app()
