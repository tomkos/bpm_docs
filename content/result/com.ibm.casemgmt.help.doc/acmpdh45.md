# getTaskPropertyValues operation

| Parameter         | Type     | Description                                                                                                               |
|-------------------|----------|---------------------------------------------------------------------------------------------------------------------------|
| taskId            | String   | The task ID, which can be the current task that is obtained by passing the F\_CaseTask, or an explicit ID of another task. |
| taskPropertyNames | String[] | The list of task properties to retrieve.                                                                                  |
| return\_value      | String[] | The TaskPropertyValues value is an array of strings, containing the property values of the requested properties.          |