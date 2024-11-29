<!-- image -->

# Design considerations for user interface generation

The following list presents some design considerations
for user interface generation:

- If you have a human task and a business object with an optional X field
that references another business object containing the optional fields Y and Z,
where the Y and Z fields are used to specify detailed
information for the optional X field, then any web-based user
interface that is generated for widgets in Heritage Process Portal spaces,
using the business object and HTML-Dojo technology will contain Add and Remove buttons
that enable you to add or remove the optional fields Y and Z.For
example, assume that you have a Customer business object with an optional Address field
that references an Address business object containing the optional
fields Street and City.
If the Customer business object is used in a human task and you later
use HTML-Dojo technology to generate a web-based user interface for
a widget, the user interface will contain Add and Remove buttons
that enable you to add or remove the optional Street and City fields.
By default, the optional Street and City fields
will not be displayed in the user interface and the optional Address field
will be populated with the value Address,
which is the name of the optional Address business object. If you
choose to add the optional Street and City fields,
they will appear nested under the optional Address field.
- If you use a tCaseFolder business object and IBM Forms to generatea web-based collaboration folder form for a Heritage Process Portal space,you will find that there have been several improvements to the generatedform. For example, the number of entry fields has been reduced inthe form, while the clarity, layout, and usability of the remainingfields and buttons has been enhanced. The generated collaborationfolder form now enables you to:
    - Click an Add link to add new attachments.
    - Click a Remove link to remove existing
attachments.
    - Assign a name to an attachment in the Name field.
    - Specify a URL path to an attachment in the URL field.
    - Specify the name of the user who attached an attachment in the Attached
by field.
    - Click a View link to view an attachment.
    - Access hover help for the fields and links on the form.
- Any human task can use the CaseTaskInterface as its interface.
In particular when you want to enable enhanced dynamic behavior, you
would typically use the CaseTaskInterface as the interface to your
human task. In some instances when you are employing the CaseTaskInterface
you will want to add your own business objects to the process. This
could be achieved by editing the CaseTaskInterface, however, it is
strongly recommended that you do not edit the CaseTaskInterface, since
changes to this interface may render it inappropriate for use as an
interface for human tasks in collaboration scopes.
The preferred
methodology for adding business objects is to create a new interface,
include a parameter of type tCaseFolder in the interface and use this
interface for your human tasks. Similarly you should not modify the
tCaseFolder parameter type. This type is used by the CaseTaskInterface
and any modification might have the same undesirable effect as modifying
the interface.

## Related concepts

- Before you begin: Client types and prerequisites

## Related tasks

- Defining user interfaces for a human task
- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)
- Integrating JavaScript in HTML-Dojo pages
- Preparing to extend generated JSF code
- Customizing clients
- Deploying a generated client to an external runtime environment