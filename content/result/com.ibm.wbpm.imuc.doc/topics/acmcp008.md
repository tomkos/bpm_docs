# Integrating IBM case
analytics tools

## About this task

- Case Analyzer Excel Reports
- IBM®
Cognos® Analytics

With the data extracted by Case Analyzer services, you can generate
real-time reports and historical data analysis by analyzing case,
task, and workflow events. The Case Analyzer component
integrates with IBM
Cognos Analytics to
provide web-based analytic and reporting capabilities. It also supports
using Microsoft Excel as a thick client-based analytic and reporting
solution.

The Case Analyzer service, which is a background task
in the Content Platform Engine, collects data from the workflow
system event logs and the object store audit log. The service stores the information in a database
that is used by IBM
Cognos Analytics reports.

- Integrating with Case Analyzer

Case Analyzer reads data from both workflow and Content Platform Engine event logs. Analytical data from both sources is published to a common Case Analyzer database. To support case management systems, new metrics that are related to cases and tasks were added to Case Analyzer, formerly known as  FileNet®  Process Analyzer.