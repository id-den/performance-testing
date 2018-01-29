pipeline {
    stages { 
         stage('Build') {
            checkout scm
         }
         stage('Performance Tests') {
             steps {
                container('Running test via Taurus') {
                     bzt "load_tests/simple_taurus.yml -o modules.console.disable=true modules.blazemeter.token=8rxaqrrwnbfmg1iwsw17 -report"
                }
             }
             steps {
                 container ('Running test via Locust') {
                     sh "locust -f load_tests/locust_test.py --host=https://performance-testing.jimdo.com --no-web -c 10 -n10"
                 }
             }
             steps {
                 container('Running test via Selenium') {
                     bzt "load_tests/simple_selenium.yml"
                 }
             }
         }
         stage('Results') {
         }
    }
}