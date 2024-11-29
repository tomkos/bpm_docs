# Reinstallation cannot create new profile when using the Typical
installation and configuration option

If databases were created for the test environment, the
databases must be dropped before you can create a new profile.

- For the qbpmaps profile, the default databases are QBPMDB, QPDWDB,
and QCMNDB
- For the qesb profile, the default databases are ECMNDB and QECMNDB
(one or both)
- For the qmwas profile, the default databases are MONITOR and COGNOSCS
- For the qmbpmaps profile, the default databases are QBPMDB, QPDWDB,
QCMNDB, MONITOR, and COGNOSCS
- For the qmesb profile, the default databases are ECMNDB, QECMNDB,
MONITOR, and COGNOSCS

You should also ensure that all old profiles are correctly
deleted from the file system. The following directories may include
old information and may need to be cleaned up:

- BPM\_Home/profiles/profile\_name
- BPM\_Home/logs

If a profile directory already exists with the same name that
you want to use in the new profile, the profile creation will fail.