# How do you enable monitoring?

For Application Response Measurement (ARM) statistics,
use the administrative console Request Metrics section to specify
and the statistics you want to monitor.

IBM® Business Automation Workflow supports
two types of Common Base Event enablement for problem determination
and business process monitoring:

The primary purpose of the Dynamic
enablement is for creating correlated service component events that
are published to logs, which allow you to perform problem determination
on services. Service component events can be large, depending on how
much data is being requested, and can tax database resources if you
choose to send events to the CEI server. Consequently, you should
publish dynamically monitored events to the CEI server only if you
need to read the business data of the events, or if you otherwise
need to keep a database record of the events. If, however, you are
monitoring a particular session, then you need to use the CEI server
database to access the service component events related to that session.