<!-- image -->

# Build it yourself

Start building the Stock Quote sample by importing the starter artifacts and creating
the mediation module for your sample. Resources such as interfaces and business objects can be
contained in the Resources library so that they can be easily shared by modules. Mediation modules
contain mediation flow and Java components, exports to allow the target service in the mediation
module to be called by other modules or clients, and imports which allow services external to the
module to be invoked. The assembly diagram of the mediation module is used to wire the exports,
components, and imports together to form the integrated service application.

1. Import the start artifacts (Resources library and StockQuoteProvider service)
2. Create the mediation module
3. Assemble the mediation module
4. Implement the mediation