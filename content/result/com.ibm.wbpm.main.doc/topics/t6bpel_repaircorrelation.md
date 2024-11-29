<!-- image -->

# Updating correlation sets associated with stopped activities

## About this task

- An exception occurred when the correlation set was evaluated.
The correlation set is to be initialized but it is already initialized.
- An exception occurred when the correlation set was evaluated.
The correlation set is to not be initialized but its values are not
set. This can occur, for example, because an initializing activity
was skipped.
- The activity needs to be retried. If the correlation set is initialized
by the activity, then it can be unitialized or changed before the forceRetry method
is called.
- The activity needs to be completed. If the correlation set is
initialized by the activity, then it can be unitialized or changed
before the forceComplete method is called.

You can retrieve the correlation set instances of a process
or activity instance. The following example shows how to initialize
or unitialize correlation set instances.

## Procedure

1. List the stopped activities in the stopped state. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_STOPPED");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);
This action returns the stopped
activities for the CustomerOrder process instance.
2. Retrieve the correlation set instances that are defined
for the activity. AIID aiid = null;

List correlationSet = null;

if (result.getEntities().size() > 0)
{
   Entity activityEntity = (Entity) result.getEntities().get(0);
   AIID aiid = (AIID) activityEntity.getAttributeValue("AIID");
	  ActivityInstanceData activity = process.getActivityInstance(aiid);
   correlationSet = process.getCorrelationSetInstances
                    (aiid, activity.getInputMessageTypeName());  
}
3. Unitialize the correlation set, for example, MyCorrelationSet.
for ( int i=0; i<correlationSet.size(); i++ )
{
  CorrelationSetInstanceData correlationSetInstance = 
            (CorrelationSetInstanceData)correlationSet.get(i);
  
  if ( correlationSetInstance.isInitialized() && 
       correlationSetInstance.getCorrelationSetName().equals("MyCorrelationSet") )
  {
    process.uninitializeCorrelationSet
       ( activity.getProcessInstanceID(), correlSetInstance.getCorrelationSetName() );
  }
}This action uninitializes the correlation
set MyCorrelationSet.
4. Initialize the correlation set, for example, MyCorrelationSet.
In this example, a string-valued property of the correlation
set is set.for ( int i=0; i<correlationSet.size(); i++ )
{
  CorrelationSetInstanceData correlationSetInstance = 
            (CorrelationSetInstanceData)correlationSet.get(i);
  
  if ( correlationSetInstance.getCorrelationSetName().equals("MyCorrelationSet") )
  {
    List correlationSetProperties = 
                    correlationSetInstance.getCorrelationSetProperties();
    for ( int j=0; j<correlationSetProperties.size(); j++ )
    {
      CorrelationPropertyInstanceData property = 
                (CorrelationPropertyInstanceData)correlationSetProperties.get(j);
  
      if ( property.getPropertyName().equals("MyProperty") )
      {
        property.setValue("NewValue");

        process.initializeCorrelationSet
           ( activity.getProcessInstanceID(), correlationSetInstance );
      }
    }
  }
}This action initializes the string-valued
property MyProperty in the correlation set MyCorrelationSet.