<!-- image -->

# Lifecycle of follow-on tasks

- When any task in the chain is suspended, the entire chain is suspended.
Each task is put into the suspended substate.
- A suspended chain of follow-on tasks can be resumed by any task
in the chain.
- If a task in the chain escalates, all of the follow-on tasks in
the chain are escalated.
- When any task in the chain is terminated, the entire chain is
terminated.
- When the first task in the chain expires, the last task in the
chain is put into the expired state.

- Lifecycle operations that do not conflict with the parent task
are always supported. These are operations, such as claim, cancel
claim, complete, creation and start of subtasks or follow-on tasks.
- Because the chain of follow-on tasks behaves like a single task
to the calling component or person (originator), follow-on tasks do
not support a duration until expiration, but expire when the expiration
timer ends for the first task in the chain.
- Parent tasks and follow-on tasks can be suspended and resumed.
This action suspends and resumes all of the tasks in the chain.
- Follow-on tasks can be terminated.
- Follow-on tasks can have their own escalations so that the owner
of the predecessor task and the originator of the follow-on task can
better control the progress of the follow-on task.
- Follow-on tasks are deleted when their parent task is deleted
or restarted. The deletion of individual follow-on tasks using the
Business Process Choreographer APIs is not supported.

## Example: Follow-on tasks

<!-- image -->

In
an article publishing process, the Review Article task
is claimed by John. He is empowered by the process to review and approve
the legal aspects of articles as well. However, this article describes
the collaboration with a competitor product, and is thus very sensitive
from a legal point-of-view. He reviews the informational aspects of
the article, and decides to pass the article on to Sarah from the
legal department for additional review. He creates a Legal
Review task, with a description that highlights his legal
concerns. He includes the article as input to the task, and then assigns
it to Sarah. He then starts the new task as a follow-on task of his
own Review Article task. His task enters the
forwarded state, and the work on it ends. The process waits for the
response from the invoked Review Article task.

Sarah
claims her Legal Review follow-on task and
starts reviewing the legal aspects. She makes some comments, and completes
her task. The output message of the follow-on task is passed to the
BPEL process. The article publishing process continues with the output
that it associates with the Review Article task,
but that comes from the Legal Review follow-on
task. Because the Review Article task is an
inline human task, it is deleted with the Legal Review task
when the BPEL process instance is deleted.

<!-- image -->