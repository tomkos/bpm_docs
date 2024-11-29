# Sample configuration properties files for the BPMConfig command

## Sample properties files

The sample configuration
properties files are provided in the install\_root/BPM/samples/config folder
(where install\_root is the installation location
of IBM® Business Automation Workflow).

- de\_type is one of Standard, Advanced,
AdvancedOnly
- environment\_type is PS (Process Server - for Workflow Server) or PC (Process Center
- for Workflow Center) (omitted where
de\_type=AdvancedOnly)
- topology is one of SingleCluster, ThreeClusters
- database\_type is one of DB2, DB2zOS, SQLServer,
Oracle
- WinAuth is only appended for environments using SQL Server with Windows
authentication

In
the install\_root/BPM/samples/config/performancetuning folder,
there are two sample properties files for performance tuning. The
files have the following names:

- Advanced-PC-ThreeClusters-DB2.properties
- Advanced-PS-ThreeClusters-DB2.properties

- Advanced-PS-ThreeClusters-DB2-MultiDB-De1.properties
- Advanced-PS-ThreeClusters-DB2-MultiDB-De2.properties
- Advanced-PS-ThreeClusters-DB2-MultiDB-MultiBus.properties