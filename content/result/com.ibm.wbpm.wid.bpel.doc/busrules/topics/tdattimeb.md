<!-- image -->

# Scheduling rules using the rule group editor

## About this task

## Procedure

1. In the rule logic area of the rule group editor, create
a new Scheduled Rule Logic by clicking the  icon.
Date fields will appear showing the current date.
2. To set a start or end date, click the appropriate  calendar
icon.
3. Select a date in the interactive calendar. To
set it to the current date, click Today, or
to leave either the start or end date open (perhaps you do not want
it to expire), then click No Date.
4. In the Rule Logic column, click Enter Rule Logic to
create a new rule, or select an existing one.

## Standards for date and time selection in a rule group

There
are a number of ways you can configure your rule group. Here are some
suggestions that are based on the number and nature of the available
rule logic. In a rule group, date based selection can be used to delegate
one operation to a specific rule logic (note that overlapping rules
are not supported, and only one can be called at a time).  The date
selection data is composed of a set of rule logic rows and one default
rule logic.

If there is only one rule logic for this rule group, it is
recommended that you select it in the default rule logic, and leave
the dates empty.

If there are two rule logics one of which represents the current
behavior and the other one the future behavior of the rule group,
it is recommended that you create two date rows in the table and leave
the default rule logic undefined.

If there is some standard behavior for the rule group, which
is occasionally overridden for short durations, it is recommended
that you use the default rule logic for the standard behavior and
create a date range for each of the short term behavior rule logics.

## Related concepts

- Rule group editor
- Using rule set names in a rule group

## Related tasks

- Specifying the rule logic for a rule group
- Customizing algorithms for date and time selection
- Creating custom selectors