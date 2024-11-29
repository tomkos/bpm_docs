<!-- image -->

# Setting up a user interface for your human task

## About this task

A client delivers task-related information to a staff
member in the form of an interactive application. You can generate
various types of clients for your human tasks, and use the generated
clients to customize a user interface through which users can interact
with the tasks in the runtime environment. Or, you can use generated
clients to quickly demonstrate a human workflow, for example, as a
proof of concept or prototype.

Using the client generator, you
can generate clients for both stand-alone human tasks that exist independently
of a BPEL process, and inline human tasks that have access to the
execution context a BPEL process. You can create one client for all
the human tasks in a module, or generate one client per task. You
can also generate one client for all human tasks in multiple processes
or modules.

You might want to provide a choice of user interfaces,
clients with different functionality for different roles, or basic
clients that can be reused by changing their appearance.

User interfaces for your human tasks can make use of
several types of technology. The human task editor provides a User
Interface section to add technology-specific configuration settings
to a human task. For some of the client technology types included
by default, the corresponding property page allows the creation or
selection of visualization files that match the Business Object data
structure used by the human task.

- To create user interfaces for more than one task, the wizard is the more efficient choice, since
you can create user interfaces for multiple tasks, even if they are not in the same module. For JSF,
the wizard creates not only the generated artifacts but also stand-alone web applications to use the
generated artifacts.
- To work in a Heritage Process Portal space, create an
HTML-Dojo user interface and use it in the Task Information widget.

- Before you begin: Client types and prerequisites

When you create a human task, you need to define, configure, or generate a client type. Each of these client types has its own prerequisites.
- Defining user interfaces for a human task

In the Human Task editor, you can select the type of client, and configure properties such as inputs and outputs for the client. You can specify existing configurations, or define new ones. You can then generate a client.
- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)

You can get your human tasks to work in widgets in Heritage Process Portal spaces by generating an HTML-Dojo page interface.
- Integrating JavaScript in HTML-Dojo pages

You can integrate JavaScript functions to customize an HTML-Dojo page. An HTML-Dojo page is an HTML form that uses Dojo widgets.
- Preparing to extend generated JSF code

Before you can extend generated JSF code for a client, you must update the faces-config.xml file of the client to be enhanced to add support for the new human task.
- Customizing clients

You might want to customize the JSF client or WebSphere® Portal user interfaces for your human tasks.
- Design considerations for user interface generation

In IBM® Integration Designer, the tools and technologies used to generate user interfaces are continually changing and evolving. This topic presents some design points that you should consider when you are designing a user interface and choosing the client type that is best suited for your purposes.
- Deploying a generated client to an external runtime environment

After generating your client you have several choices for how to deploy it to the runtime environment.