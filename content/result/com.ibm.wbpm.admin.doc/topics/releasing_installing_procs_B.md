# Building a custom deployment service flow

## Before you begin

## About this task

- Create or update database tables
- Update necessary environment variables
- Determine which snapshots are already installed
- Migrate individual process instances
- Create custom time schedules

For example, you can customize a deployment service flow to create tables on the target process
server to hold data such as the options for drop-down menus that exist in your process app. When you
need to add to or change those menu options, you can modify the service flow so that those database
updates are handled automatically during installation.

If your deployment service was created for a process application in desktop Process Designer, you must first convert it to a
deployment service flow in the Process Designer
before customizing it. For more information, see Converting heritage services.

## Procedure

To add functionality to a deployment service flow, complete the following
steps:

1. In the Process Designer, open the process
app or case solution that contains the deployment service flow.
2. From the Services > Deployment Service Flow category, open the deployment service flow.
3. In the diagram that opens, add the service calls and scripts
that you need for your particular installation.
4. Save your changes.