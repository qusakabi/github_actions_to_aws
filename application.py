from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello from AWS Elastic Beanstalk via GitHub Actions! 🚀"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)