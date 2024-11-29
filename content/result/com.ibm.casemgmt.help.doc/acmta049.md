# Improve performance at case creation time by limiting subfolder structure

For example, you might design a case with up to 10 subfolders directly under the case. As another
example, you might design a case with two subfolders directly under the case and with four
subfolders under each of the higher-level subfolders. Various other combinations might also yield a
predefined subfolder structure of 10 or fewer subfolders.

If your solution requires cases with a more complex subfolder structure, create the folders after
the case is initialized. You can add them programmatically, within an automatic activity process, or
allow users to add them on demand as needed.