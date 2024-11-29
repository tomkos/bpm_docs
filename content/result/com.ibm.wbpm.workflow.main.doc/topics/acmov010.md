# Case health analysis

## Enabling case health analysis

Depending on whether you upgraded to IBM Business Automation
Workflow or installed it
without upgrading, you may need to enable or disable the case health analysis feature or possibly
even install it. More information is found in the topic Enabling or disabling case health analysis .

In Business Automation Workflow V19.0.0.1
and later, the case health analysis feature is disabled by default.

## How is case health determined?

For a case
that has stages, Case Client first
calculates the expected time frame for case completion based on the
aggregate duration of the stages. Case Client then compares
the time that is already spent on the case to the expected duration.
If the case cannot be completed within the expected time frame, the
case health is always set to poor.

<!-- image -->

For historical case health analysis, IBM Business Automation
Workflow requires that the
aggregate data for a case type includes statistical data from many completed cases. IBM Business Automation
Workflow does not perform the
historical analysis until enough historical data is available.