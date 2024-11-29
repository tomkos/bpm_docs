# Installing the Case Analyzer reporting tools

You can use Case Analyzer reporting tools to work with reporting components like Case Analyzer
SSAS OLAP  service and sample reports for Cognos and
Excel of a Case Analyzer store. The default
installation of these tools supports Microsoft SQL Server version up to 2016. If
you are using the latest versions of Microsoft SQL server, you can manually copy
the required contents from MSSQL\_2017\_2019\_2022 folder into the installation
folder or run upgrade\_reporting\_tools.bat batch script to copy these files
automatically according to the steps described in the readme.txt.

1. Extract the contents of ibm-java-jre-8xxxx-win-xxxx.zip to a temporary
folder.
2. Delete the content of the Java directory <Case Analyzer Reporting Tools
location>\Case Analyzer components\SSAS OLAP connector\java.
3. Copy the contents of the extracted folder from the temporary location to <Case
Analyzer Reporting Tools location>\Case Analyzer components\SSAS OLAP
connector\java.

Alternatively, to update the Java version to IBM® Business Automation
Workflow Java automatically, run
upgrade\_reporting\_tools.bat batch script.

## About this task

## Procedure

To install the Case Analyzer reporting
tools:

1. Extract the CaseAnalyzerReportingTools.zip in your <BAW
Installation Folder>CaseManagement > analytics  folder.
2. Extract the folder and give appropriate permissions to all the files along with the
executable ones.
3. Follow the readme.txt file provided in the
zip/folder to continue.