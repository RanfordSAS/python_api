pipeline {
  agent { label 'principal' }
  tools {
    maven '3.8.1'
  }
  stages {
    stage('maven') {
      steps {
        sh 'mvn --version'
      }
    }
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
