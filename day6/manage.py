import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get("FLASK", 'develop')
app = create_app(env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
