from app import create_app,db
from app.models import User,Pitch,Comment
from flask_script._compat import text_type
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

#change from 'development to production' when deploying to heroku
# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,user=User,Pitch=Pitch, Comment=Comment)

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'naza123rena' #add secret key configaration
    manager.run()