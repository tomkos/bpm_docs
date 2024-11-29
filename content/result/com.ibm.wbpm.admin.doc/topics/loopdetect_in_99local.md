# Detecting infinite loops in services and process instances

| Property                 | Default Value                                              | Description                                                                                                       |
|--------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| loop-detection-exception | false                                                      | If set to true, causes the service engine to stop the service and generates an exception when a loop is detected. |
| loop-detection-duration  | For service-engine: 120 seconds For bpd-engine: 60 seconds | The duration in seconds until the potential looping is reported. The value -1 makes the duration unlimited.       |

```
<server>
   <service-engine merge="replace">
	<loop-detection-duration>120</loop-detection-duration>
	<loop-detection-exception>false</loop-detection-exception>
   </service-engine>

   <bpd-engine merge="replace">
	<loop-detection-duration>60</loop-detection-duration>
   </bpd-engine>
</server>
```

- CWLLG0872W: Service '{0}' has been running for {1} seconds and might be in an
infinite loop.
- CWLLG0873W: Service '{0}' for instance {1} has been running for {2} seconds and
might be in an infinite loop.
- CWLLG0874E: Service '{0}' was terminated after {1} seconds because it might be
in an infinite loop.
- CWLLG0875E: Service '{0}' for instance {1} was terminated after {2} seconds
because it might be in an infinite loop.

If process instances are not in an infinite loop but the following message is in the
SystemOut.log, consider changing the loop-detection-duration
values for the BPD engine: CWLLG0871W: Business process definition (BPD) instance
{0} has been running for {1} seconds and might be in an infinite loop.