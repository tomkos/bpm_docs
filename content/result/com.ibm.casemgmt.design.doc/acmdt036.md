# Configuring auditing

## About this task

Choose properties to audit that are meaningful to your business and solution. For example, a
financial organization might want to audit properties such as LoanAmount, ApprovalStatus, and
Priority. A case analyst might be interested in the number of occurrences of a particular case type,
or the length of time that caseworker require to complete a particular task.

You can specify properties to audit by using the audit configuration wizard in the Case administration client. Select document
properties and properties of each case type for the solution that you want to audit. If tasks are
defined for the case type, you can select the task and then select the task properties that you want
to audit. To view custom properties in the extended history, you must select those properties for
auditing. In addition, some system properties are automatically selected for auditing.

Audit configuration settings are stored in an audit manifest file. Use the export and import
audit configuration wizards to move an audit manifest from one environment to another. For example,
you can create and check your audit configuration in a test environment before you import the audit
configuration into production.

After you specify properties to audit and apply the audit configuration to a solution, you can
use Case Analyzer to generate
chart-based reports that are based on statistical information that is gathered from the system. You
are some additional configuration steps to be followed before using Case Analyzer and other case analytics tools.
For more information see, Integrating IBM case analytics tools.

To track the extended history of cases by using the timeline visualizer widget,
you must define a case history store. You can store extended case history data in the database
instance that is used for the target object store. Alternatively, you can store extended history
data in a separate database instance. For example, you might want to use a separate, remote database
server if the I/O throughput is problematic. For more information, see Preparing a database for the case history store.

## Procedure

To configure auditing:

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM® Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. In the navigation tree on the left side, select a design object store and click
Solutions.
3. On the Solutions page on the right side, select the solution that contains
the properties you want to audit.
4. Click Actions > Manage > Audit
Configuration and complete the wizard steps.
You can create an audit configuration, or edit an existing audit configuration. You can save
your changes but for change to get reflected in the audit configuration, you need to apply
it.Note: While using Case event emitter, if you want to restrict some of the case or task properties
from processing, you need to select the “Disable BAI” checkbox for the respective
properties.
5 If you plan to use the timeline visualizer widget, you must prepare a databaseto record extended case history data. Then, configure and enable the case history store. Attention: If the Content Platform Engine server that serves as thebackend to the IBM Business AutomationWorkflow system is configured as a cluster, configure and enable the case history store when only a singleContent Platform Engine server isavailable. This is typically during a maintenance window when all but one of the application serverinstances hosting the Content Platform Engine server can be stopped. To create the case history store: To enable an existing case history store: Note: In addition to creating and enabling a case history store, you need to ensure that the casehistory services are enabled in Content Platform Engine . This facilitates theavailability of case history data. For more information, see Enabling and disabling case history .

To create the case history store:

    1. In the Case administration client, in
the navigation tree on the left side, select a target object store and click New Case
History Store.
    2. Complete the wizard steps.

To enable an existing case history store:

    1. In the Case administration client, select a target object
store in the navigation tree on the left side and then select Case History
Store.
    2. Select the check box to enable the case history store and then save your changes and
close.