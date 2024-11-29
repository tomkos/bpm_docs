# Installing interim fixes silently

## Before you begin

Visit the IBM
Support website to check for available fix packs and interim
fixes.

1. Read the interim fix documentation thoroughly. The documentation
lists dependencies, such as WebSphere® Application
Server fix pack levels or other IBM product
fixes that you must install before you apply the interim fix.
2. To ensure that your implementation is performing the same way
that it did before you applied the interim fix, prepare a regression
test plan.
3. Back up your databases and profiles.
4. Before you deploy the interim fix to a production environment,
install the interim fix in a development or quality-assurance environment.
5. You must perform the installation
using the same user account that you used to install the product packages.

## About this task

## Procedure

To install an interim fix silently, complete the following
steps:

1. Download the interim fix to the local system.
2. Create a new directory and extract the interim fix in the
new directory.
3. Stop IBM Business Automation Workflow before you update.
Close all programs and stop servers that have profiles for this product.
4. Open a command prompt, and change directories to the /eclipse/tools directory
under Installation Manager. Important: On Windows, start your command prompt by right-clicking and selecting Run
as administrator.
5 Make the appropriate replacements and run the followingcommand: imcl install fixID -repositories repositoryLocation -installationDirectory installationDirectory -log logLocation Forexample:C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl install 8.5.5.0-WS-BPMADVWESB-IFJR39658 -repositories C:\interimFix\8.5.5.0-WS-BPMADVWESB-IFJR39658 -installationDirectory C:\IBM\BPM -log logfix.txt

```
imcl install fixID -repositories repositoryLocation -installationDirectory installationDirectory -log logLocation
```

    1. Replace fixID with
the ID of the interim fix. The ID can be found in the repository.xml file
in the directory where you extracted the interim fix, in the fix
id element. For example:<fix id="8.5.5.0-WS-BPMADVWESB-IFJR39658" version="0.0.0.20131115\_1047" offeringId="EnhancedFix" offeringVersion="0.0.0.EnhancedFix">
    2. Replace repositoryLocation with
the directory where you extracted the interim fix.
    3. Replace installationDirectory with
the location where you installed IBM Business Automation Workflow.
    4. Replace logLocation with
the location and file name to log the installation information.

```
C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl install 8.5.5.0-WS-BPMADVWESB-IFJR39658 -repositories C:\interimFix\8.5.5.0-WS-BPMADVWESB-IFJR39658 -installationDirectory C:\IBM\BPM -log logfix.txt
```

## Results

```
Installed 8.5.5.0-WS-BPMADVWESB-IFJR39658\_0.0.0.20130525\_1047 to the C:\IBM\BPM directory.
```

## Related information

- IBM Installation Manager documentation