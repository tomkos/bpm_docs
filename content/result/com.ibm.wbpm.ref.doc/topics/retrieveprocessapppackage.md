# retrieveProcessAppPackage command-line utility (deprecated)

You can customize your offline installation by using optional parameters at the command line to
override the default values for this utility.

## Location

The retrieveProcessAppPackage command-line utility is in the
install\_root/BPM/Lombardi/tools/process-installer
directory.

## Syntax

The syntax differs depending on whether you have a stand-alone or network deployment environment.
The command is run against the default profile, although you can use optional parameters to run the
command against a different profile.

- Stand-alone
environmentretrieveProcessAppPackage.bat 
{optional\_parameters} 
process\_app\_acronym 
snapshot\_name 
offline\_server\_name 
install\_package\_name 
user\_name 
user\_password
- Network deployment
environmentretrieveProcessAppPackage.bat 
{optional\_parameters} 
-host host\_name 
-port port\_name 
-nodeName node\_name 
-serverName server\_name 
process\_app\_acronym 
snapshot\_name 
offline\_server\_name 
install\_package\_name 
user\_name 
user\_password

## Parameters

<!-- image -->

<!-- image -->

## Examples

<!-- image -->

<!-- image -->

```
retrieveProcessAppPackage.sh TESTDPL Test\ Snapshot Dev\ Offline test\_package\_file.zip
```

```
retrieveProcessAppPackage.sh TESTDPL "Test Snapshot" "Dev Offline" test\_package\_file.zip
```