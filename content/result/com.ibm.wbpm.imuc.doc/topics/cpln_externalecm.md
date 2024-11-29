# Planning for an external Content Platform Engine

Business Automation Workflow contains the
BPM document store as a content
repository that is used for Business Automation Workflow documents. This internal
BPM document store is
automatically configured. Its usage is restricted so that it cannot be integrated with all existing
IBM Content Foundation products.

Plan to use an external Content Platform Engine under the following
conditions:

- You intend to use case management.
- You have an existing Content Platform Engine that you want to use with
Business Automation Workflow.
- You want to retain artifacts that will persist longer than six months, such as documents and
cases.
- You intend to use Content Platform Engine for documents (in
addition to cases and processes).
- You have an upgrade to an existing IBM Case
Manager
installation.
- You want to build integrated solutions that use IBM Content Foundation products.

When you use an external Content Platform Engine as the content repository
for the BPM document store, you
can build integrated solutions that use other IBM Content Foundation products. For example, you can
use Content Navigator as a content-centric user interface or IBM Datacap to capture documents that
come from your customers. Capturing these documents can automatically start a case. For more
information, see IBM Content
Foundation.

<!-- image -->

You can author applications in the same way with an external content repository. All integration
functions used with the BPM document store also work in the same
way.

- Business Automation Workflow documents
can be accessed with JavaScript, web services, and REST APIs.
- Content integration steps can be used as in the predefined BPM document store server definition.
Content integration steps can also be used as in the BPM content store server definition,
if you have the Basic Case Management feature from a previous release installed.
- Coach views from the Content Management toolkit can be used with one of the predefined server
definitions without any difference for either the embedded or external content repository.

To use an external FileNet® Content
Manager installation as
a content repository for the BPM document store, you must have a common
user repository. The repository must contain the users that work with your applications. This
repository is an enterprise-wide Lightweight Directory Access Protocol (LDAP) repository that
contains all the users and groups. The FileNet Content
Manager must be set up
on a WebSphere Application Server.

Each Business Automation Workflow
deployment environment that you want to integrate with an FileNet Content
Manager installation
must have its own dedicated object store. To get your Business Automation Workflow deployment environment to
use an object store in the external FileNet Content
Manager installation,
you can configure your Business Automation Workflow deployment environment to
use empty object stores in an external FileNet Content
Manager installation.
This configuration is useful if you set up a new Business Automation Workflow deployment environment.
If the embedded content repository in your Business Automation Workflow deployment environment
has data, it will be lost when you configure an external FileNet Content
Manager. For information
on how to configure this option, see Configuring an existing external Content Platform Engine.

## Frequently asked questions

The following list provides some common FAQs relating to an external Content Platform Engine:

- How is the existing data handled in the embedded content repository that exists before switching
to an external FileNet Content
Manager server? The
existing data in the embedded content repository is lost after switching to an external FileNet Content
Manager server.
- How is the existing data handled in the external FileNet Content
Manager server? The
existing data in the external FileNet Content
Manager server is not
affected.
- How is the database for the external FileNet Content
Manager server
configured?The database for the external FileNet Content
Manager server is
configured with the FileNet Configuration Manager utility. It is not configured in Business Automation Workflow.
- Are there constraints when you use the user registry? All users and groups that are
referenced by the object store must be defined in a shared user registry to work with Business Automation Workflow and the FileNet Content
Manager installation.
Your applications that use content function must use only users and groups from the shared user
registry. Non-shared users or groups, for example, from an internal file repository, are not able to
work with the content. The EmbeddedECMTechnicalUser authentication alias, which is used by Business Automation Workflow to access the external
ECM with administrator privileges, must refer to a user from the shared user
repository.
Business Automation Workflow and Content Platform Engine must have
the same registry for achieving single-sign on (SSO). For example, Business Automation Workflow and Content Platform Engine could both have federated
repositories such as the Virtual Member Manager (VMM) repositories. A combination of Business Automation Workflow with VMM and Content Platform Engine with a stand-alone LDAP
is not supported by IBM WebSphere® Application
Server. If using shared LDAP
repositories, they must be added to the WebSphere federated repositories on both the Content Platform Engine, as well as IBM Business Automation
Workflow.
- Is it possible to share the same FileNet P8 domain with separate Business Automation Workflow environments?When
configuring separate IBM Business Automation
Workflow environments with an
existing Content Platform Engine, it is
possible to configure separate IBM Business Automation
Workflow configurations with a
single FileNet P8 domain. The requirement is for all of the separate IBM Business Automation
Workflow configurations be on
the same product version. Sharing of object stores across the different IBM Business Automation
Workflow configurations is not
allowed.

## Considerations for object store configuration

- Design Object Store (DOS): The object store used by case management to store design data.
- Target Object Store (TOS): The object store used by case management for storing runtime
data.
- Workflow Document Store (DOCS): The object store used by workflow processes to store
documents.

If you configure the object stores incorrectly initially, the add-ons for the object stores are
installed incorrectly, which might leave your system in an unsupported state. Object store add-ons
cannot be undone. To recover from this situation and correct any other potential missteps, you must
rebuild the environment and recreate the profile.

## Related information

- Configuring a new external Content Platform Engine
- Configuring an existing external Content Platform Engine
- Maintaining an external Content Platform Engine configuration
- Management of folders and documents for ECM systems