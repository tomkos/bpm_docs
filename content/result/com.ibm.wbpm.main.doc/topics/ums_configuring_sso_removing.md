# Removing  single sign-on authentication delegation

1 If you want to remove an IBM Business Automation Workflow singlesign-on configuration, you must set up the environment variables that points to IBM Business Automation Workflow installation directory:
    1 Open a command prompt and navigate to the following directory: Where profile\_name is the profile name of the Deployment Manager (typically, this isDmgr01 ) and drive : is the system drive on which the file directory isstored. For example: C: or D: .
        - Linux:
/opt/IBM/WebSphere/AppServer/profiles/profile\_name/bin
        - Windows: drive:\Program
Files\IBM\WebSphere\AppServer\profiles\profile\_name\bin

Where profile\_name is the profile name of the Deployment Manager (typically, this is
Dmgr01) and drive: is the system drive on which the file directory is
stored. For example: C: or D:.

2 Execute the following script:
    - Linux: ./setupCmdLine.sh
    - Windows:  setupCmdLine.bat
2. Reuse the properties file for configuration that you want to remove:
For an IBM Business Automation Workflow or Process Portal configuration
Reuse the connectToUms-workflow.properties file that was edited in the add
scenario and modify the parameters that have changed. Important: If you connected your
IBM Business Automation Workflow system to User Management 1.0.0, you
do not yet have a connectToUms-workflow.properties file. Use the template from
wlp/ibmUserManagement/extension/configTemplates/workflow/connectToUms-workflow.zip
and adapt the properties matching the connectToUms.jy script that was executed
at the time of connecting.

For a Process Federation Server configuration
Reuse the connectToUms-PFS.properties file that was edited in the add
scenario and modify the parameters that have changed.
3 Run connectToUms.bat or connectToUms.sh to execute theparameters of your customized properties file.Forexample: For an IBM Business Automation Workflow or Process Portal configuration Enter thecommand:connectToUms.bat remove -username <user name> -password <password> -ums\_username <User Management admin user> -ums\_password <User Management admin user password> For a Process Federation Server configuration

```
connectToUms.bat remove -username <user name> -password <password> 
   -ums\_username <User Management admin user>  -ums\_password <User Management admin user password>
```

1. Enter the
command:connectToUms.bat remove
   -ums\_username <User Management admin user> -ums\_password <User Management admin user password>
2. Reverse the changes to the Process Federation Server configuration file from the
wlp/ibmUserManagement/extension/configTemplates/pfs/PFS-template-server.xml
file and any other changes that you made when you added the configuration.
4. For UMS 1.0.0, 1.0.1, and 1.0.3 quick start configurations, you must also remove the client from
your User Management Service configuration XML files.
5. Restart your server.