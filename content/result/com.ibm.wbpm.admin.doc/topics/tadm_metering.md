# Monitoring concurrent users and activities

## Before you begin

## Procedure

1. While the metering agent is running, you must schedule the
IlmtCollector script to run (for example, once a day) to save the data for the
concurrent user and activity metrics. For instructions,
see Collecting license compliance records in the FileNet® P8
Platform documentation.
2. Run the IlmtReporter script to generate both CSV format files (for
viewing in a spreadsheet program) and slmtag files that can be read by the
IBM License Metric
Tool agent. For instructions,
see Generating license compliance reports in the FileNet P8
Platform documentation.