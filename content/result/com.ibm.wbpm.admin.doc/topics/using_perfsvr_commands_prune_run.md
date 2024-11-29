# Running the prune command

## Before you begin

Before you run the prune command,
complete the following tasks:

- Ensure that you have installed or upgraded your Performance Data
Warehouses to the latest version of Business Automation Workflow.
- Start the Performance Data Warehouse. If you are running in a
clustered environment, ensure that all servers in the cluster are
running.
- Create a backup of the performance database.
- Go to the following directory: install\_root\profiles\profile\_name\bin.Remember: perfDWTool must be run from an active node in the
support cluster.

## Command syntax

Run the prune command
by using the following syntax:

<!-- image -->

<!-- image -->

```
perfDWTool.sh -u user\_name -p password -nodeName node\_name  prune -daysOld number-of-days-old
```

<!-- image -->

```
perfDWTool.bat -u user\_name -p password -nodeName node\_name  prune -daysOld number-of-days-old
```

Where -daysOld indicates
the age of the data that should be removed. The age is based on the
current server time.

For example, suppose, at 4:00 p.m. on
October 24, you use the prune command with the -daysOld parameter
set to 2. All data that is older than October
22 at 4:00 p.m. is deleted.

- It can contain only numeric characters.
- It must be a value greater than 0.
- If you enter 0 or a negative number, or
if you include alphabetic or special characters, an error is returned.