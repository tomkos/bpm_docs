# Stopping and restarting the deployment manager

## Before you begin

To use this page, your user ID must be
associated with the Administrator, Configurator, Operator, or Monitor
role.

## Procedure

1 Choose a method to stop the deployment manager. Method Actions Using the administrative console Using the command line

| Method                           | Actions                                                                                                                                                                                                                                                         |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Using the administrative console | Navigate to System Administration > Deployment Manager. Click Stop.                                                                                                                                                                                             |
| Using the command line           | Navigate to the deployment manager profile\_root/bin directory. Enter the stopManager command for your operating system.Note: If you do not specify the -username and -password command line parameters, the system prompts you to enter a user ID and password. |

2. Wait for verification that the deployment manager has stopped.
3. Navigate to the deployment manager profile\_root/bin
directory.
4. Enter the startManager command for your
operating system.

## What to do next