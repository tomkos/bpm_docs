# Troubleshooting IBM Business Automation
Workflow on containers

For information about retrieving the log files of the installed operator, see Troubleshooting.

For usage tips and information about existing solutions for issues that you might encounter with
production deployment, see Troubleshooting Business Automation Workflow or Workstream
Services.

- Elasticsearch or OpenSearch fails to start

When it is configured to use GP2 block storage, the Elasticsearch pod might fail to start if it cannot obtain node locks. You might see the following error:
- The ums-teams-deployment pods do not start

The pods do not start and the status of the ums pods stays in 0/1 state.
- Changing deployment hostname suffix after installation

If you change the value of the shared\_configuration.sc\_deployment\_hostname\_suffix parameter in the CR and apply the CR after installation, you might find that the old value is still used. Instead of using the new fully qualified domain name to access workflow, it redirects to the previous name and fails.