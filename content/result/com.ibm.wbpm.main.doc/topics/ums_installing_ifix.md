# Installing User Management Service iFixes

- Viewing available iFixes
- Applying an interim fix to a User Management Service installation
- Removing an interim fix from a User Management Service installation:
- Updating the Liberty ND server.

## Viewing available iFixes

1. In a browser, go to Fix
Central.
2. Click Find product.
3. For the product group, select  IBM® Business Automation Workflow.
4. Select the version of the product to be updated.
5. For the platform, select your operating system, and click Continue.
6. Select Browse for fixes, and click Continue.
7. For information about a particular fix, click More
Information.

## Applying an interim fix to a User Management Service installation

User Management Service archive-based
interim fixes are named version-ums-archive-fix.jar,
where version is the fix pack level identifier,
for example, 1.0.4-ums-archive-fix.jar.

Each
interim fix is installed by executing the relevant JAR file, which
extracts the content into the User Management Service  /wlp/ibmUsermanagement directory.
A  readme.txt file includes backup and restore
instructions and a description about any APAR context.

1. Open a console and direct it to the location of the JAR file.
2. (Optional) To view the available options, enter the command:java -jar version-ums-archive-fix.jar -help
3. If your Liberty installation is in the wlp directory
or in the same directory as the JAR file, enter the command:java -jar version-ums-archive-fix.jarTip: Optionally specify the --verbose option.
4. If your Liberty installation is not in the wlp directory and not in the
same directory as the JAR file, enter the
command:java -jar version-ums-archive-fix.jar LibertyRootDirWhere
LibertyRootDir is the absolute or relative path to the Liberty installation
directory.
5. To activate the fix in your runtime, stop and restart your User Management Service servers.

## Removing an interim fix from a User Management Service installation:

1. Stop  your User Management Service servers.
2. Delete the directory LibertyRootDir/wlp/ibmUserManagement and
replace it with the backup.
3. To deactivate the fix in your runtime, stop and restart your User Management Service servers.

## Updating the Liberty ND server.

1. In a separate installation directory, download and install the
liberty ND server as described in Installing Liberty by extracting a Java archive file.
2. Copy the wlp/usr and the wlp/ibmUserManagement folders
from the old to the new installation directory.
3. Stop the User Management Service server(s)
in the old installation directory.
4. Start the User Management Service server(s)
from the new installation directory.