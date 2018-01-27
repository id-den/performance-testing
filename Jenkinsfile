node {
   stage('Build') {
      checkout scm
   }
   stage('Performance Tests') {
       bzt "load_tests/simple_taurus.yml -o modules.console.disable=true"
   }

   stage('Deploy') {
   }
}