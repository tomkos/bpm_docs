# Track license usage for IBM Integration
Designer

Integration Designer is licensed per authorized user. The
Microsoft Windows User ID can be tied to the authorized user and is recorded on the machine where
Integration Designer runs.

When Integration Designer is
running, usage files (.slmtag files) are created
in the <workspaceroot>/.metadata folder. The
IBM BigFix client collects the usage files from the machine where Integration Designer is running
and sends them to the License Metric Tool for analysis.

For more information about the License Metric Tool and how you can use it to track your license
usage, see the IBM License Metric Tool documentation.