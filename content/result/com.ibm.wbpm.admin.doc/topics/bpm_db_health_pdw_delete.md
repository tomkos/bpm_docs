# Deleting old data from the Performance Data Warehouse database

## Using the Process Admin Console

1. Click Server Admin > Workflow
Admin > Health Management.
2. Select the command Prune PDW.
3. Specify the minimum age, in days, of the data to delete.
4. Click Submit.
5. After the request is submitted, you can check the progress of
the removal in the system log.

## Using a REST API call

Call
the operations REST API POST https://host:port/ops/std/bpm/pdw/prune.

```
POST https://host:port/ops/std/bpm/pdw/prune?age=30
```