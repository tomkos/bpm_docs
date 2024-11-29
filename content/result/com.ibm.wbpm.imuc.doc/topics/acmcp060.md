# Setting up Box as an external repository and for
sharing

## About this task

For detailed information about configuring IBM Content
Navigator to
connect to Box and enabling document sharing, see Integrating IBM Content
Navigator with Box.

## Procedure

To integrate IBM Business Automation
Workflow with Box:

1. Create a Box application for the IBM Content
Navigator server.
2. Configure a connection to Box.
In the IBM Content
Navigator administration tool of the web client,
click Repositories > New Repository to create a Box repository. If you plan to use
Box to share documents, ensure that you set the
share administrator.
3 Add the Box repository to the IBM Business AutomationWorkflow desktop.
    1. In the IBM Content
Navigator administration tool, click
Desktops and open your IBM Business Automation
Workflow
desktop.
    2. On the Repositories tab, add the Box repository to the Selected Repositories list and save your changes.
4 Enable the Box integration features that you want touse. Feature Procedure Box as an external repository Enable case types to support external documents. In Case Builder ,edit each case type for which you want users to be able to add documents or attachments fromBox and select Allow documents and attachments fromrepositories other than the case management object stores . This option is not requiredif you use Box only to share documents. If you want to enable case workers to add a copy of a Box document to the current case instead of referencing the document in Box , enable the Box copy optionfor the case management repository: Document sharing Enable the Box share option for your IBM Business AutomationWorkflow desktop and for each IBMFileNet Content Manager or IBM ContentManager repository that you want to share documentsfrom: IBM Business AutomationWorkflow desktop IBMFileNet Content Manager or IBM ContentManager repository If you want to share documents in existing solutions that were created before IBM Business AutomationWorkflow V5.2.1 Fix Pack 3, see the topic Adding Box Share menu actions for existing solutions . The Box Share and Delete Box Share menu actions are displayed by defaultin the Documents view.

| Feature                       | Procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Box as an external repository | Enable case types to support external documents. In Case Builder, edit each case type for which you want users to be able to add documents or attachments from Box and select Allow documents and attachments from repositories other than the case management object stores. This option is not required if you use Box only to share documents. If you want to enable case workers to add a copy of a Box document to the current case instead of referencing the document in Box, enable the Box copy option for the case management repository: In the IBM Content Navigator administration tool, click Repositories and open the IBM FileNet® Content Manager target object store that is used as the case management repository. On the Configuration Parameters tab, enable the Optional Features > Box copy option.                                                                                                                                                                                                                                                                      |
| Document sharing              | Enable the Box share option for your IBM Business Automation Workflow desktop and for each IBM FileNet Content Manager or IBM Content Manager repository that you want to share documents from:  IBM Business Automation Workflow desktop   In the IBM Content Navigator administration tool, click Desktops and open your IBM Business Automation Workflow desktop. On the General tab, enable the Box share services option and select the Box repository for shared files.   IBM FileNet Content Manager or IBM Content Manager repository   In the IBM Content Navigator administration tool, click Repositories and open each IBM FileNet Content Manager or IBM Content Manager repository. On the Configuration Parameters tab, enable the Optional Features > Box share option.    If you want to share documents in existing solutions that were created before IBM Business Automation Workflow V5.2.1 Fix Pack 3, see the topic Adding Box Share menu actions for existing solutions. The Box Share and Delete Box Share menu actions are displayed by default in the Documents view. |

5. Deploy your solution.