<!-- image -->

# Example: Monitoring events in the logger

## About this task

## Procedure

1. Open the administrative console.
2. In the navigation pane, click Servers > Application Servers.
3. Click server\_name.
4. Under Troubleshooting, click Logging and tracing
5. Click Change Log Detail levels
6. Select the Runtime tab.
7 Expand the tree for WBILocationMonitor.LOG.BR and you will see seven event types underthe WBILocationMonitor.LOG.BR.brsample.* element:
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount.ENTRY
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount.EXIT
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount.FAILURE
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount.SelectionKeyExtracted
    - WBILocationMonitor.LOG.BR.brsample\_module.DiscountRuleGroup.Operation.\_calculateDiscount.TargetFound
8. Click each of the events and select finest.
9. Click OK.
10. Switch the business rules sample application page, and run the application once.
11. Use a text editor to open the trace.log file located in the
profile\_root/logs/server\_name folder on your
system.

## Results

After completing this exercise, you should understand
how to select service component event points for monitoring to the logger. You have seen that the
events fired in this type monitoring have a standard format, and that the results are published as a
string in raw XML format directly to a log file. To view the published events, open the log file in
a text editor, and decipher the contents of individual events.

## What to do next