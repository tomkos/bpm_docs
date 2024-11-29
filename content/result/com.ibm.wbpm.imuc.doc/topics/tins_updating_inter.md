# Installing fix packs and interim fixes interactively

You can install updates to software
packages using IBM® Installation
Manager interactively.

You cannot use this procedure to install updates on the
underlying IBM Db2® Standard
Edition database. You
must update Db2 by following its
normal update process.

## Before you begin

Visit the IBM
Support website to check for available fix packs and interim
fixes.

1. Read the fix pack and interim fix documentation thoroughly. The
documentation lists dependencies, such as WebSphere® Application Server fix pack levels
or other IBM product fixes that
you must install before you apply the fix pack or interim fix.
2. To ensure that your implementation is performing the same way
that it did before you applied the fix pack or interim fix, prepare
a regression test plan.
3. Back up your databases and profiles.
4. Before you deploy the fix pack or interim fix to a production
environment, install the fix pack or interim fix in a development
or quality-assurance environment.
5. You must perform the installation
using the same user account that you used to install the product packages.

Each installed package has the location embedded for
its default IBM update repository.
For Installation Manager to search the IBM update
repository locations for the installed packages, the preference Search
service repositories during installation and updates on
the Repositories preference page must be selected. This preference
is selected by default.

During the update process, Installation
Manager might prompt you for the location of the repository for the
base version of the package. If you installed the product from DVDs
or other media, they must be available when you use the update feature.

## Procedure

To find and install product package updates:

1. Stop
all software for the product that you are updating. Close
programs and stop servers that have profiles for this product.
2 Start Installation Manager. From the Start page of theInstallation Manager, click Update .
    - You can also click Start > Programs > IBM > package
group name > Update. For example, click Start > Programs > IBM > IBM Business Automation Workflow > Update.
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
to the directory where the extracted files for the interim fix or
fix pack are located.
5. Double-click the repository.config file.
6. Click OK in the Add
Repository window. Click OK to close
the Preferences window.
5. In the Update Packages wizard, select
the package group containing the product package you want to update
or select the Update all check box, and then
click Next. Enter your IBM user ID and password.
Installation Manager searches for updates in its repositories
and the predefined update sites for the software you are updating.
A progress indicator shows the search is taking place.
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
If you do not accept the terms of the license agreements, you cannot install the fix pack or
interim fix.
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

## Related information

- IBM Installation Manager documentation
- Applying fix packs to DB2 database products