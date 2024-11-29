# Creating a process

## About this task

A business process typically contains activities that are performed by various users or teams. At
run time, a business user works with tasks that are created for the activities.

The following diagram illustrates the main tasks and activities that are associated with creating
processes.

<!-- image -->

The activities in a process can access documents that are stored in a content management system.
When you create a process, you decide how you want to access these documents.

You create a process from the Processes category in the library.

## Procedure

1. Select Processes from the library. Click +.
In the Processes menu, select Process.
2. In the New Process dialog, enter a name for the
process.
3. Click Finish. The editor opens in the
Overview page. The process that you created is added in the
Processes category. An inline user task is automatically created for you and
added to the process.
4 Optional: In the Overview page,
    - Use the Documentation field to add information about the process that you
want to share with your development team.
    - If the process is generated from Case Builder, select
Automatically sync shared business objects to ensure the content object is
synchronized properly in the process instance.
    - Because shared business objects are passed by value with a reference, which means that changes
you make are saved and propagated to other instances that work with the same data, enable the
automatic save and data synchronization functions by selecting Automatically sync shared
business objects in the process or service.
5. Assign teams whose members can start a process, or instance owner teams whose members can work
with tasks at run time. 
See Assigning teams to a process.
6. Create the variables for the information that you want to share across
activities.
7. In the Definition page, add activities that define the business
tasks and wire them according to the workflow.
8. Create user interfaces for the process. See Creating user interfaces for processes.

## Results

When you create a process, an inline user task is automatically added that is ready to run (if a
dependency exists between the process app and the UI toolkit). Information about inline user tasks
is found in the topics Working with inline user tasks and Configuring coach templates for inline user tasks.

- Implementing activities in a process

Choose the implementation for each activity in your process and set the required properties.
- Creating an unstructured (ad hoc) activity

An ad hoc activity is not part of the structured process; it is an activity that a business user can run as needed. An ad hoc activity has no input wires and is started according to predefined preconditions, rather than by a predefined process flow. Such activities can be required or optional, and they can be defined as repeatable or to run at most once.
- Converging and diverging process flows with gateways

Gateways control the divergence and convergence of a sequence flow, determining branching and merging of the paths that a process can take at run time.
- Task types

Learn more about the task types that are available when modeling processes.
- Modeling subprocesses

You can use a subprocess  to encapsulate logically related steps within a parent process. Steps in a subprocess can directly access business objects (variables) from the parent process. No data mapping is required. However, unlike a linked process, a subprocess can be accessed and instantiated only from the parent process, and it is not reusable by any other process or subprocess.
- Modeling events

Events can be triggered by a due date passing, an exception, or a incoming message from an external system. You can add events that can occur at the beginning, during, or at the end of a process. Use events to track data, manage errors, and retrieve information about the execution of your processes.
- Undercover agents

An undercover agent (UCA) is attached to a message event or a content event in a process or business process definition (BPD) and calls a service to handle the event.
- Assigning teams to a process

You can assign a team whose members can start a process, or an instance owners team whose members can work with the process at run time in Process Portal.
- Assigning teams to user tasks

For activities that are implemented as user tasks, you can designate the users who receive the runtime task by using the Assignments page in the properties for the user task.
- Starting a process

A process or subprocess starts when its start event receives a trigger such as a message or document. You configure the type of the start event depending on the origin of the trigger. You can include multiple start events in your process to start the process in  different ways. For example, a process might start when a customer submits an online complaint form or when a customer service representative initiates the process in response to a customer call.
- Creating user interfaces for process instances

Create user interfaces that a user sees for the process instance at run time.
- Making process instance user interfaces reusable

You can create a custom user interface for your process instance, and reuse the interface     for other processes.
- Visualizing process data

Use the data visualization option in the designer to create a visual representation of a selected process. The visualization is displayed in a new web browser window. It contains the web-based diagram view of the process. Select the required data variables or tag groups that you want to visualize on the left side in the browser window.
- Converting BPDs to processes

Convert business process definitions (BPDs) to processes so that you can work with them in the Process Designer.
- Instance names in BPDs and processes

When the flow of an instance progresses from a parent BPD to a child linked BPD, the instance name changes to reflect the child linked BPD. However, when the flow of an instance progresses from a parent process to a child process, the instance retains the name of the parent process.
- Selecting Business Automation Workflow or an external ECM system to manage folders

You choose a folder to manage your Enterprise Content Management (ECM) documents and subfolders. This folder can be on IBM Business Automation Workflow or an external Enterprise Content Management system.
- Management of folders and documents for ECM systems

When you build a process, the Enterprise Content Management (ECM) folders and documents is managed by IBM Business Automation Workflow using the BPM document store as a repository.
- Changing the way enterprise content is accessed

The activities in a process can access documents that are stored in an Enterprise Content Management system (ECM). If your process accessed content with the Basic Case Management feature in a previous release, you must change the content management method to IBM BPM. When you make the change, you lose some information that you must recover manually.
- Migrating case types

Before you can edit case types that were created in previous versions of IBM Process Designer, you must convert them to processes. A process provides all the capability of both case types and BPDs.
- Managing external files

External files are images, style sheets, JAR files, or other assets that are part of a workflow implementation but that are developed outside of the designer. You can add these external files to your process application or toolkit in the Designer view so that all project assets are included in the repository.