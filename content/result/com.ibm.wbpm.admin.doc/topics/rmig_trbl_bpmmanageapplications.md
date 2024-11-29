# BPMManageApplications troubleshooting

- If you use the remote migration utility to run the command in
the source environment, the log file is in remote\_migration\_utility/logs/migration.
- Otherwise, the log file is in install\_root/logs/migration in
the target environment.

- To see the status of your WebSphere® Application
Server applications,
open the administrative console and go to Applications > Application types > WebSphere enterprise
applications.
- To see the status of the schedulers, go to the server log for
the application cluster. You can find the log under the profile path
of any custom node, in node\_profile/logs/app\_cluster\_member/SystemOut.log.
Check for a message in the log similar to the following message:[6/27/13 12:13:03:311 CST] 0000008b SchedulerDaem I   SCHD0038I: The Scheduler Daemon for instance BPEScheduler has started.This
message provides the status for the scheduler daemon for the instance
named BPEScheduler. If you do not see such a message,
the scheduler is not started.