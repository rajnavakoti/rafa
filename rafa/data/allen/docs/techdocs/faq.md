# Frequently asked questions

## How do I publish documentation only repositories?

If you have your markdown files in the root directory and not in a `docs/` subfolder, you will need to install a MkDocs plugin that provides this functionality and configure the `mkdocs.yml` file accordingly.

- In the GitHub actions example, add `mkdocs-same-dir` to the `pip install` step:

```yaml
- name: Install mkdocs and mkdocs plugins
  run: python -m pip install mkdocs-techdocs-core==0.* mkdocs-same-dir
```

- In `mkdocs.yml` set:

```yaml
site_name: 'My documentation'
docs_dir: '.'
site_dir: '.'

nav:
  - Home: README.md

plugins:
  - techdocs-core
  - same-dir
```

For reference, you can take a look at the following repository [Engineering-Baseline](https://github.com/ingka-group-digital/Engineering-Baseline).

## How do I validate or test techdocs locally?

Install npm (node.js) if it is not in your local system. Check with below commands.

```sh
npm -h
```

Install techdocs software/plugin in your local using below commands.

```sh
npm install -g @techdocs/cli
```

Go to your repository where `mkdocs.yaml` and `docs/` folder are located and run the below command.

```sh
techdocs-cli serve
```

A browser will be open in your local and the document will look like below:

![techdocs local](../assets/techdocs_local.png)

### References

- https://backstage.io/docs/features/techdocs/cli
- https://www.mkdocs.org/user-guide/installation/
