# Augmenting managed-node profiles using the Profile Management
Tool

## Before you begin

Remember to
shut down any servers associated with a profile you plan to augment.

## About this task

If you want to augment a
custom profile using the Profile Management Tool, it must not yet
be federated.

## Procedure

1 Use one of the following methods tostart the Profile Management Tool.
    - Start the tool from the Quick Start console.
    - Run the command installation\_root/bin/ProfileManagement/pmt.sh.
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