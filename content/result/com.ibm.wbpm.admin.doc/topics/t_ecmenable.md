# Enabling or disabling event subscriptions

## About this task

## Procedure

1. Launch the Process Admin Console.
2 Open the Installed Apps page andthen click the Event Subscriptions tab. TheEvent Subscriptions tab opens and displays the following sectionsand subsections:
    - One expandable section for each type of event subscription, such
as ECM event subscriptions.
    - Within each event subscription section, one subsection for each
server that is defined for the process application.
    - Within each server subsection, a table that lists the event subscriptions
for the server.
3. Expand the section for an event subscription type. For
example, ECM event subscriptions.
4. Expand the subsection for the appropriate ECM server. The subsection contains a table
that lists all of the event subscriptions for the ECM server and indicates whether they are enabled
or disabled. By default, all event subscriptions display their state of enablement or disablement
after installation.

The BPM content store
supports all Content Management Interoperability Services (CMIS) operations. It is used for
developing case management applications. Event subscriptions include documents and folders when you
use the BPM content store as
the target server. It is only available in IBM® Business Process Manager
Advanced.
5 Complete one of the following steps: As soon as a check box is selected or cleared, the enabled ordisabled state of the event subscription is reflected in the databaseand it is applied at run time.

- If you want to disable any of the event subscriptions that are listed in the table, clear
Enabled next to each event subscription that you want to disable. The enabled
or disabled state of the event subscription will be cleared when the process application is
de-activated.
- If you want to enable any of the event subscriptions that are listed in the table, select
Enabled next to each event subscription that you want to enable. The enabled
or disabled state of the event subscription will be cleared when the process application is
activated.Note: To enable an event subscription, the corresponding server settings must be correct.
If you receive a message that implies that the server is not connected, click the
Servers tab and then click Test Connection to test and
subsequently correct the server settings.