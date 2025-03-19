pipeline {
  agent { label 'principal' } // Ensure this agent is a Windows machine

  environment {
    // Define the SonarScanner tool name (configured in Jenkins Global Tool Configuration)
    SONAR_SCANNER_HOME = tool name: 'sq_test', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
  }

  stages {
    // Stage 0: Setup Python and ensure pip is installed
    stage('Setup Python') {
      steps {
        script {
          // Check if Python is installed
          def pythonInstalled = bat(script: 'python --version', returnStatus: true) == 0
          if (!pythonInstalled) {
            // Install Python (example for Windows)
            bat 'curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe'
            bat 'python-installer.exe /quiet InstallAllUsers=1 PrependPath=1'
            bat 'del python-installer.exe'
          }

          // Ensure pip is installed
          bat 'python -m ensurepip --upgrade'
        }
      }
    }

    // Stage 1: Checkout the code from GitHub
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/RanfordSAS/python_api.git'
      }
    }

    // Stage 2: Create and activate a Python virtual environment
    stage('Setup Virtual Environment') {
      steps {
        bat 'python -m venv venv'
      }
    }

    // Stage 3: Install Python dependencies inside the virtual environment
    stage('Install Dependencies') {
      steps {
        bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
      }
    }

    // Stage 4: Run tests and generate coverage report (optional)
    /*
    stage('Run Tests') {
      steps {
        bat 'call venv\\Scripts\\activate && pytest --cov=./ --cov-report=xml:coverage.xml'
      }
    }
    */

    // Stage 5: Run SonarQube analysis
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
