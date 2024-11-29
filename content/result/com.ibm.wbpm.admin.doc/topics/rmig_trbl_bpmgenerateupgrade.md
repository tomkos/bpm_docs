# BPMGenerateUpgradeSchemaScripts troubleshooting

Change the log level to FINEST as described in "Troubleshooting migration." After you run the
command again, check the log file named
BPMGenerateUpgradeSchemaScripts\_timestamp.log. The file is
found in install\_root/logs/migration. If you cannot find the
cause of the problem, you can provide the log to IBM support.

The command reads database information from the properties file specified by the
target.config.property.file property in the
target\_migration.properties file. If the generated SQL scripts are not what you
expect, check the value of that property or the specified file to make sure that the settings are
correct.