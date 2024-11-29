# Troubleshooting the launchpad application or Quick Start

## Troubleshooting the launchpad application

<!-- image -->

```
set BROWSER=Mozilla
```

If the launchpad links still do not work after you have tried these tips,
start the component installation programs directly.

## Troubleshooting Quick Start

On Windows operating systems, Quick Start opens by
default in Internet Explorer. On Unix and Linux systems, Quick Start opens by default in Firefox.

1. Navigate to
HKEY\_LOCAL\_MACHINE\SOFTWARE\Clients\StartMenuInternet\FIREFOX.EXE\shell\open\command.Note: The
preceding line might be word-wrapped. Be sure to navigate to the location specified in the preceding
lines, up to the command key in the registry.
2. Change the (Default) entry so that spaces are removed from the path. For
example, if the path is set as C:\Program Files\Mozilla Firefox\firefox.exe,
change the path to its short equivalent C:\Progra~1\Mozill~1\firefox.exe.The
short names might not be the same on all systems. For example, if you have installed Mozilla
Thunderbird in addition to Mozilla Firefox, and both are installed in the Program
Files directory, the short name to the location of Mozilla Firefox might be different
from that in the previous example. You can use the dir /X command to determine
the short names of individual files and directories that are located in the current
directory.Note: If you choose this option, be careful that the Windows registry does not become corrupted. This key might vary for different locales, so use
caution or choose another workaround. It is recommended that you back up the registry before you
make any changes.

1. Set Windows Internet Explorer as the default
browser.
2. Reset Mozilla Firefox as the default browser. This action automatically changes the registry
entry in the first workaround so that the spaces are removed.This works only when you set the
default browser from within the Mozilla Firefox application. It does not work if you use Add/Remove Programs > Set Program Access and Defaults.

- Quick Start console fails to start on the Windows operating system

To run Quick Start on Windows, you must use the administrator privilege. This is required for both administrative and non-administrative users.