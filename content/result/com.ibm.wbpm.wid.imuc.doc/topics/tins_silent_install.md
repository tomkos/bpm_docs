# Installing IBM Integration
Designer silently using a
response file

## Before you begin

Operating system and software prerequisite levels are important. Although the
installation process automatically checks for prerequisite operating system patches, review the
system requirements if you have not done so. The system requirements link lists all supported
operating systems and the operating system fixes and patches that you must install to have a
compliant operating system. It also lists the required levels of all prerequisite
software.

## About this task

- Installation Manager
- WebSphere® Application
Server Network Deployment (if you are
installing the test environment)

- Installs Installation Manager if it is not already installed or updates it to the appropriate
level if it is installed.
- Installs the required base products and IBM Integration
Designer.

## Procedure

To silently install IBM Integration
Designer, complete the following steps:

1. Before installing, read and accept the license terms. Adding -acceptLicense to
the command line means that you accept all licenses.
2 Create the response file that will install the required base products and IBM IntegrationDesigner . Copy a sample response file, suitable for your operating system and useraccess level, from one of the following directories: Alternatively, you can create a response file by recording your actions in InstallationManager. When you record a response file, the selections that you make in Installation Manager arestored in an XML file. When you run Installation Manager in silent mode, Installation Manager usesthe data in the XML response file to perform the installation.
    - To install both Integration Designer and the test
environment:
extract\_directory/disk1/responsefiles/iid\_testenv/
    - To install Integration Designer alone:
extract\_directory/disk1/responsefiles/iid/
3 Review the file and its comments, and modify the parameters as needed for yourenvironment. The default values provided in the sample response files will perform a basic installation.In particular, review the following parameters and values:

In particular, review the following parameters and values:

- If you are installing as a non-Administrator or non-root user, check that all location variables
point to directories that your user ID has permissions for.
- Repository locations. If your response file is not stored in the
extract\_directory/responsefiles/BusMon directory, update the
default relative paths of the repository locations. The repository locations can be local or remote.
- Installation location of Installation Manager. If
necessary, update the location where Installation Manager is
already installed or will be installed.
- Installation location of IBM IntegrationDesigner . Ifnecessary, update the location where a supported instance of WebSphere ApplicationServer Network Deployment is already installed or will be installed.IBM IntegrationDesigner , and optionally, IBMCognos® Analytics and DB2 Express will also be installed intothis location.Tip:
    - Ensure that your installation path does not contain parentheses.
    - If you are installing DB2 Express, your installation path cannot contain National Language
Strings (NLS).
    - Keep the installation path as short as possible. Otherwise, you might run into problems later
when the paths of other components, when added to this path, exceed the 255-character path
limit.
- Eclipse location (eclipseLocation). If you want to install into an existing
supported instance of WebSphere Application
Server Network Deployment, specify its
Eclipse location directory.
- WebSphere Application
Server Network Deployment features. Accept the default list
of features.
- IBM Integration
Designer features. Specify whether you
want to install the product for production use, or for development, test, or staging
(non-production) use.
- If you are installing DB2 Express, follow the instructions in the response file for providing
the necessary user IDs and passwords. Use the instructions in step 1 for generating the encrypted
passwords to include.
4. Run the following command.
Important: If you are running Windows, start your command prompt by
right-clicking and selecting Run as administrator.
To
install IBM Integration
Designer and the test
environmentextract\_directory\disk1\IM\_win64\installc.exe
-acceptLicense input ..\responsefiles\response\_file\_name.xml -log
silent.logNote: If you already have 32-bit Installation Manager installed, then you can
run the command from the extract\_directory\IM\_win32\tools
directory.

To install IBM Integration
Designer
aloneextract\_directory\disk1\IM\_win64\installc -acceptLicense
input ..\responsefiles\response\_file\_name.xml -log
silent.log

## Results

## What to do next