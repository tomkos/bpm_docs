# Installing interactively

## Before you begin

To extract files on AIX, use the GNU tar program instead of the AIX tar program. The AIX tar
program might truncate long file names, which can cause installation errors. To install the GNU tar
program, see Use GNU tar to extract server installation images on AIX.

<!-- image -->

Extract the installation files to a directory that does not contain spaces or special
characters.

When you install the product, also install any available cumulative fixes or
fix packs. If you have Internet access, you can include available fixes from the live repository
during installation.

- /user\_home\_directory/bpm\_updates.properties

## About this task

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1. Start Installation Manager. For information about where
Installation Manager is installed, see Installation directories for the product and profiles. 
Note: Installation Manager must be at a minimum level of
Version 1.8.0 before you start the installation. Installation Manager detects an available update if you are connected to
the Internet.
Run IM\_INSTALL\_LOCATION/IBMIM.exe.
2. Add the repositories to the Installation Manager preferences.
Open File > Preferences and click Add Repository. Type or browse to the 
repository/repos\_64bit/repository.config file for the repository that you extracted and
click OK to save the new repository settings.
3 Click Install . Select the packages that you want toinstall and click Next . Important:
    - Except on Linux on Power LE, IBM WebSphere SDK Java Technology Edition 8 (Java
8) is always installed and used. Do not change this default. On Linux on Power LE only, Java 7.1 is
installed by default and you must install the Java 8 extension package after you have finished
installing Business Automation Workflow. For instructions, see Installing and uninstalling SDK Java Technology Edition Version 8.0.
    - IBM WebSphere SDK Java Technology Edition 8 (Java 8) is always installed
and used. Do not change this default.
4. On the Licenses page, read the license agreement.
If you agree to the terms of the license agreement, click  I accept the terms in the
license agreements, and then click Next.
5. On the Location page, select the installation directory and click
Next. 
The Install Packages wizard checks your system for operating system prerequisites. If you are
at a later release of a supported operating system, or if the operating system is not supported, you
might receive a warning. You can continue with the installation, but the installation or product
operation might not succeed until you apply product fix packs.If you receive a warning, go to the
product support web pages and obtain the latest fix packs to apply after installation. To migrate
non-IBM prerequisite and corequisite products to the supported versions, see the documentation for
those products.
6 On the Features page, expand the plus symbol to select the packagefeatures that you want to install. Installation Manager automatically enforces dependencies withother features and shows the updated download size and disk space requirements for theinstallation. When you are finished selecting features, click Next . If you choseto install Db2® , you are prompted foryour database administrator user name and password.

1. Select the translations to install. Under Translations Supported by All
Packages, English is selected by default for the English version.
To install other language versions, select the appropriate language under Translations
Supported by Only Some Packages.
2. Optional: 
To see the dependency relationships between features, select Show
Dependencies.
3. Optional: 
Click a feature to view its brief description under Details.
4 Select one of the following features to install. Your selection is recorded in the product tag for inventory purposes, so select the licensefeature that matches the license you have purchased and want to use. There are no functionaldifferences.Important:
    - IBM Business Process
Manager Server Production
License to use the server in production.
    - IBM Business Process
Manager Server Non-production
License to use the server only for development, test, or staging.
    - IBM Business Automation
Workflow Enterprise Service Bus
Production License to use the server in production.
    - IBM Business Automation
Workflow Enterprise Service Bus
Non-production License to use the server only for development, test, or staging.
    - Workflow Server is most often considered a production
server. Check the license for verification.
    - Do not mix production and non-production servers in the same cell.

If you chose
to install Db2®, you are prompted for
your database administrator user name and password.

7. On the Summary page, review your choices before installing the IBM Business Automation Workflow package. The disk space that is required to perform
the update is shown. When you are satisfied with your installation choices, click
Install.
A progress indicator shows the percentage of the installation completed.
8 When the installation process is complete, a message confirms thesuccess of the process.

1. Optional: To open the installation log file for the current session in a
new window, click View Log File. To continue, close the
Installation Log window.
2. If you plan to use the BPMConfig command-line utility to create your
deployment environment, select None to complete the installation.
3. Click Finish.

## What to do next

## Related reference

- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow