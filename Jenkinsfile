pipeline {
  agent { label 'principal' }
  stages {
    stage('Preparar') {
      steps {
        bat 'echo Directorio actual: %cd%'
        bat 'dir'
      }
    }
    stage('Scan') {
      steps {
        withSonarQubeEnv(installationName: 'sq_test') {
          bat 'mvnw.cmd clean org.sonarsource.scanner.maven:sonar-maven-plugin:3.9.0.2155:sonar'
        }
      }
    }
  }
}
