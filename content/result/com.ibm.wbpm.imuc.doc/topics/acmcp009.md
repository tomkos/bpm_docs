# Integrating IBM
Watson Explorer Analytical Components

## Before you begin

## About this task

The IBM
Watson Explorer Analytical Components crawler for case management solutions can
be configured with filters to include or exclude specific objects, such as case type, document
class, file extension, or document name pattern.

The crawler also indexes cases for specific properties, for example, name, state, creation date,
or comments. You can specify which properties to index in the IBM
Watson Explorer Analytical Components administration console.

You configure a collection in IBM
Watson Explorer Analytical Components by specifying
the location of the content source, parameters for discovery, and parameters for content analysis.
You can then use the IBM
Watson Explorer Analytical Components content analytics miner
application to explore the analyzed content, discover unexpected correlations between words and
phrases, and see which words and phrases occur frequently in many cases.

You can use multiple views to explore the analyzed
content from different perspectives. For example, you might want to
explore trends or deviations in the data, or you might want to look
for connections between cases by exploring correlation and frequency
values through two facets at the same time.

As you explore a
collection and view the results, you can iteratively fine tune your
query, zoom in on particular items of interest, and expand or narrow
the set of case documents that you want to focus on.

## Procedure

To configure IBM
Watson Explorer Analytical Components for IBM Business Automation
Workflow:

1. Install the Content Platform Engine Client software on the IBM
Watson Explorer Analytical Components crawler server.
For more information, see Configuring the crawler server to support IBM Business Automation
Workflow and FileNet P8
crawlers.
2. In the IBM
Watson Explorer Analytical Components administration console, create a
collection for your IBM Business Automation
Workflow content.
For more information, see Creating a collection.
3. In the IBM
Watson Explorer Analytical Components administration console, create the
IBM Business Automation
Workflow crawler.
To create the crawler, you run a wizard that helps you identify the content that you want to
crawl, or analyze, as well as additional settings such as security options. For more information,
see Case Manager crawlers.
4. Set up text analysis rules.
This task is usually performed by a business analyst or subject matter expert who determines
how the text will be analyzed. For more information, see Analytic resources and content analytics.
5. Set up a schedule for running the IBM Business Automation
Workflow
crawler.
For more information, see Crawler schedules.
6. After the crawler runs, use the content analytics miner application to view, query, and analyze
the collected, indexed data.
For more information, see Analyzing content.

- Installing IBM Watson Explorer Analytical Components

IBM Watson Explorer Analytical Components is a tool for crawling and interactively analyzing the text and metadata of documents and content objects. IBM Watson Explorer Analytical Components provides a specific IBM Business Automation Workflow Crawler, which can be used to analyze case comments in a case management system. IBM Watson Explorer Analytical Components is a separate installation and configuration from IBM Business Automation Workflow.