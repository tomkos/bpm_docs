# Making multiple changes to process instance values in Process Portal

## Procedure

1 In the Gantt View page for a processinstance, click Batch Modify . Restriction: If the process instance containsa group of parallel tasks, you might not be able to change individualtasks within the group in the Batch Modify window. The followingtable describes the available settings:Table 1. Task settingsthat you can modify in batch If you select... Then specify... And then apply the update to... For... Reset to Current Which of the following values you want to resetto the current value: Changed values or only critical path values. Activities, Active Tasks, or Activities andActive Tasks Decrease Duration by % The numeric percentage by which you want todecrease the duration All values, changed values, unchanged values,or only critical path values Activities and Active Tasks Decrease Amount The setting that you want to decrease (durationor due date) and the value for the amount. For the value that youspecify, the duration or due date is decreased by that number of days.For example, if you specify 10 , the duration or duedate is decreased by 10 days. All values, changed values, unchanged values,or only critical path values Activities, Active Tasks, or Activities andActive Tasks Increase Duration by % The numeric percentage by which you want toincrease the duration All values, changed values, unchanged values,or only critical path values Activities and Active Tasks Increase Amount The setting that you want to increase (durationor due date) and the value for the amount. For the value that youspecify, the duration or due date is increased by that number of days.For example, if you specify 10 , the duration or duedate is increased by 10 days. All values, changed values, unchanged values,or only critical path values Activities, Active Tasks, or Activities andActive Tasks Set Value The setting that you want to change (duration,due date, or priority), and the value for that setting. For durationand due date, you can specify days. If you specify only a value, theduration or due date is set to that number of days. For example, ifyou specify only 10 , the duration or due date isset to 10 days. For priority, you can choose the new priorityfrom the list. All values, changed values, unchanged values,or only critical path values Activities, Active Tasks, or Activities andActive Tasks

| If you select...       | Then specify...                                                                                                                                                                                                                                                                                                                                                                            | And then apply the update to...                                            | For...                                                   |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------|
| Reset to Current       | Which of the following values you want to reset to the current value:  Duration Due Date Priority                                                                                                                                                                                                                                                                                          | Changed values or only critical path values.                               | Activities, Active Tasks, or Activities and Active Tasks |
| Decrease Duration by % | The numeric percentage by which you want to decrease the duration                                                                                                                                                                                                                                                                                                                          | All values, changed values, unchanged values, or only critical path values | Activities and Active Tasks                              |
| Decrease Amount        | The setting that you want to decrease (duration or due date) and the value for the amount. For the value that you specify, the duration or due date is decreased by that number of days. For example, if you specify 10, the duration or due date is decreased by 10 days.                                                                                                                 | All values, changed values, unchanged values, or only critical path values | Activities, Active Tasks, or Activities and Active Tasks |
| Increase Duration by % | The numeric percentage by which you want to increase the duration                                                                                                                                                                                                                                                                                                                          | All values, changed values, unchanged values, or only critical path values | Activities and Active Tasks                              |
| Increase Amount        | The setting that you want to increase (duration or due date) and the value for the amount. For the value that you specify, the duration or due date is increased by that number of days. For example, if you specify 10, the duration or due date is increased by 10 days.                                                                                                                 | All values, changed values, unchanged values, or only critical path values | Activities, Active Tasks, or Activities and Active Tasks |
| Set Value              | The setting that you want to change (duration, due date, or priority), and the value for that setting. For duration and due date, you can specify days. If you specify only a value, the duration or due date is set to that number of days. For example, if you specify only 10, the duration or due date is set to 10 days. For priority, you can choose the new priority from the list. | All values, changed values, unchanged values, or only critical path values | Activities, Active Tasks, or Activities and Active Tasks |

2. Click Update Values. 
The Changes section shows the results
of the updates.
3. Review the pending changes to the values. When
you change the duration or due date of an activity or a task, the
durations and due dates of all subsequent activities and tasks in
the projected path that are affected by the change are updated accordingly.
4. Click Save to commit the changes.