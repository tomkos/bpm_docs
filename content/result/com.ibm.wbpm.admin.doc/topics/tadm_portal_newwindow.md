# Opening services in Heritage Process Portal in a new
browser window (deprecated)

## Before you begin

## About this task

| Property                     | Default   | Description                                                                                                                     |
|------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| launch-in-new-window-enabled | false     | Provided to support the Quirks mode in Internet Explorer 10 and 11, this property forces tasks to open in a new browser window. |

```
<server>
 <portal>
    <launch-in-new-window-enabled merge="replace">true</launch-in-new-window-enabled>
 </portal>
</server>
```

For information about making and deploying 100Custom.xml configuration
changes, see Creating a 100Custom.xml configuration file.