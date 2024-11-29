# NPE exceptions when loading IBM Content Navigator client jars

```
[6/11/22 3:49:44:900 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in 
[https://bawshare1.fyre.ibm.com:9443/ICMClient/bpm-icn-plugin.jar]
java.lang.NullPointerException
	at com.ibm.ecm.util.PluginUtil.getPluginFile(PluginUtil.java:168)
	at com.ibm.ecm.util.PluginUtil.getPluginsMap(PluginUtil.java:109)
	at com.ibm.ecm.util.PluginUtil.getPluginsMap(PluginUtil.java:69)
	at com.ibm.ecm.util.PluginUtil.dropPlugins(PluginUtil.java:1700)
	at com.ibm.ecm.jaxrs.ApplicationEventHandler.lambda$applicationStopped$1(ApplicationEventHandler.java:102)
	at com.ibm.ecm.jaxrs.ApplicationEventHandler$$Lambda$250/0x0000000000000000.run(Unknown Source)
	at com.ibm.ecm.jaxrs.ApplicationEventHandler.tryRunning(ApplicationEventHandler.java:111)
	at com.ibm.ecm.jaxrs.ApplicationEventHandler.applicationStopped(ApplicationEventHandler.java:102)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:90)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55)
	at java.lang.reflect.Method.invoke(Method.java:508)
	at com.ibm.ecm.event.EventManager$HandlerMethod.invokeNow(EventManager.java:355)
	at com.ibm.ecm.event.EventManager$HandlerMethod.lambda$invoke$10(EventManager.java:345)
	at com.ibm.ecm.event.EventManager$HandlerMethod$$Lambda$156/0x0000000000000000.run(Unknown Source)
	at com.ibm.ecm.util.ContextualExecutorService$RunWrapper.run(ContextualExecutorService.java:76)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:522)
	at java.util.concurrent.FutureTask.run(FutureTask.java:277)
	at com.ibm.ecm.util.ContextualExecutorService$RunWrapper.run(ContextualExecutorService.java:76)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1160)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
	at java.lang.Thread.run(Thread.java:825)
```

```
Line 9833: [6/11/22 3:49:44:900 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in [https://bawshare1.fyre.ibm.com:9443/ICMClient/bpm-icn-plugin.jar]
Line 9884: [6/11/22 3:49:44:900 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in [https://bawshare1.fyre.ibm.com:9443/ICMClient/ICMAPIPlugin.jar]
Line 9935: [6/11/22 3:49:44:900 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in [https://bawshare1.fyre.ibm.com:9443/ICMClient/ICMClient.jar]
Line 9986: [6/11/22 3:49:44:916 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in [https://bawshare1.fyre.ibm.com:9443/ICMClient/ICMAdminClientPlugin.jar]
Line 10037: [6/11/22 3:49:44:916 PDT] 000001a6 SystemOut     O CIWEB Error: com.ibm.ecm.util.PluginUtil.getPluginsMap() Exception loading plug-in [https://bawshare1.fyre.ibm.com:9443/ICMClient/ICMMonitor.jar]
```