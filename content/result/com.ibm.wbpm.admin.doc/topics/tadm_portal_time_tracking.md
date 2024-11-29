# Disabling the display of time tracking information in Process Portal

## About this task

| Setting               | Default Value   | Description                                                                        |
|-----------------------|-----------------|------------------------------------------------------------------------------------|
| Display-time-tracking | true            | Option to display the time tracking information for individuals in Process Portal. |

```
<server merge="mergeChildren">
  <portal merge="mergeChildren">
    <display-time-tracking merge="replace">true</display-time-tracking>
  </portal>
</server>
```

For more information about making changes in the 100Custom.xml file, see
The 100Custom.xml file and configuration.