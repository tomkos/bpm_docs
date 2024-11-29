# Naming conventions

Acronyms can contain these characters: capital letters (A-Z), numbers (0-9), and underscore (\_).
Snapshot acronyms can also contain a period (.).

The project acronym is created when the project is created. You must specify an acronym that is
unique across your environments.

The branch acronym is automatically generated using the same guidelines as the snapshot acronym
although it doesn't include periods. For example, a new branch created with the name My New
Branch would result in an acronym value of MNB. The default branch name
and acronym are Main. The name and acronym must be unique within the project.

- capital letters (A-Z), numbers (0-9), a period (.)
- lowercase characters that follow whitespace or an underscore (\_), converted to uppercase

- Enforce a consistent format across your organization that guarantees seven or fewer characters
are used for each snapshot acronym.
- Use a date-based snapshot-naming convention like MMDDYY, MM-DD-YY, OR YY-MM-DD. Avoid any
convention that uses periods and eight digits like MMDDYYYY.
- Use a version format to prefix the application, which takes care not to exceed seven total
characters and can include periods, numbers, and uppercase letters.
- Have a description or application acronym appended as a suffix so it doesn't impact the acronym,for example
    - 072920A\_MyApp
    - 07-29-20B\_GA
    - 07\_29\_20C\_HSS

- 03-26-15A\_MyApp
- 03-26-15B\_MyApp
- 23.154\_MyApp

- 10.13.15\_My App and 10.13.19\_MyApp
- MYAPPNAMEv3.4.16 and MYAPPNAMEv3.4.17

For example, a snapshot name
11.22.33 results in a 11.22.3 snapshot
acronym.

- Naming conventions for Workflow Center server deployments

On the IBM Workflow Center server, you can deploy a snapshot of a process application as well as a snapshot of a toolkit. In addition, you can deploy the tip of a process application or the tip of a toolkit. (A tip is the current working version of your process application or toolkit.) The version context varies, depending on the type of deployment.
- Naming conventions for Workflow Server deployments

On Workflow Server, you can deploy the snapshot of a process application. The process application snapshot acronym is used to uniquely identify the version.