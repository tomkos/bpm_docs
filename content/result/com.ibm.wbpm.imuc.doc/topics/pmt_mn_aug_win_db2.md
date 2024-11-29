# Augmenting managed-node profiles using the Profile Management
Tool

## Before you begin

Remember to
shut down any servers associated with a profile you plan to augment.

## About this task

If you want to augment a
custom profile using the Profile Management Tool, it must not yet
be federated.

<!-- image -->

<!-- image -->

- To run the Profile Management Tool on Windows, you
must elevate your Microsoft Windows user account privileges.
Whether you are an administrative user or a non-administrative user,
right-click the pmt.bat file and select Run
as administrator. Alternatively, use the runas command
at the command line. For example, the following command can be run
from the installation\_root\bin\ProfileManagement directory:runas /user:MyAdminName /env pmt.batNon-administrative
users are prompted for the administrator password.
- If you install multiple instances of IBM Business Automation Workflow as
the root user and give a nonadministrative user access to only a subset
of those instances, the Profile Management Tool does not function
correctly for the nonadministrative user. In addition, a com.ibm.wsspi.profile.WSProfileException or Access
is denied message occurs in the installation\_root\bin\ProfileManagement\pmt.bat file.
By default, nonadministrative users do not have access to the Program
Files directory, which is the default installation location
for the product. To resolve this issue, nonadministrative users must
either install the product by themselves or be given permission to
access the other product instances.

## Procedure

1 Use one of the following methods tostart the Profile Management Tool.
    - Start the tool from the Quick Start console.
    - Use the Windows Start
menu. For example, select Start > Programs or  All Programs > IBM > Business Process Manager
8.5 > Profile Management Tool.
    - Run the command installation\_root\bin\ProfileManagement\pmt.bat
2. Shut down any servers associated with a profile
you plan to augment.
3. On the Welcome page,
click Launch Profile Management Tool or select
the Profile Management Tool tab.
4. On the Profiles tab,
select the profile that you want to augment and click Augment. 
If you augment a WebSphere Application
Server profile,
it must be from the version of WebSphere Application
Server on which IBM Business Automation Workflow is
installed. The Augment button cannot be selected
unless a profile can be augmented. The Augment
Selection  page opens in a separate window.
5. On the Augment Selection page,
select the Business Automation Workflow managed node augmentation
template. Then click Next.
6. On the Profile Augmentation
Summary page, review the information. Click Augment to
augment the profile or Back to change the characteristics
of the profile.
7. On the Profile Augmentation
Complete page, review the information. To proceed to the
Quick Start console, make sure that Launch Quick Start
console is selected and click Finish.

## What to do next

After
you have finished adding managed-node profiles, configure the deployment
environment.