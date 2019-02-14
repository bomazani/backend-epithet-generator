import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print(f'PROJECT_ROOT: {PROJECT_ROOT}')
REPO_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
print(f'REPO_ROOT: {REPO_ROOT}')
RESOURCES_ROOT = os.path.join(REPO_ROOT, 'resources')
print(f'RESOURCES_ROOT: {RESOURCES_ROOT}')


def configure_app(proj_root):
    import dotenv
    import flask
    from flask import Flask

    env_path = os.path.join(proj_root, '.env')
    dotenv.load_dotenv(env_path)
    app = Flask(__name__)
    return app

app = configure_app(PROJECT_ROOT)
