from flask import Flask

test = Flask(__name__)
@test.route('/')
def hello_world():
    return 'hello test 123'
if __name__ == '__main__':
    test.run()
