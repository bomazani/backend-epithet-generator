def configure_app():
    import os
    import dotenv
    import flask

    # from dotenv import load_dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.abspath('.')
    env_path = os.path.join(PROJECT_ROOT, '.env')
    dotenv.load_dotenv(env_path)

    app = Flask(__name__)


    return app

    
app = configure_app()
