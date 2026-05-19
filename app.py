from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''CI/CD Pipeline Success!!!...

    A CI/CD pipeline in Jenkins automates the process of building, testing, and deploying code.
    It helps developers integrate changes and deploy them quickly and reliably. Jenkins makes 
    this automation easy and efficient.

    1. Defines pipelines in a Jenkinsfile for version-controlled build, test, and deploy steps.
    2. Breaks workflows into automated stages like build, test, and deploy.
    3. Triggers runs on code commits to provide quick feedback.
    4. Uses agents for parallel and scalable execution.'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
