<!-- image -->

# Example: Using the queryAll method

```
queryAll( "DISTINCT ACTIVITY.AIID", 
       "PROCESS\_TEMPLATE.NAME = 'sampleProcess'",  
       (String)null, (String)null, (Integer)null, (TimeZone)null )
```

```
SELECT DISTINCT ACTIVITY.AIID
   FROM   ACTIVITY AI, PROCESS\_TEMPLATE PT
   WHERE  AI.PTID = PT.PTID
   AND    PT.NAME = 'sampleProcess'
```