# Installing IBM Process Federation
Server silently
by using a response file

## Before you begin

- IBM Installation
Manager. If you
are installing Process Federation Server in group mode,
you must use an instance of Installation Manager that is installed in
group mode. For more information, see the Installation Manager IBM Knowledge Center
topic Group mode roadmaps and silent installation.
- WebSphere® Application
Server Liberty
Network Deployment.
- IBM WebSphere SDK Java Technology Edition for Liberty. For more information about the supported
versions, see the system requirements for your Business Automation Workflow configuration: IBM Business
Automation Workflow detailed system requirements.

## About this task

1. Optional: Installation Manager is installed or updated
to the appropriate level.
2. The required base products and Process Federation Server are installed.

## Procedure

1. Create the response file that will install the required
base products and Process Federation Server.
Copy a sample response file that is suitable for your bit version
and user access level from the following directory: extract\_directory\responsefiles\PFS\extract\_directory/responsefiles/PFS/Alternatively,
you can create a response file by recording your actions in Installation Manager. When
you record a response file, the selections that you make in Installation Manager are stored
in an XML file. When you run Installation Manager in silent
mode, it uses the data in the XML response file for the installation.
2. Review the response file and its comments, and modify the
parameters as needed for your environment and the access level of
your user ID. Although you can use the default values that
are provided in the sample response files for a basic installation,
review the following parameters and values before you use the file:
Permissions
For non-root or installation group user IDs, check that all location
variables point to locations that the user or group has permissions
for.
Repository location
If you are not installing directly from the extract\_directory/responsefiles/PFS/ directory,
point to the location of your installation repository. The repository
can be local or remote.
Installation location
The installLocation directory where Installation Manager is or
will be installed.
Product installation location
The location where Process Federation Server will
be installed. If you want to install the product into an existing
supported instance of WebSphere Application
Server Liberty
Network Deployment, specify its directory.Restriction: Ensure
that the directory names in the path contain only the following characters: 0-9
A-Z a-z (space) & ( ) + - . \_

Eclipse location
The eclipseLocation directory. If you want
to install into an existing supported instance of WebSphere Application
Server Liberty
Network Deployment, specify its Eclipse location directory.
The list of features for the product
3. Read and accept the license terms before you install the
product. Adding -acceptLicense to the
command line means that you accept all licenses.
4 Run the following command. The format of thecommand depends on your permissions.Note: If you already have 32-bit Installation Manager installed,you can run the command from the following directory: directory.
    - extract\_directory\IM\tools
    - extract\_directory/IM/tools
    - Root user:extract\_directory\IM64\installc -acceptLicense 
   input extract\_directory\responsefiles\PFS\response\_file\_name.xml 
   -log preferred\_log\_location\silent\_install.logextract\_directory/IM64/installc -acceptLicense 
   input extract\_directory/responsefiles/PFS/response\_file\_name.xml 
   -log preferred\_log\_location/silent\_install.log
    - Non-root user:extract\_directory\IM64\userinstc -acceptLicense 
   input extract\_directory\responsefiles\PFS\response\_file\_name.xml 
   -log preferred\_log\_location\silent\_install.logextract\_directory/IM64/userinstc -acceptLicense 
   input extract\_directory/responsefiles/PFS/response\_file\_name.xml 
   -log preferred\_log\_location/silent\_install.log
    - Installation group user:extract\_directory\IM64\groupinstc -acceptLicense 
   input extract\_directory\responsefiles\PFS\response\_file\_name.xml 
   -log preferred\_log\_location\silent\_install.logextract\_directory/IM64/groupinstc -acceptLicense 
   input extract\_directory/responsefiles/PFS/response\_file\_name.xml 
   -log preferred\_log\_location/silent\_install.log

## Results

## What to do next

1. Create the Process Federation Server database.
See Creating the Process Federation Server database.
2. Create a process federation server. See Creating a process federation server.