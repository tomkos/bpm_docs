# Setting repository preferences in Installation Manager

If you start Installation Manager directly (for example
from a repository located on a web server), you must specify the URL
for the directory that contains the product package in Installation
Manager before you can install the product package.

## Before you begin

By default, Installation Manager uses an
embedded URL in each software development product to connect to a
repository server through the Internet and search for installable
packages and new features. Your organization may require you to redirect
the repository to use intranet sites.

## About this task

## Procedure

1. Start Installation Manager.
2. On the Start page of Installation
Manager, click  File  > Preferences, and then click Repositories.
The Repositories page opens, showing any available repositories,
their locations, and whether they are accessible.
3. On the Repositories page, click Add
Repository.
4. In the Add repository window, type the URL of the repository location or
browse to it and set a file path.
The repository location is typically
image\_directory/disk1/diskTag.inf, where
image\_directory contains the extracted installation image of the product you want
to install.
5. Click OK. The new
or changed repository location is listed. If the repository is not
accessible, a red x is displayed in the Accessible column.
6. Click OK to exit.

## What to do next