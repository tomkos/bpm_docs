<!-- image -->

# Correlating BPEL processes

## Correlation sets

Correlation sets are initialized with values from process
inbound or outbound messages.

1. A partner call is made, and an instance of the process is initialized.
2. Correlation tokens are gathered for the partner.
3. Communication is terminated for some reason. Usually because one
of the participants needs to gather some more information independently.
4. Communication is reestablished, the tokens gathered earlier are
used to confirm that the same partner is interacting with the same
instance of the process.
5. The process continues running.

To illustrate how a correlation set might be used in a
real world setting, imagine that you call a travel agent to ask about
a trip. In this, the initial conversation, you tell the agent what
you're interested in, and she gives you a quote. You tell her that
you want to think about it, so she gathers some specific contact information
about you (name and phone number), and you end the conversation. A
week later, you have made up your mind, and you call the travel agent
again and give her your contact information. With this, she is able
to identify you, and pulls up your quote on her computer. You conclude
your business.

In this example, the correlation set is the contact
information that the agent stores so that she'll be able to recognize
you in future correspondence. She does not stop everything else that
she's doing while you decide what you want to do, instead she conducts
similar business with other customers, and picks up your request where
it left off when you reinitiate contact.

## Correlation properties

Correlation properties
contain a name and a data type and define the correlation sets with
which they are associated. In addition, you can map a message parameter
to a correlation property using a property alias.

## Property aliases

In the previous example,
mention was made of tokens. Correlation tokens refer to specific message
parts in your process. Sometimes you may find that you want to correlate
a property to a message part from another interface. They may have
what is essentially the same kind of content, but use different names,
so you will need to tell the system that they are analogous. You would
do this with an alias. For example, you would use an alias to tell
the system that whenever it encounters a message part called lastName,
it should assume that it means the same as the other message part
called familyName.

Aliases are especially
useful in abstract BPEL processes that can't always fully expose their
data. These kinds of processes need to make all of the business logic
apparent to each of its partners, but often can't afford to reveal
sensitive business data. In this context, aliases allow for the fact
that two message parts may have the same value, but are called something
by one partner, and something entirely different by another. In other
words, aliases recognize that the partners may be using the same data
in the process but are labelling it differently.

For a real
world example, you use aliases most every time that you use a snack-based
vending machine. When you look through the window of the vending machine
to choose the snack that you want to buy, you don't identify the snack
by its proper name, you identify it with a code, usually a combination
of a letter and a number. For example, you may want to buy an oatmeal
cookie, but you don't enter the word "cookie" on the keypad, instead
you enter a code that is unique to that item (for example F6). The
vending machine then knows exactly which snack to dispense.

## Example

- Correlation
- Multiple Correlation Sets

- Configuring correlation sets

Correlation sets are used in runtime environments where there are multiple instances of the same process running. The sets allow two partners to initialize a BPEL process transaction, temporarily suspend activity, and then recognize each other again when that transaction resumes.

## Related reference

- Correlation tab: BPEL process editor
- Defaults tab: BPEL process editor
- Description tab: business state machine editor