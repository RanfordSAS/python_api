pipeline {
  agent { label 'principal' } // Ensure this agent is a Windows machine

  environment {
    // Define the SonarScanner tool name (configured in Jenkins Global Tool Configuration)
    SONAR_SCANNER_HOME = tool name: 'sq_test', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
  }

  stages {
    // Stage 1: Checkout the code from GitHub
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/RanfordSAS/python_api.git'
      }
    }

    // Stage 2: Install Python dependencies
    stage('Install Dependencies') {
      steps {
        bat 'pip install -r requirements.txt'
      }
    }

    // Stage 3: Run tests and generate coverage report
    /*
    stage('Run Tests') {
      steps {
        bat 'pytest --cov=./ --cov-report=xml:coverage.xml'
      }
    }
    */

    // Stage 4: Run SonarQube analysis
    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv(installationName: 'sq_test') { // 'sq_test' is the name of the SonarQube server configured in Jenkins
          bat "${SONAR_SCANNER_HOME}\\bin\\sonar-scanner.bat"
        }
      }
    }
  }

  // Post-build actions
  post {
    success {
      echo 'SonarQube analysis completed successfully!'
    }
    failure {
      echo 'SonarQube analysis failed.'
    }
  }
}
