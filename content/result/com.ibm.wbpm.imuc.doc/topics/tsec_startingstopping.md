# Starting and stopping the server

## Before you begin

<!-- image -->

<!-- image -->

- Right-click a command prompt shortcut.
- Click Run As Administrator.
- When you open the command prompt window as Administrator, an operating-system
prompt asks you if you want to continue. Click Continue to
proceed.

## Procedure

1 Start the server. The followingtable describes the options for starting the server. Start the server Details From the First Steps user interface Click Start the server . From a command line Enter: Note: You are not required to provide a user name and passwordto start the server. However, you will need to authenticate yourselfif you try to launch the administrative console or perform any otheradministrative task. The server starts or an errormessage is returned.

The following
table describes the options for starting the server.

| Start the server                    | Details                                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| From the First Steps user interface | Click Start the server.                                                                                      |
| From a command line                 | Enter:  On Windows platforms: startserver servername On Linux® and UNIX platforms: startserver.sh servername |

2 Stop the server. The followingtable describes the options for stopping the server. Stop the server Details From the First Steps user interface Click Stop the server and provide avalid user name and password when prompted. The user name you providemust be in either the operator or administrator role. From a command line Enter: Note: You are required to provide a user name and password tostop the server. If the user name and passwordyou provide are members of the operator or administrator roles, theserver will stop.

The following
table describes the options for stopping the server.

| Stop the server                     | Details                                                                                                                                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From the First Steps user interface | Click Stop the server and provide a valid user name and password when prompted. The user name you provide must be in either the operator or administrator role.                                                                         |
| From a command line                 | Enter:  On Windows platforms: stopserver servername -profileName ProfileName -username username -password password On Linux and UNIX platforms: stopserver.sh servername -profileName ProfileName -username username -password password |

3. Check that the server stopped successfully
The following table describes the options for verifying that
the server stopped correctly.

Check that the server stopped successfully
Details

From the user interface
The First Steps output window details the results of your
request. 

From a command line
The outcome of your request is displayed in the command window
from which the request was made.