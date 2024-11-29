# Rule steps do not run if processing timeout value is too low

## Symptoms

In Case Client,
you view the details of the task that contains the rule step and see
that the task failed with the error Work Performer Exception:null.
In addition, the following error message is written to the pesvr\_system.log file
during rule execution:

CMExecute[1].int2vm13cmtosuser.FNTARGETDS\_1
.ICM\_RuleOperations.P8Admin [ LOAN1\_PoorCreditRating: 93A2C03B20B4314BA02B16087B5BFC3C:Workflow:
executeRule] FAILED.; Exception: java.lang.InterruptedException  		
at
java.lang.Object.wait(Native Method)  		
at java.lang.Object.wait(Object.java:485)
 		
at ilog.rules.res.xu.ruleset.internal.IlrRulesetProvider.getRuleset(IlrRulesetProvider.java:213)
 		
at ilog.rules.res.xu.spi.IlrManagedXUConnection.createEngineManager(IlrManagedXUConnection.java:1443)
 		
at ilog.rules.res.xu.spi.IlrManagedXUConnection.getEngineManager(IlrManagedXUConnection.java:1319)
 		
at ilog.rules.res.xu.spi.IlrManagedXUConnection.getXURulesetArchiveInformation(IlrManagedXUConnection.java:1260)
 		
at ilog.rules.res.xu.cci.IlrXUConnection.getXURulesetArchiveInformation(IlrXUConnection.java:466)
 		
at ilog.rules.res.xu.cci.IlrXUInteraction.getRulesetInformation(IlrXUInteraction.java:561)
 		
at ilog.rules.res.xu.cci.IlrXUInteraction.dispatchExecution(IlrXUInteraction.java:129)
 		
at ilog.rules.res.xu.cci.IlrXUInteraction.execute(IlrXUInteraction.java:253)

## Causes

## Resolving the problem

To set the
processing timeout value for the rules component queue:

1. In Process Configuration Console, select the appropriate connection
point.
2. Click Component Queues > ICM\_RuleOperations.
3. In the Component Properties window, click
the Adapter tab and modify the value of the Processing
Timeout (ms) field.