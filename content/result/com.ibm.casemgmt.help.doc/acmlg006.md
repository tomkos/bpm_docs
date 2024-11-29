# Log files for the Business Automation Workflow installation

| Operating system                 | Default file path                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------|
| AIX®  Linux®  Linux for System z | /opt/IBM/CaseManagement/logs/IBM\_Case\_Manager\_5.2.1.0\_InstallLog.txt                       |
| Windows                          | drive:\Program Files (x86)\IBM\CaseManagement\logs\IBM\_Case\_Manager\_5.2.1.0\_InstallLog.txt |

The installation process also creates logs with debug
information in the temp directory that is configured for your system.
If there are problems with the installation, check the debug logs
for more information. The following table shows sample default locations
of the temp directory. Your temp directory might be in a different
location.

| Operating system               | Default file paths                                                                                                                                |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| AIX  Linux  Linux for System z | /tmp/cm520\_install\_stderr.txt  /tmp/cm520\_install\_stdout.txt                                                                                      |
| Windows                        | drive:\Users\Administrator\AppData\Local\Temp\2\cm520\_install\_stderr.txt drive:\Users\Administrator\AppData\Local\Temp\2\cm520\_install\_stdout.txt |