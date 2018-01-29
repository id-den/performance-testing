pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Clone..'
                checkout scm
            }
        }
        stage('Performance Tests') {
            steps {
                parallel(
                    "Running test via Taurus": {
                         bzt "load_tests/simple_taurus.yml -o modules.console.disable=true modules.blazemeter.token=8rxaqrrwnbfmg1iwsw17 -report"
                    },
                    "Running test via Locust": {
                        sh "locust -f load_tests/locust_test.py --host=https://performance-testing.jimdo.com --no-web -c 10 -n10"
                    },
                    "Running test via Selenium": {
                        bzt "load_tests/simple_selenium.yml" 
                    }       
                )
            }
        }
        stage('Results') {
            steps {
                echo 'Results....'
            }
        }
    }
}