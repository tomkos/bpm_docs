<!-- image -->

# Customizing people assignment criteria

1. Copy one of XML files that contain the people assignment criteria
definitions to a convenient location. These files must be extracted
from com.ibm.wbit.tel.ui\_version\_number.jar which
can be found in the shared\_resources/plugins directory
(typically on Windows, the shared\_resources directory
is C:\Program Files\IBM\SDP70Shared).
2. In the copied version of the file, make the necessary changes.
3. Restart IBM® Integration
Designer.
4. Add the new file to the workspace. From the main menu select File > Import > General > File
System and then browse to the new file. In the Into
folder field select any module or folder within a module,
the new file only needs to be part of the workspace to be available.
Click Finish.
5. Edit the human task preferences page and add a pointer to your
customized XML file, optionally making it the default choice. See
related tasks for details about setting human task preferences.