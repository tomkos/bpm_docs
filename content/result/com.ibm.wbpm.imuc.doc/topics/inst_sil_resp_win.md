# Installing silently using a response file

## Before you begin

- IBM Installation
Manager
- WebSphere® Application
Server Network Deployment, including the
ejbdeploy and thinclient features.

## About this task

By using response files, you can simplify the silent installation and
reduce errors in the process because you set up your installation options once in a saved, sharable
file that can be used on one or more machines. The installation software provides sample response
files for each supported operating system. You can use an unmodified sample response file to perform
a silent installation using default settings, or you can modify the response file to set particular
values. The comments in the sample response files provide detailed instructions and information
about setting the values.

- Installation Manager is installed or updated to the appropriate level.
- The required base products and IBM Business Automation
Workflow are
installed.

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1. Run the following command to generate
encrypted passwords using Installation Manager to securely connect to Db2® and the administrative console. 
Important: On Windows, start your command prompt by right-clicking and selecting
Run as administrator.
extract\_directory/IM64/tools/imutilsc -silent -nosplash encryptString password\_to\_encrypt
Note: If you already have 32-bit Installation Manager installed, you can run the command from the
extract\_directory\IM\tools directory.
2 Create the response file that will install the required base products and IBM Business AutomationWorkflow . Copy a sample response file, suitable for your user access level from the following directory: Alternatively, you can create a response file by recording your actions in InstallationManager. When you record a response file, the selections that you make in Installation Manager arestored in an XML file. When you run Installation Manager in silent mode, Installation Manager usesthe data in the XML response file to perform the installation.
    - extract\_directory/responsefiles/BPM/
3 The default values that are provided in the sample response fileswill perform a basic installation, but you should review the file and its comments, and modify theparameters as needed for your environment and the access level of your user ID. Review the following parameters and values:

Review the following parameters and values:

- Permissions - For non-administrator user IDs, check that all location variables point to
locations that the user has permissions for.
- Repository location - If you are not installing directly from the
extract\_directory/responsefiles/BPM/ directory, point to the
location of your installation repository. The repository can be local or remote.
- Installation location - The installLocation directory where IBM
Installation Manager is or will be installed.
- Product installation location - The directory where the product will be installed. To install
into an existing supported instance of WebSphere Application
Server Network Deployment,
specify its directory.Tip: Keep the installation path as short as possible. Otherwise,
you might run into problems later when the paths of other components, when added to this path,
exceed the 255-character path limit.
- Eclipse location - The eclipseLocation directory. To install into an
existing supported instance of WebSphere Application
Server Network Deployment, specify its
Eclipse location directory.
- The list of features for the product
- Production or non-production use - Your selection is recorded in the product tag for inventorypurposes, so select the license feature that matches the license you have purchased and want to use.Important:
    - Workflow Server is most often considered a production
server. Check the license for verification.
    - Do not mix production and non-production servers in the same cell.
- If you are installing Db2, follow
the instructions in the response file for providing the necessary user IDs and passwords. Use the
instructions in step 1 for generating the encrypted passwords to include in the response file.
4. Read and accept the license terms before installing. Adding
-acceptLicense to the command line means that you accept all licenses.
5. Run the following command:

Important: On Windows, start your command prompt by right-clicking and selecting
Run as administrator.
Administrator:extract\_directory/IM64/installc.exe -acceptLicense input  
  extract\_directory/responsefiles/BPM/response\_file\_name.xml 
  -log preferred\_log\_location/silent\_install.log
Non-administrator:extract\_directory/IM64/userinstc.exe -acceptLicense input  
  extract\_directory/responsefiles/BPM/response\_file\_name.xml 
  -log preferred\_log\_location/silent\_install.log

## Results

Installation Manager installs the required prerequisites and IBM Business Automation
Workflow, and writes a log file to the directory that you
specified.

## What to do next

## Related tasks

- Working in silent mode
- Recording a response file with Installation Manager

## Related reference

- IBM Business Process Manager system requirements
- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow