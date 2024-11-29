# Disabling communication with IBM Business Automation
Insights

Disable communication to IBM® Business Automation
Insights to restore your
IBM Business Automation
Workflow
environment.

## Procedure

1. Find the defconfig.xml file. The
defconfig.xml file holds the DEF configuration and must be present in the
Business Automation Workflow Deployment
Manager profile at this
location:<BAW\_Install\_Root>/profiles/DmgrProfile/config/cells/<CellName>.
2. Change the name of defconfig.xml to disable the emissions of events
altogether. No more events are emitted to the queue.
3. Do a full resynchronization in WebSphere Application Server including the dmgr and node
levels. Then restart Business Automation Workflow. Verify that
the defconfig.xml file does not exist anywhere on the system. If
defconfig.xml still exists, repeat the resynchronization and
restart.