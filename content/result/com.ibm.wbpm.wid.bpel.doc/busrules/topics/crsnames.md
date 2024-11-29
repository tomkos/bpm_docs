<!-- image -->

# Using rule set names in a rule group

- http://www.yourNamespace.com/default/getDiscountRate
- http://www.yourNamespace.com/holiday/getDiscountRate

If you reference these rule sets within a single operation, only
the local name for the rule set is shown, so the references may appear
identical in both the tool and the web environments.

| Label               | Name            |
|---------------------|-----------------|
| Default             | getDiscountRate |
| July 1 to August 31 | getDiscountRate |

- http://www.yourNamespace.com/getDefaultDiscountRate
- http://www.yourNamespace.com/getHolidayDiscountRate

If you do this, the names will be unambiguous, and there will not
be any confusion.

| Label               | Name                   |
|---------------------|------------------------|
| Default             | getDefaultDiscountRate |
| July 1 to August 31 | getHolidayDiscountRate |

## Related concepts

- Rule group editor

## Related tasks

- Specifying the rule logic for a rule group
- Scheduling rules using the rule group editor
- Customizing algorithms for date and time selection
- Creating custom selectors