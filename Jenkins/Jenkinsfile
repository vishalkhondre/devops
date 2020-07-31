node ('buildserver') {

    stage('checkout-scm') {
        checkout changelog: false, 
        poll: false, 
        scm: [$class: 'GitSCM', branches: [[name: '*/master']], 
        doGenerateSubmoduleConfigurations: false, 
        extensions: [], 
        submoduleCfg: [], 
        userRemoteConfigs: [[url: 'https://github.com/ganeshhp/helloworldweb.git']]]
    }

    stage('build') {
        sh label: '', script: 'mvn package'
    }

    stage('save-artifact') {
        archiveArtifacts artifacts: 'target/Helloworldwebapp.war', followSymlinks: false
    }

}