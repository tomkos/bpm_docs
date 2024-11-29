# Failover to secondary data center

## About this task

To bring back the secondary data center to take over the working, do the following steps:

## Procedure

1. Start the secondary database on the secondary data center.
2. From Content Platform Engine administrative console, disable the request
forwarding.
3. From Content Platform Engine administrative console, move the database connection from
Content Platform Engine site 1 to Content Platform Engine site 2 by moving a site component
operation.
4. Restart Content Platform Engine cluster in secondary data center.
5. Start the Business Automation Workflow servers in secondary data center.