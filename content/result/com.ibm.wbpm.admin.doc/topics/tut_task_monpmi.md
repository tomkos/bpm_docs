<!-- image -->

# Example: Monitoring service component performance

## About this task

## Procedure

1. Open the administrative console.
2 Select the cluster or server to monitor.
    - To monitor a cluster, click Servers > Clusters > WebSphere application server clusters > cluster\_name.
    - To monitor a single server, click Servers > Server Types > WebSphere application servers > server\_name.
3. Click the Runtime tab.
4. Under Performance, click Performance Monitoring Infrastructure.
5. Select Custom.
6. Expand WBIStats.RootGroup > BR > brsample\_module.DiscountRuleGroup > Operation.
7. Select \_calculateDiscount.
8. Select the check boxes next to BadRequests, GoodRequests, and ResponseTime.
9. Click Enable.
10. In the navigation pane, click Monitoring and Tuning > Performance Viewer > Current Activity.
11. Select the check box next to server\_name, then click Start
Monitoring.
12. Click server\_name.
13. Expand WBIStats.RootGroup > BR > brsample\_module.DiscountRuleGroup > Operation.
14. Select the check box next to \_calculateDiscount.

## Results

Run the
business rules sample application several times, and then watch the performance viewer as it
periodically refreshes. Notice that there are now lines on the graph, representing the cumulative
number of successful requests and the average response time for each successful request. You can
also see the values next to the name for each statistic. The line for the number of successes should
continue to rise as you perform additional invocations of the sample, while the response time line
should level off after a few refreshes.

After you have completed this example, you should
understand how IBM® Business Automation Workflow implements
performance monitoring of service components. You should know how to select service components for
monitoring, and how the performance statistics are calculated. You will also be able to start the
performance monitors, and view the performance measurements for your applications as they are being
used.

## What to do next