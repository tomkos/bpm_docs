# Commit and deliver scripts

## Commit script

- Commits the changes to the IBM® Business Automation
Workflow repository
- Copies the changed solution files to the sandbox
- Runs a commit script that you provided to check the set of changes from the sandbox into the
VCS

- Reads the input parameters supplied in the input.properties file
- Handles deleted solution assets
- Creates a change set that contains any new or modified solution assets
- Associates the comments that the user entered for the Commit action with
each asset
- Checks the change set into the VCS

## Deliver script

After a solution is committed, the user clicks the Deliver action on the
Manager Solutions page. Case Builder then runs
the deliver script that you provided. This script checks the modified solution as a whole into the
VCS.

- Reads the input parameters supplied in the input.properties file
- Checks all of the solution assets and the solution manifest into the VCS
- Associates the comments that the user entered for the Deliver action with
each asset
- Creates a baseline or snapshot of the solution
- Labels the baseline and delivers it to the VCS

## Script requirements

The scripts can be either .sh files for Linux or AIX systems or
.bat files for Windows systems.

The scripts must be in the scripts subdirectory of the sandbox. You can edit
the stub scripts that the BPMConfig command creates in the
scripts subdirectory. Alternatively, you can create your own scripts to replace
the stub script files. If you create the scripts, you must give them the same names as the stub
script files.

Case Builder passes to the scripts the path to the user's
sandbox. This path takes the following form:sandbox\solution
prefix\user name. For example, the path might be
C:\sandbox\_CreditCard\DISP\ajones where
C:\sandbox\_CreditCard is the sandbox, DISP is the solution
prefix, and ajones is the name of the user who is committing or delivering the
solution.

These scripts must return an integer code. Use the return code 0 to indicate successful execution
of the script.

If you specify a heartbeat interval when you configure VCS integration, the scripts must modify
the output.txt file in the sandbox to serve as the heartbeat. The scripts can
output error messages and other information messages to either the output.txt
file or to standard output. IBM Business Automation
Workflow captures and logs the
content of the output.txt file.