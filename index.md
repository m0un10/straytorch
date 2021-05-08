
`straytorch` provides an interactive tabular dashboard for viewing difference reports generated from multiple data sources.

With straytorch, you point it at your directory of JSON files and it will generate a HTML report where you can inspect and find differences.

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
