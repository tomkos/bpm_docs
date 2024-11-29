# Alert definitions and alerts

- A set of pages in the Process Admin Console in which you create
alert definitions.
- A set of REST and JavaScript APIs
that provide access to the alerts generated from the alert definitions.

## Alert definitions

In the Process Admin Console, there is an Alert Definitions group. Within
the group is a list of pages in which you can create and maintain alert definitions. The pages let
you define alerts to monitor the number of business process application instances and tasks
respectively. An alert definition consists of a name that identifies the definition, the name of the
process application and snapshot being monitored, the threshold value that triggers an alert, and an
operator. You can also target the alert for a specific state such monitoring the number of completed
instances. The page contains a table that lists the existing alert definitions, as well as the
fields that are used to create an alert definition or modify an existing one.

<!-- image -->

## REST and JavaScript APIs

The
REST and JavaScript APIs
for the BPM alerts provide access to the alerts generated from the
alert definitions. By using the APIs, applications can have user interfaces
that display the alerts, code to create emails, or have some other
way of notifying administrators.

You can use the APIs to create an application or service based on requirements such as sending
emails or providing a user interface. When you are creating the application or service, you can set
how often the application or service checks for alerts. Keep in mind that each check puts a load on
the system so you must balance the importance of immediately knowing about an alert condition
against the impact on performance. The check can also vary for different alert definitions because
the APIs let you check for specific alerts separately. You can also change the impact on performance
by having higher-priority alerts checked more frequently compared to lower-priority alerts.