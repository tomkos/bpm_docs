# Configure with setBPMExternalECM

When you run the setBPMExternalECM admin command to configure IBM Business Automation Workflow to
use an external Content Platform Engine, for parameter ceURL, use the virtual
hostname and include all hostnames in a Content Platform Engine cluster. For example,

corbaloc::CPEServer1:9810,:CPEServer2:9811/cell/clusters/CPEcluster/FileNet/Engine

The BOOTSTRAP\_ADDRESS port between two Content Platform Engine clusters must be same.