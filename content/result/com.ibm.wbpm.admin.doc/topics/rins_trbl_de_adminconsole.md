# Deployment environment is missing in the WebSphere administrative
console on Linux

```
ServletWrappe E com.ibm.ws.webcontainer.servlet.ServletWrapper service SRVE0014E:
Uncaught service() exception root cause /com.ibm.ws.console.servermanagement/addPropLayout.jsp:
com.ibm.websphere.servlet.error.ServletErrorReport: javax.servlet.jsp.JspException:
Missing message for key "addprops.category.label.businessintegration"
```

If the error is logged, complete the following steps
to resolve the problem:

1. Ensure that the value specified for the ulimit -n command
is high enough for the version of WebSphere Application Server used
in IBM BPM. For more information, see the topic Preparing Linux systems
for installation.
2. Stop all servers.
3. Run the following command to restore the application for the WebSphere
administrative console application (where dmgr\_profile\_root is
the root directory of the deployment manager profile): dmgr\_profile\_root/bin/iscdeploy.sh -restore