# IBM Business Automation Workflow log
files

## Installation and configuration logs

Various
log files are created during the installation and uninstallation of IBM Business Automation Workflow and
during profile creation, augmentation, and deletion. Examine these
logs when problems occur during the product installation and configuration
process.

## Runtime logs

By default, log, error, and
trace information for all processes and applications on a process
server is written to the SystemOut.log, SystemErr.log,
and trace.log files, which are stored in the install\_root/profiles/profile\_name/logs/server\_name directory.
These files are standard log files provided by WebSphere Application
Server and capture information based on how logging and tracing are
configured for the server.

Typically, the SystemOut.log file
is used to monitor the health of the running server and for problem
determination; entries include information to help you identify the
specific component associated with the message. The SystemErr.log file
contains exception stack trace information that is useful when performing
problem analysis. When tracing is enabled, the trace.log file
contains trace messages that can be used for problem determination.

- TW BPD Engine: Errors generated as a result of process instance
execution on the current server
- TW Console: Actions that occurred in the Process Admin console
- TW Error: Java exceptions
- TW EventManager: Historical information about Event Manager processing
- TW Exp/Imp:Process export and import transactions in Process Designer
- TW Limit: Process server limit overruns
- TW JavaScript: Logging associated with JavaScript log functions
like log.info() or log.debug()
- WS Inbound: Calls to published web services
- WS Outbound: Data about web services consumed by processes
- WS UCA Execution: Errors generated by Undercover Agent (UCA) execution

- WebSphere Application Server warnings in the Workflow Center log file

In IBM Business Process Manager Advanced, if the Process Designer web editor is open for a long period of time, you might notice unexpected messages in the SystemOut.log file for the Workflow Center. For example, you might see 0000035e, SRVE8092W, 000001b0, or SECJ0371W messages.