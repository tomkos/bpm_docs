# Uninstalling interim fixes silently

## Before you begin

## Procedure

To uninstall an interim fix silently, complete the following
steps:

1. Stop
all software for the product that you are updating. Close
programs and stop servers that have profiles for this product.
2. Open a command prompt, and change directories to the /eclipse/tools directory
under Installation Manager. Important: On Windows, start your command prompt by right-clicking and selecting Run
as administrator.
3 Make the appropriate replacements and run the followingcommand: imcl uninstall fixID -installationDirectory installationDirectory -log logLocation Forexample:C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl uninstall 8.5.5.0-WS-BPMADVWESB-IFJR39658 -installationDirectory C:\IBM\BPM -log logfix.txt

```
imcl uninstall fixID -installationDirectory installationDirectory -log logLocation
```

    1. Replace fixID with
the ID of the interim fix. The ID can be found in the repository.xml file
in the directory where you extracted the interim fix, in the fix
id element. For example:<fix id="8.5.5.0-WS-BPMADVWESB-IFJR39658" version="0.0.0.20111115\_1047" offeringId="EnhancedFix" offeringVersion="0.0.0.EnhancedFix">
    2. Replace installationDirectory with
the location where you installed IBM Business Automation Workflow.
    3. Replace logLocation with
the location and file name to log the information.

```
C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl uninstall 8.5.5.0-WS-BPMADVWESB-IFJR39658 -installationDirectory C:\IBM\BPM -log logfix.txt
```

## Results

The log (specified by the -log parameter)
contains no error messages if uninstalling is successful. The command
line shows a message that the fix was uninstalled.