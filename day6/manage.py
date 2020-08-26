import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get("FLASK_ENV", 'develop')  # 获取环境变量  后一个参数是默认值
app = create_app(env=env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
