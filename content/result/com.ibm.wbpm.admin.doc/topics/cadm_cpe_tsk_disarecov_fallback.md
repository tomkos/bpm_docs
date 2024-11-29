# Fallback to primary data center

## About this task

To bring the primary data center back to service, do the following steps:

## Procedure

1. Bring back up the primary database on the secondary data center.
2. Start the Content Platform Engine cluster in the primary data center.
3. From Content Platform Engine administrative console, enable the request forwarding to
route the request from Content Platform Engine site 2 to Content Platform Engine site1.
4. From Content Platform Engine administrative console, move back the database connection
from Content Platform Engine site 2 to Content Platform Engine site 1 by moving a site component
operation.
5. Restart all Content Platform Engine clusters in both primary data center and secondary
data center.
6. Restart the Business Automation Workflow servers in primary data center, keep the
Business Automation Workflow servers stopped in the secondary data center.