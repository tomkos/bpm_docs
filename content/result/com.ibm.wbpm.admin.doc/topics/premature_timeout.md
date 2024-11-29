# Logging into web Process Designer using a system ID may result in premature session
timeout

When you log into web Process Designer using a system ID, there may be other system processes
that are already running under the ID. This can affect the system determination about when the ID is
first used for a login operation and possibly result in the premature expiration of the browser
session.

It is recommended that you use a non-system ID to log into web Process Designer.