# Exception messages in Decision service testing 
(deprecated)

- When a rule component is running, exception messages include the
Decision service name and step name.
- Exceptions in a rule condition cannot be traced to a specific
rule.
- Exceptions in a rule action can be traced to a specific rule.
- The rule name includes a number part that corresponds to the order
of the rules in the BAL rules component, such as 1, 2, 3, or 4. If
there are numerous rules in a BAL rules component, this number helps
you track down the location of the error.

## Example of a null exception

```
ilog.rules.res.session.IlrRuleServiceException: ilog.rules.res.session.IlrSessionException: An error occurred while the rule session was invoked.:
ilog.rules.res.session.IlrSessionException: An error occurred while the rule session was invoked.
ilog.rules.res.util.IlrRemoteException: Ruleset execution error
ilog.rules.res.util.IlrRemoteException: null
    at call to 'mainRuleflow flow task body'
    at call to 'execute'
ilog.rules.res.util.IlrRemoteException

    at ilog.rules.res.session.IlrRuleService.executeRuleset(IlrRuleService.java:124)
    at com.ibm.rules.sdk.samples.documentrules.ResultsTab$4.widgetSelected(ResultsTab.java:206)
    at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:234)
    at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
    at org.eclipse.swt.widgets.Display.sendEvent(Display.java:3776)
    at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1367)
    at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1390)
    at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1375)
    at org.eclipse.swt.widgets.Widget.notifyListeners(Widget.java:1187)
    at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3622)
    at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3277)
    at org.eclipse.ui.internal.Workbench.runEventLoop(Workbench.java:2629)
    at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2593)
    at org.eclipse.ui.internal.Workbench.access$4(Workbench.java:2427)
    at org.eclipse.ui.internal.Workbench$7.run(Workbench.java:670)
    at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
    at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:663)
    at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
    at com.ibm.rules.sdk.samples.documentrules.Application.start(Application.java:38)
    at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
    at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
    at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
    at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:369)
    at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
    at java.lang.reflect.Method.invoke(Method.java:597)
    at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:619)
    at org.eclipse.equinox.launcher.Main.basicRun(Main.java:574)
    at org.eclipse.equinox.launcher.Main.run(Main.java:1407)
    at org.eclipse.equinox.launcher.Main.main(Main.java:1383)
Caused by: ilog.rules.res.session.IlrSessionException: An error occurred while the rule session was invoked.:
ilog.rules.res.session.IlrSessionException: An error occurred while the rule session was invoked.
ilog.rules.res.util.IlrRemoteException: Ruleset execution error
ilog.rules.res.util.IlrRemoteException: null
    at call to 'mainRuleflow flow task body'
    at call to 'execute'
ilog.rules.res.util.IlrRemoteException
```

## Unsupported variable type

```
An error occurred in simpleTypeTestService service, at rule 1 in step SimpleTypeRuleStep. 
Detail message: Ruleset /b\_c54531e1028c40a185bf1115183a3420/1.0/\_bd1ea7af45d14fa9afcea38113db2c35\_8cf262cc674e4561bce84c00820bc88e/1.0 parsing failed 'IRL/rule\_1.irl', line 8: 
  error: incompatible values involved in assignments
com.lombardisoftware.core.TeamWorksException: 
  An error occurred in simpleTypeTestService service, at rule 1 in step SimpleTypeRuleStep. 
  Detail message: Ruleset /b\_c54531e1028c40a185bf1115183a3420/1.0/\_bd1ea7af45d14fa9afcea38113db2c35\_8cf262cc674e4561bce84c00820bc88e/1.0 parsing failed 'IRL/rule\_1.irl', line 8: 
   error: incompatible values involved in assignments
     at com.lombardisoftware.core.TeamWorksException.asTeamWorksException(TeamWorksException.java:129)
     at com.lombardisoftware.core.RegexExceptionRewriter.rewrite(RegexExceptionRewriter.java:76)
     at com.lombardisoftware.core.ExceptionHandler.returnProcessedException(ExceptionHandler.java:310)
```

## Uninitialized variable produces a NullPointerException

```
An error occurred in NotificationRules service, at rule 1 in step AlertRuleStep. 
Detail message: Object CustomerName not found at run time during execution. Make sure the object has been initialized.
	at com.lombardisoftware.core.TeamWorksException.asTeamWorksException(TeamWorksException.java:129)
	at com.lombardisoftware.core.RegexExceptionRewriter.rewrite(RegexExceptionRewriter.java:76)
	at com.lombardisoftware.core.ExceptionHandler.returnProcessedException(ExceptionHandler.java:310)
	at com.lombardisoftware.servlet.ControllerServlet.doError(ControllerServlet.java:152)
	at com.lombardisoftware.servlet.ControllerServlet.doCommon(ControllerServlet.java:417)
	at com.lombardisoftware.servlet.ControllerServlet.doPost(ControllerServlet.java:134)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:738)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:831)
```