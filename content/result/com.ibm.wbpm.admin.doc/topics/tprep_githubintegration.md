# Configuring projects for a CI/CD integration

Github offers the facility to configure a webhook that you can use to
trigger an automated and secure continuous integration and continuous delivery (CI/CD) pipeline
hosted in your preferred CI/CD tool. When a new snapshot of your workflow project is created, you
can trigger the Github webhook by pushing a file descriptor of the project (in JSON format) to a
configured Git repository, which in turn triggers the CI/CD pipeline.

This feature is available only on Workflow Center.

## Procedure

Complete the following configuration to push the project descriptor file of your
workflow snapshot to Github.

1. Install Business Automation Workflow
and create the deployment environment.
2. Update the
100Custom.xml file with the Github repository URL and authentication alias name
by adding the following configuration. For the location of the file and instructions about updating
it, see Location of 100Custom configuration files and Creating a 100Custom.xml configuration file. <server>
                <git-configuration  merge="replace">
                  <git-endpoint-url>https://api.github.com/repos/user1/bawgitrepo</git-endpoint-url>
                  <git-auth-alias-name>Git-J2C-Auth-Alias-Name</git-auth-alias-name>
                </git-configuration>
              </server>where <git-endpoint-url> is the REST
API URL for your Git repository. The value should be "api.github.com" instead of
"github.com".
3. If required, import the target Github Enterprise Transport Layer
Security (TLS) trust in the WebSphere administrative console.  This step is not needed if the Git website is signed with a well-known
certificate authority (CA). See How to add the signer/public key/remote server certificate to the
WebSphere Application Server truststore trust.p12 or java truststore
cacerts.
4. Create an authentication alias in the WebSphere
administrative console by clicking Security > Global
security > Java Authentication and Authorization
Service > J2C authentication
data > New. The authentication alias is saved to
INSTALL\_PATH/profiles/Dmgr/config/cells/cell\_name/security.xml.<authDataEntries xmi:id="JAASAuthData\_1697618472314" alias="Git-J2C-Auth-Alias-Name" userId="bpmadmin1bbb" password="{xor}KzA6NDErMDQ6MQ==" description=""/>
5. Synchronize the node and restart the server.
6 Verify the configuration:
    - Check TeamWorksConfiguration.running.xml to see that
<git-endpoint-url> and <git-auth-alias-name> are
merged into the file. For the location of the file, see Location of 100Custom configuration files.