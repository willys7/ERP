pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    ExampleENV="${WORKSPACE}"/.ExampleENV
                    if [ -d "$ExampleENV" ]; then
                    rm -fr "$ExampleENV"
                    fi
                    virtualenv --no-site-packages "$ExampleENV"
                    . "$ExampleENV"/bin/activate
                    ls
                    cd ERP
                    ls
                    pip install -r requirements.txt
                    python manage.py migrate
                    python manage.py test
                   '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                echo 'dummy change'
                sh 'docker-compose up'
            }
        }
    }
}
