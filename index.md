# straytorch

`straytorch` is an open-source report generation tool for providing interactive tabular dashboards that assist with data difference comparison from multiple data sources.

## Why straytorch?

There are many existing tools for visualising differences in source code and these tools are often extended to perform diffs of data files such as JSON and YAML. Unfortunately, these tools have a number of drawbacks:

- they operate on the raw file contents and provide poor insights in cases where the data is unsorted. 
- they assume that the consumer understands the source data structures even if they are just interested in the values
- they don't supporting comparing more than two things or become unwieldy when they do.
- they are poor candidates for finding different across a large number of instances such as a use case where we want to see what is difference across a dev, test, UAT, staging and production environment or, when we want to see how data has changed over a long period of time

`straytorch` addresses these issues by:

- automatically flatterning structured data into a tabular view which makes it easier to reason with
- providing interactive features for searching, filtering and sorting against any field
- allowing for reports to be customised to only display what is important

## Getting started

With straytorch, you point it at your directory of data files and it will generate an interactive dashboard where you can inspect and find differences in the data.

```
# export your data (e.g. from target environments)
tree data/
├── dev.yml
├── tst.yml
└── prd.yml

# generate your report
straytorch -c report.yml data/
```

Once your report is generated you can server it up with the HTTP server of your choice

```
# serve your report
python -m SimpleHTTPServer 4444
open http://localhost:4444
```

## Use cases

- Comparing configuration across environments and finding inconsistencies
- Comparing versions of data or an environment at points in time
- Detecting configuration drift for an environment since it was last updated
- Finding differences in terraform state files or any other json-based data format

## Got a question or suggestion?

Please feel free to [start a discussion](https://github.com/m0un10/straytorch/discussions) over at our github repository.
