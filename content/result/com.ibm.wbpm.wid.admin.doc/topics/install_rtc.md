<!-- image -->

# Installing Rational Team Concert into the workbench

## About this task

You can use the installation method described in the procedure
to install Rational Team Concert Client v2.x into the same workspace
as IBM Integration Designer.

1. Open the Installation Manager that references your IBM Integration
Designer installation.
2. Follow the Rational Team Concert Client 3.0 installation instructions
to add the path to the repository location.
3. Install Rational Team Concert Client 3.0 to the same package as
Integration Designer.

## Procedure

1. From https://jazz.net, download a "p2 Install"
edition of a version of Rational Team Concert Client for Eclipse that
is compatible with IBM Integration Designer. For Rational Team Concert
Client v2.x, you must use this method; using IBM Installation Manager
to install into the same workbench as the IDE is only supported for
version 3.0 and later.
2. Extract the contents of the compressed file that you downloaded.
For example, extract the contents to C:\RTC. Ensure that you preserve
the directory structure of the extracted contents.
3. Start Integration Designer.
4. Click Help > Install new software.
5. In the Available Software wizard, click Add.
6. In the Add Repository window, beside the Name field, click Local and then look for the
rtc-p2-repository subdirectory of the directory where you previously
extracted the compressed file, for example, C:\RTC\rtc-p2-repository. Click OK.
7 On the Available Software page:
    1. In the Name section, select Rational Team
Concert and, optionally, one or both NLS categories to
install language packs.
    2. In the Details section, ensure Group items
by category and Contact all update sites are selected.
8. Click Next, and click Next again on the Details page and on the Install Details
page.
9. On the Review Licenses page, read the text of the license
agreements. If you agree to the terms of all of the license agreements,
select I accept the terms of the license agreements and then click Finish.
10. During the installation, a security warning window-box
might open because the Rational Team Concert Client bundles and features
are not signed. If this happens, click OK to
complete the installation.
11. When you are prompted to restart at the end of the installation,
click Yes. When the workbench
restarts, the Rational Team Concert Welcome page opens.

## What to do next

1. Click Window > Preferences.
2. On the Preferences page, expand General and click Capabilities.
3. On the Capabilities page, click Advanced.
4. In the Advance Capabilities Settings window, expand Team, select Jazz Source Control, and then click OK.
5. On the Capabilities page, click OK.