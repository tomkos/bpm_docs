# installProcessAppPackage command-line utility (deprecated)

## Location

The installProcessAppPackage command-line utility is in the
install\_root/BPM/Lombardi/tools/process-installer
directory.

## Syntax

The syntax differs depending on whether you have a stand-alone or network deployment environment.
The command is run against the default profile, although you can use optional parameters to run the
command against a different profile.

- Stand-alone
environmentinstallProcessAppPackage.bat 
{optional\_parameters} 
install\_package\_name 
user\_name 
user\_password
- Network deployment
environmentinstallProcessAppPackage.bat 
{optional\_parameters} 
-host host\_name 
-port port\_name 
-nodeName node\_name 
-serverName server\_name 
install\_package\_name 
user\_name 
user\_password

## Parameters

<!-- image -->

<!-- image -->