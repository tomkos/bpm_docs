# Silently installing and uninstalling Installation Manager

IBM® Installation
Manager can be silently installed and uninstalled.

## Silently installing Installation Manager

### Procedure

To install Installation Manager silently:

1. Extract the installer and switch to the InstallerImage\_platform
subdirectory.
2. Run the following command:

extract\_directory\IM\_win64\installc --launcher.ini -acceptLicense
silent-install.ini -log <log file path and name> For example:
extract\_directory\IM\_win64\installc --launcher.ini -acceptLicense
silent-install.ini -log c:\mylogfile.xmlNote: If you already have 32-bit Installation
Manager installed, then you can run the command from the
extract\_directory\IM\_win32\tools directory.

### What to do next

<!-- image -->

## Silently uninstalling Installation Manager from Windows

### Procedure

To silently uninstall Installation Manager from Windows:

1. From a command line, go to the uninstall directory for
the Installation Manager. By default, this is C:\Documents
and Settings\All Users\Application Data\IBM\Installation Manager\uninstall.
2. Enter the following command: uninstallc.exe
--launcher.ini silent-uninstall.ini