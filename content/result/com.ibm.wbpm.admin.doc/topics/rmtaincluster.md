# Administering cluster members with an external Content Platform Engine

When cluster members are added or removed on either the Business Automation Workflow environment or the connected Content Platform Engine environment, the list of servers that are
involved in the server-to-server communication changes. Use the
updateBPMExternalECM administrative task to update this list.

- IBM Business Automation Workflow : If you add or remove anBusiness Automation Workflow cluster member with a connectedexternal Content Platform Engine system, use theupdateBPMExternalECM administrative task. This administrative task determines thelist of Business Automation Workflow servers that Content Platform Engine can communicate with. See updateBPMExternalECM command .
    - If you did not specify the -backlinkURL parameter when you initially ran
the setBPMExternalECM administrative task (which is recommended), you do not need
to specify it with the updateBPMExternalECM administrative task. The list of
available Business Automation Workflow cluster member servers is
maintained automatically.
    - If you specified a list of cluster member servers by using the
-backlinkURL parameter when you initially ran the
setBPMExternalECM administrative task, specify this same parameter with the
updateBPMExternalECM administrative task. You are responsible for updating the
list of available IBM BPM cluster member servers. Note: Once you use the
-backlinkURL parameter in an updateBPMExternalECM
administrative task, it must be specified in all subsequent updateBPMExternalECM
administrative tasks.
- Content Platform Engine: If you add or remove a cluster
member in the Content Platform Engine environment that is
connected to an Business Automation Workflow environment, use the
updateBPMExternalECM administrative command to update the list of servers. This
administrative task determines the list of Content Platform Engine servers that  Business Automation Workflow can communicate with. When you run the
updateBPMExternalECM administrative task, use the -ceURL
parameter to provide to Business Automation Workflow the list of
updated Content Platform Engine servers.