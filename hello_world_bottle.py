from bottle import route, run, template

'''Starter code from Bottle, go to localhost:8080 and change the url to "localhost:8080/hello/<NAME>"  '''

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8081)