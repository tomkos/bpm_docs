# Case management overview

For example, if you want to design a solution for resolving credit
card disputes, IBM Business Automation
Workflow provides
tools to quickly design and create a solution that case workers can
then use to process cases in that solution.

- An active-content infrastructure that manages the persisted case
object model and enables content-based events for case activities.
For example, the addition of a document or a field change triggers
a case activity.
- Enterprise content management integration that includes complete
document lifecycle capabilities including versioning, security, and
records management.
- True content management functionality that enables you to store
document metadata that you can later modify and search on.
- A process map that manages the logic for the execution of an activity.
- An out of the box user interface that is built in a flexible and
easily customizable widgets-based environment that you can also extend
to create a role-based client experience that provides case workers
with the information they need to work on cases.
- Template-based solutions that you can easily modify and reuse.
- Rich analytics provided by Case Analyzer offer several ways to track
and measure performance that is associated with cases and workloads so that you can optimize your
cases.

- Case management solution concepts

Solutions consist of case types, activities, steps, and other components. A solution is an application that case workers use to process cases.
- Scenario: Financial services credit card dispute resolution

IBM Business Automation Workflow can provide card-issuing banks with a case management solution for credit card dispute resolution. IBM Business Automation Workflow provides a comprehensive view of the case for the case workers, improves case worker efficiency, and reduces the chance for errors as the case is being processed.
- Scenario: Automobile insurance claims

IBM Business Automation Workflow provides a sample solution for creating and managing automobile insurance claims. With the case management system, you can associate the data about the claim and the submitter with the supporting documentation as it is submitted. The business analyst can quickly process any required changes to the automobile claim solution. By configuring a solution in IBM Business Automation Workflow, you can ensure that claims are processed completely and accurately.
- Case Builder

The Case Builder is a web-based tool for business analysts to design and develop a solution and the artifacts that make up cases in that solution. Optionally, business analysts can use a wizard in Case Builder to guide them through creating a solution, or they can create the solution components manually and in any order. After the solution is initially defined, multiple business analysts can collaborate and contribute to the solution creation and refinement. For example, while one business analyst designs case types, case properties, and activities with corresponding workflows for case workers to process, another can define business rules for automated decision making.
- Case Client

The Case Client is a web-based application for case workers to complete their work for each case. Before the Case Client is deployed into production so that case workers can access it, business analysts can modify the application to customize it.
- Case configuration tool

The IBM Business Automation Workflow case configuration tool is used to configure Case Builder, Case Client, and integration points with other optional components. Based on the values that you specify, the configuration tool configures the environment and deploys the applications.
- Case administration client

The IBM Business Automation Workflow case administration client is a web-based application that is used to administer your case management system. Administrators can access wizards to work with solutions, manage project areas, configure security and auditing, and migrate case management components from one environment to another.
- Development and production environments

The case management environment consists of a development environment for creating and initially testing solutions, a test environment for fully testing the solutions, and a production environment where users work on active and archived cases. All of the environments include FileNet® P8 object stores and databases for storing solution data. In addition, environments include a file system at the IBM Case Manager tier for storing pages, views, and resources, and a file system at the FileNet P8 tier for storing rulesets, if applicable.
- Case health analysis

IBM Business Automation Workflow monitors case health by analyzing the due dates for quick tasks, deadlines for work items, duration of case stages and overdue userTasks from BPM processes. IBM Business Automation Workflow then displays health indicators so that a case worker can quickly see whether a case is in good health. If the case is not in good health, the case worker can view details as to why.