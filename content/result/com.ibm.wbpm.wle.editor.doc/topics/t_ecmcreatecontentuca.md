# Creating and configuring an undercover agent for a content
event

## Before you begin

The following procedure describes how to create a content
undercover agent without consideration for some of the other components
that are required to detect and respond to ECM events, such as an
event subscription. If you need to create a content undercover agent
and all of the other required components as well, you should follow
the instructions in the topic Subscribing to document and folder events.
This end-to-end approach is a simpler approach than creating each
component on a stand-alone basis. It automatically creates some resources
that you would otherwise need to create manually.

## Procedure

1. Open the designer.
2. To launch the New Undercover Agent, click the plus
(+) icon beside Events and then select
Undercover Agent. The New Undercover Agent wizard
opens.
3 Configure the content undercover agent by completing thefollowing steps in the undercover agent editor:
    1. Beside the Event Marker area, click
Select and then select Content. (Use the
Content selection to work with content events that originate from ECM
servers. By comparison, the Message selection is used to work with message
events that originate from processes, service flows, JMS listeners, or web services that you have
created.)
    2. Beside the Implementation area,
accept the default selection Variable or select Service (if
necessary). Use a variable implementation to pass events directly
from the undercover agent to the process. Use a service implementation
to process information about events by adding business logic or decisions.
    3. If you accepted Variable as your
implementation, the default variable type ECMContentEvent is
used and it cannot be changed.
    4. If you selected Service as your
implementation, the default attached service Default ECM
Event is already selected. However, you can click Select beside
the Attached Service area and choose a different
attached service for the undercover agent.
    5. Ensure that the Enabled check
box is selected, which enables the content undercover agent to run.
    6. In the Parameter Mapping section,
select the Use Default check box if you want
to use the default value of the input variable in the attached service.
If the input variable of the attached service does not have a default
value, this check box is disabled. You can type a value in the field
to manually map a constant value to the input variable of the attached
service. For example, you might use a constant for testing purposes.
    7. If you accepted the Content event
marker and you need to create an event subscription for the undercover
agent, click Add Event Subscription and follow
the instructions in the topic Subscribing to document and folder events.
4. Click Save or Finish Editing.
5. Click Run Now to test the content undercover agent and monitor
it as described in Maintaining and monitoring IBM Business Automation Workflow Event Manager.

## Results

The new configured content undercover agent is displayed
in the Undercover Agents section of the Implementation
library list.