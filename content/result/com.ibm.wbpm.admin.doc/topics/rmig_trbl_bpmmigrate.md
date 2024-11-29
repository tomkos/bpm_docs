# BPMMigrate troubleshooting

- Edit install\_root/bin/wsadmin.sh.
Find PERF\_JVM\_OPTIONS and increase the value of -Xmx256m to
-Xmx512m.
- Edit install\_root\bin\wsadmin.bat.
Find PERFJAVAOPTION and increase the value of -Xmx256m to
-Xmx512m.

To diagnose other problems, change the log level to FINEST as described in "Troubleshooting
migration." After you run the command again, check the log file named
BPMMigrate\_timestamp.log. The file is found in
snapshot\_folder/logs/. If you cannot find the cause of the
problem, you can provide the log to IBM support.

For the scheduler migration, the BPMMigrate command runs the
AdminTask that is registered during server startup and uses the scheduler service
to re-create each scheduler task. The trace for the AdminTask is saved in
snapshot\_folder/logs/. The log for the scheduler migration
is saved on one of the active nodes, in
install\_root\_24.0.0.0/profiles/custom\_profile/logs. Collect both the
trace file and the log file for analysis if an exception occurs.

Make sure that the messaging engine is started before you run BPMMigrate.
Otherwise, the command fails when it tries to migrate the service integration bus messages.