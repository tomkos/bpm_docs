<!-- image -->

# Ownership patterns

Ownership patterns do not apply to invocation tasks.

| Single ownership   | Single ownership   | Parallel ownership   | Parallel ownership   |
|--------------------|--------------------|----------------------|----------------------|
| Start state        | End state          | Start state          | End state            |
| Ready              | Claimed            | Subtask started      | Ended                |
| Ready              | Ended              | Subtask started      | Ended                |
| Claimed            | Ended              | Subtask started      | Ended                |

- Selecting a calendar type for the completion conditions

Change the calendar type for the completion criteria by modifying the duration properties of the human task.