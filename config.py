import os

SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

app.config["SQLALCHEMY_DATABASE_URI"] = postgresql://mystorydb_user:PzW57YczDpJJH2ZNtgAv5p9SGOjWOLvK@dpg-cl9u48e2eqrc7393hn40-a/mystorydb