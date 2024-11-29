<!-- image -->

# Preparing to install

## About this task

Versions of IBM® Integration
Designer that are earlier than 20.0.0.1 can't be upgraded. You must perform a new installation first.
Different versions of Integration Designer can coexist on
your workstation, but they must not be installed in the same directory.

## Procedure

Before you install the product, complete these steps:

1. Confirm that your system meets the IBM Integration
Designer hardware and software
requirements described in Detailed system requirements for a specific product.
2. Read the section Planning to install and give particular attention to the
topic Coexistence considerations.
3. Prepare your operating system following the instructions.
4. Download the most recent base image of Integration Designer and the service release
(delta .zip file) for the version you want from the IBM Password Advantage website. The files you
should download depend on which version you are installing. Download the base release and add the
service release and fixable files. Details are in the download documentation and Fix Central.
5. Extract all the files onto your local file system or a shared drive. Extract all files to
the same location, and overwrite directories if prompted.
Launchpad and IBM Installation
Manager can obtain updates
from online repositories; however, if you're running in an isolated environment you might need to
prepare by downloading updates from Index of
/software/websphere/bpm/repositories/server/launchpad/2000, download both files for the
launchpad interim fix and put them into a directory on your local system.Create the following
file: %HOMEPATH%bpm\_updates.properties
In the
bpm\_updates.properties file, add text to point to the location of the
cumulative fix and the launchpad interim fix in your local system, for
examplelaunchpad.1=interim\_fix\_location
fixpack.BPM\_CF=local\_repository\_path
iid.20002.delta.repository.zip
workflow.20002.delta.repository.zip
These details are from step 2b in Installing IBM
Business Automation Workflow Version 21.0.3.

- Preparing Windows systems for installation

Before you can install IBM Business Automation Workflow, you must prepare your Windows operating system.