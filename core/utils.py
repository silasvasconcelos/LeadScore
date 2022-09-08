import os

import environ

root = environ.Path(__file__) - 2  # get root of the project
SITE_ROOT = root()
env = environ.Env()
env_file = root('.env')
if os.path.exists(env_file):
    environ.Env.read_env(env_file=env_file)  # reading .env file
else:
    print(
        f"""File .env cann\'t be found in: {env_file}.\nWill try to load from the system variables!""")
