# Generic consideration

- Use the virtual hostname to define Content Platform Engine hosts, it can be defined in
/etc/hosts on related machine, for example, see the following table: 
Table 1. 

Virtual hostname
Mapped to machines

CPEIHS.cn.ibm.com
Map to hostname for load balancer for Content Platform Engine Cluster1

CPEServer1.cn.ibm.com
Map to hostname for Content Platform Engine Cluster1 Node1

CPEServer2.cn.ibm.com
Map to hostname for Content Platform Engine Cluster1 Node2

CPEIHS.cn.ibm.com
Map to hostname for load balancer for Content Platform Engine Cluster2

CPEServer1.cn.ibm.com
Map to hostname for Content Platform Engine Cluster2 Node1

CPEServer2.cn.ibm.com
Map to hostname for Content Platform Engine Cluster2 Node2
- Use Same Network folder between Business Automation Workflow and Content Platform Enginecluster1 and Business Automation Workflow and Content Platform Engine cluster2, for example:
    - Share folder between Business Automation Workflow and Content Platform Engine cluster1 is:
/home/IBM/Share
    - Share folder between Business Automation Workflow and Content Platform Engine cluster2 is:
/home/IBM/Share