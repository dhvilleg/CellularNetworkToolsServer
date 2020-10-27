from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'dbaarcotel'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qGbU$69amY7f'
app.config['MYSQL_DATABASE_DB'] = 'arcoteldb'
app.config['MYSQL_DATABASE_HOST'] = 'mydbintanciaarcotel.cbrxv1qpdujs.us-east-2.rds.amazonaws.com'
mysql.init_app(app)
