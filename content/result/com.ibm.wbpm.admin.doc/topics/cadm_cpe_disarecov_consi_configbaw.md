# Configure with IBM Business Automation Workflow Case configuration tool

While using IBM Business Automation Workflow Case configuration tool (configmgr) to do the
configuration,

- Use the virtual hostname while run configmgr, for example:
    - Content Platform Engine server connection: CPEIHS.cn.ibm.com
    - Content Platform Engine server WSI URL:
https://CPEIHS.cn.ibm.com:443/wsi/FNCEWS40MTOM/
    - Content Platform Engine server EJB URL:
corbaloc::CPEServer1:9810,:CPEServer2:9811/cell/clusters/CPEcluster/FileNet/Engine
    - Network shared directory: /home/IBM/Share

- First, Start Business Automation Workflow Node1, Node2. Stop Business Automation Workflow Node3,
Node4, configure Business Automation Workflow and Content Platform Engine Cluster1.
- Second, Stop Business Automation Workflow Node1, Node2, Start Business Automation Workflow
Node3, Node4, configure Business Automation Workflow and Content Platform Engine Cluster2.
- Then, restart Business Automation Workflow environment and Content Platform Engine clusters,
keep Business Automation Workflow servers Node1, Node2 running.