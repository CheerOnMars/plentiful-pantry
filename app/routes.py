from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Super Sario'}
    return '''
<html>
    <head>
        <title>Home Page - Plentiful Pantry</title>
    </head>
    <body>
        <h1>Plentiful Pantry:  ''' + user['username'] + '''!</h1>
    </body>
</html>'''
