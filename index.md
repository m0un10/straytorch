# straytorch

`straytorch` is an open-source report generation tool for providing interactive tabular dashboards that assist with data difference comparison from multiple data sources.

## Why straytorch?

There are many existing tools for visualising differences in source code and these tools are often extended to perform diffs of data files such as JSON and YAML. Unfortunately, these tools operate on the source file contents (not the sorted content) which means they generally provide poor insights in cases where the data is unsorted. Furthermore, as the number of comparison sources grows beyond 2 files, it becomes difficult to gain insight into what differences are important. Because of this, existing tools are often poor candidates for finding differences across a large number of instances such as a use case where we want to see what is difference across a dev, test, UAT, staging and production environment or, how data has changed over a long period of time.

`straytorch` addresses these issues by:

- automatically flatterning structured data into a tabular view
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
