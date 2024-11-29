# Configuring your system for case management

## Before you begin

- You have the Business Automation Workflow license. If you are
upgrading from IBM Business Process Manager
 (IBM BPM) or IBM Case
Manager, you must also upgrade your license to
Business Automation Workflow.
- You ran the createObjectStoreForContent command to create the design object store,target object store, and other necessary items before you can use the embedded. Or, if you alreadyhave an external Content Platform Engine and want to use it, youfollowed the instructions in Configuring an existing external Content Platform Engine . Similarly, if you have an externalIBM ContentNavigator and want to use it, you followedthe instructions in Configuring IBM Business Automation Workflow with an external IBM Content Navigator .Note: Case systems require multiple object stores. The required object stores differ between legacyIBM CaseManager environments and IBM Business AutomationWorkflow . Use the following methodology to create the minimal number of object stores that are needed tomeet the requirements specified above:

Case systems require multiple object stores. The required object stores differ between legacy
IBM Case
Manager environments and IBM Business Automation
Workflow.

    - Legacy IBM CaseManager environments require twoobject stores:
        - A design or staging object store
        - A target object store
- Business Automation Workflow case functions require three object stores:
    - A content object store (which must be initially empty)
    - A design or staging object store
    - A target object store

Use the following methodology to create the minimal number of object stores that are needed to
meet the requirements specified above:

1 When configuring case functions in Business Automation Workflow with a new embeddedContent Platform Engine , run thecreateObjectStoreForContent command once to create the following two object stores:
    - A design or staging object store – development environments have a design object store and
production environments have a staging object store.
    - A target object store
2. If the embedded Content Platform Engine is used, the content objectstore (docs) are created and
initialized on the first time startup of application clusters, so you do not need to create it
manually.
3. When configuring case functions in Business Automation Workflow with
an existing Content Platform Engine in order to integrate with the
repositories of an existing legacy case system, then the external Content Platform Engine server already has the design and staging stores and
the target object stores. It is not necessary to create them. Only the content object store needs to
be created, which is required for the case functions in Business Automation Workflow. The content object store should be hosted by the same
Content Platform Engine server as the other case-related object
stores. Use IBM Administration Console for
Content Platform Engine (ACCE) on the external
Content Platform Engine server to create the content object store. Do
not use the createObjectStoreForContent command.
4 Configure the object stores with a security master group, as a best practice documented for caseobject stores. Learn from the Case management in IBM Business Automation Workflow section what kind of security should beplanned and applied:

- To configure security for the design and target object stores, use the Content Platform Engine Security Script Wizard.
- To configure security for the content object store (docs), use the maintainDocumentStoreAuthorization command.
5. When configuring separate IBM Business Automation
Workflow environments with an
existing Content Platform Engine, it is
possible to configure separate IBM Business Automation
Workflow configurations with a
single FileNet P8 domain. The requirement is for all of the separate IBM Business Automation
Workflow configurations be on
the same product version. Each separate environment has its own set of unique object stores. Sharing
of object stores across the different IBM Business Automation
Workflow configurations is not
allowed.
- For detailed information about designing and configuring case management, see Case management in IBM Business Automation Workflow. It is also recommended that you verify your case applications by following the
instructions in the topic Verifying the case applications in the development environment.

## About this task

Your case management system consists of a development
environment for creating and testing case management solutions and
a production environment for working with running case management
solutions. You must configure both environments.

Configuring
the development environment includes configuring Case Builder and Case Client. Configuring
the production environment includes configuring only Case Client.

You
use the BPMConfig command to create a profile for
each development environment instance and a profile for each production
environment instance. You then use this profile to run the configuration
and deployment tasks in the Case configuration tool.

- You are using the embedded Content Platform Engine server
and intend to integrate with Box.
- You are using an external Content Platform Engine server.

After you edit the profile, save your changes and then
run the task. The data that you enter in the graphical user interface
is saved in XML files, but you do not directly edit the files.

If
you use the command-line version of the Case configuration tool, you
must directly edit the XML files that store the values for the task.
The XML files contain the properties and values that describe the
associated configuration and deployment tasks. Three XML files contain
the information that is common to all tasks in the profile, and each
configuration task in the profile has one configuration XML file.

Configure security by assigning permissions to different users, groups, and roles to determine
the areas and objects of a solution in a FileNet® P8 object store that these users can access. See
the section Configuring security for IBM Business Automation Workflow
solutions.

1. Configuring the development environment for case management

Configure the development environment before you use IBM Business Automation Workflow to create and deploy solutions. Before you move them into a production environment, use the development environment to create, modify, and test solutions.
2. Configuring the production environment for case management

You must configure the production environment before you deploy your solutions to production. You configure the production environment after you configure the development environment.
3. Configuring your case management system for federation

To enable users to work with case instances in Workplace on-premises in a federated environment, case instances need to be indexed so that case data is included in the Process Federation Server federated data repository index.

## Related information

- Enabling the case management features