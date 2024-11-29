# Tuning authorization performance for Process Portal

## About this task

| Property                          | Default   | Description                                                                                                                                                                                                                                                                                  |
|-----------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| optimize-group-membership-lookups | true      | Optimizes the authorization lookups that impact both user actions, such as claiming tasks, and system actions, such as refreshing the task list in the Work dashboard. To enable the improved performance, the property is by default set to true. It is not recommended to set it to false. |

```
<common>
   <security>
      <optimize-group-membership-lookups merge="replace">true</optimize-group-membership-lookups>
   </security>
</common>
```

For information about making and deploying 100Custom.xml configuration
changes, see Creating a 100Custom.xml configuration file.