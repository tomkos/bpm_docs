# Creating custom KPIs

## About this task

## Procedure

1. Open a process application in the Designer view.
2. Click the plus sign next to Performance and select Key
Performance Indicator from the list.
3. In the New Key Performance Indicator window,
type a descriptive name for the new KPI and click Finish.
4. Provide a description for the KPI in the Documentation field.
5. In the Details section of the window, select the
Unit for the KPI from the drop-down list.
For example, if your company assembles cell phones and you want to measure the number of
phones in production, select Count from the drop-down list.
6. To roll up the unit you are tracking into a higher-level KPI, click
Select to choose the KPI that you want. IBM Business Automation Workflow displays the KPIs in the current process
application and any KPIs in referenced toolkits, including the System Data toolkit. 
For example, select the standard KPI, Resource Cost, to roll the
Count KPI from the previous step into a higher-level KPI.
You can click New to create a new KPI. Click the
X icon to remove a roll-up KPI.
7. In the Roll-up multiplier field, specify the value by which to multiply
the unit that you are tracking before the data is collected in the roll-up KPI.
For example, to obtain an accurate Resource Cost for the previous
step, enter the value of each cell phone in the Roll-up multiplier field.
Rolling up to higher-level KPIs is useful when you create SLAs. The Resource Cost example in this
procedure shows how to create an SLA for a condition where the cost of resources in production was
either too high or too low.
8. Click Save.