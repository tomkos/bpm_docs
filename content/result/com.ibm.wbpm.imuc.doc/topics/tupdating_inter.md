<!-- image -->

# Installing fix packs for IBM Integration
Designer interactively

## Before you begin

Each installed package
has the location embedded for its default IBM update repository. For Installation Manager
to search the IBM update repository
locations for the installed packages, the preference Search
service repositories during installation and updates on
the Repositories preference page must be selected. This preference
is selected by default.

During the update process the repository
for the base version of the package is required. If you have deleted
the files required for rollback in Installation Manager, then Installation
Manager prompts for the original installation disk when you upgrade
to a fix pack. If you installed the product from DVDs or other media,
they must be available when you use the update feature.

## About this task

You cannot use this procedure to install updates on the underlying IBM Db2® Standard
Edition or IBM
Cognos® Analytics. You must update these products following
their normal update processes.

## Procedure

To find and install product package updates:

1. Close all programs that were installed using Installation
Manager before updating.
2 Start Installation Manager. From the Start page of theInstallation Manager, click Update .
    - You can also click Start > Programs > IBM > package
group name > Update. For example, click Start > Programs > IBM > IBM Integration
Designer > Update.
3. If IBM Installation
Manager is not detected on your system or if an older version is already
installed, then you must continue with the installation of the latest
release. Follow the on-screen instructions in the wizard to complete
the installation of IBM Installation
Manager.
4 If you do not have Internet access, download the interimfix or fix pack locally, extract it to its own directory, and addthe new directory to Installation Manager.

1. Start Installation Manager.
2. From the Start page, click File > Preferences > Repositories.
3. From the Repositories page, click Add Repository.
4. In the Add Repository window, browse
to the new directory you created for the interim fix or fix pack files.
5. Select the repository.config file
and click Open.
6. From the Repositories page, click OK.
5. In the Update Packages wizard, select
the package group containing the product package you want to update
or select the Update all check box, and then
click Next. Installation Manager
searches for updates in its repositories and the predefined update
sites for the software you are updating. A progress indicator shows
the search is taking place.
6 If updates for a package are found, then they are displayed in theUpdates list on the Update Packages page under their corresponding package.Only the latest recommended updates are displayed by default. Click Show all to display all updates found for the available packages.

1. To learn more about an update, click the update and review its description under
Details.
2. If additional information about the update is available, a More info
link is included at the end of the description text. Click the link to display the information in a
browser. Review this information before installing the update.
7. Select the updates that you want to install or click Select
Recommended to restore the default selections, and click Next.
Updates that have a dependency relationship are automatically selected
and cleared together.
8. On the Licenses page, read the license agreements for the selected
updates. The list of licenses for the updates you selected is displayed; click each item to display
the license agreement text. If you agree to the terms of all the license agreements, click
 I accept the terms of the license agreements. Then click
Next.
9 On the Summary page, review your choicesbefore installing the updates.

1. If you want to change the choices you made on previous
pages, click Back, and make your changes.
2. When you are satisfied, click Update to
download and install the updates. A progress indicator shows the percentage
of the installation completed.
10. Optional: 
When the update process completes, a message that confirms the success of the process is
displayed. Click View log file to open the log file for the current session
in a new window. You must close the Installation Log window to continue.
11. Click Finish to close the wizard.
12. Close Installation Manager.