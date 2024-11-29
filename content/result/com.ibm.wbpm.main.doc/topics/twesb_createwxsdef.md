<!-- image -->

# Creating a new WebSphere eXtreme
Scale definition

## About this task

## Procedure

1. In the navigation pane, click Service integration > WebSphere eXtreme
Scale definitions.
The eXtreme Scale definitions page, showing a list of all the eXtreme Scale definitions, is
displayed.
2. Click New.
The eXtreme Scale definitions configuration page opens.
3. Complete the following property fields:

WebSphere eXtreme
Scale
definition name
This field is required and must be unique inside the cell. It is the administrative name for
this eXtreme Scale
definition.
Description
You can use this field to enter a description for the definition. Optional - for your own
reference.
Default WebSphere eXtreme
Scale definition
This field indicates whether this definition is the default. If this is the first definition you
have created, this definition will be set as the default. Note: You cannot update the default from
this page.

Grid name
This field is required because it is the identifier for the location of the grid within the
Object Grid XML file.
Catalog service endpoints
This field is required because it is the identifier as a hostname (or IP address) and port to
connect to a WebSphere eXtreme
Scale catalog server.
Security enabled
You can specify whether you want security to be enabled when you connect to the eXtreme Scale server.
Credential generator
If you specify that you want security to be enabled, then you are required to select which
security credentials you want to use to authenticate with the eXtreme Scale server. The valid
options are either UserPassword or WSToken.
Authentication Alias
If you specify to use UserPassword security credentials, then you must
define the alias to authenticate with the eXtreme Scale server instance.
4. Click Apply to save these properties.
5. Click Save to apply your changes to the master configuration.

## Results