pipeline {
  agent { label 'principal' } // Ensure this agent is a Windows machine
  tools {
    maven '3.8.1' // Ensure Maven 3.8.1 is configured in Jenkins for Windows
  }
  stages {
    stage('Maven Version') {
      steps {
        bat 'mvn --version' // Use 'bat' for Windows commands
      }
    }
    stage('Preparar') {
      steps {
        bat 'echo Directorio actual: %cd%' // Print current directory
        bat 'dir' // List files in the current directory
      }
    }
    stage('Scan') {
      steps {
        withSonarQubeEnv(installationName: 'sq_test') { // Use SonarQube environment
          bat 'mvnw.cmd clean org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
        }
      }
    }
  }
}
