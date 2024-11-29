# Configuring the default duration for projected path discovery
in Process Portal

## Before you begin

## About this task

| Property                             |   Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| calc-all-paths-processing-time-limit |        20 | Limits the amount of time (in seconds) that  Process Portal spends trying to calculate the critical path. If a projected path cannot be determined during this time, the Gantt chart does not display any future tasks. For all future instances of the BPD, the Gantt chart does not include any future tasks either. If the value is updated and the server is restarted, the projected path will be reevaluated for the next instance that is started. |

```
<common>
  <critical-path>
    <calc-all-paths-processing-time-limit merge="replace">20</calc-all-paths-processing-time-limit>				
  </critical-path>
</common>
```

For information about making and deploying 100Custom.xml configuration
changes, see Creating a 100Custom.xml configuration file.