<!-- image -->

# Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)

## Procedure

1 In the Business Integration view, right-clickthe human tasks for which you want to generate a user-interface, andselect Generate Human Task User Interfaces . To generate a client for tasks in different modules, selectthose modules in the business integration view by holding the Ctrl keywhile you select each one. The User InterfaceWizard for Human Tasks launches.Note:
    - If the generated client is intended to be able to start a process,
then this process must have a human task defined for the initial receive
activities, or you must have another initiating task on the assembly
diagram wired to the process .
    - If the human task is not represented on your assembly diagram,
then you will get a warning message.
    - If a humans task contains an error of any kind, the task will
not be listed in the wizard. A warning message will be shown.
2 On the Client Generator Selection page, proceed as follows:

1. In the Generator type field, choose HTML-Dojo pages for
Process Portal spaces.
2. Use this list to choose the human tasks for which you want to generate the client. Expand the
tree until you find the required human tasks, and then select the associated check boxes.
3. Decide on the type of form that you want to use for the human task, and indicate whether you
want to overwrite existing interface settings.
If you select HTML, you also need to indicate the web project where the
HTML pages are saved.
4. Click the Browse to see a list of web projects. In the resulting window
you can choose from the list of web projects, create a folder within an existing web project or
create a web project.
5. Click Finish.

Important: When you generate an HTML-Dojo user interface for a human task, the interface
you generate can contain a calendar date type. The calendar that is used to enter data in this field
is controlled by the calendar type that you specified in the Business Integration preferences. In
the Business Integration perspective, click Window >  Preferences. In the Preferences navigation pane, expand Business Integration and then click
Calendar. Set the calendar type to the one for which you are generating the
human task interface.

## Related concepts

- Before you begin: Client types and prerequisites

## Related tasks

- Defining user interfaces for a human task
- Integrating JavaScript in HTML-Dojo pages
- Preparing to extend generated JSF code
- Customizing clients
- Deploying a generated client to an external runtime environment

## Related reference

- Design considerations for user interface generation