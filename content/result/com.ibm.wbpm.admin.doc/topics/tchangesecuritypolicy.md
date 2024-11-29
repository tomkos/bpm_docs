# Changing the security policy

## About this task

| Setting               | Default Value   | Description                                                                                                   |
|-----------------------|-----------------|---------------------------------------------------------------------------------------------------------------|
| adhoc-reroute-enabled | true            | Controls the ability to move or route tokens between activities. This runtime property is enabled by default. |

```
<server merge="mergeChildren"> 
  <portal merge="mergeChildren"> 
    <adhoc-reroute-enabled merge=”replace”>true</adhoc-reroute-enabled>	 
  </portal>
</server>
```

For
information about the 100Custom.xml file's location, and how to create, modify,
and deploy it, see The 100Custom.xml file and configuration.

## Related tasks

- Generating an instance migration policy file to manage orphaned tokens