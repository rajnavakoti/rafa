# TechDocs

This document explains how to create TechDocs for your software components and publish to Allen.

- Official documentation: [TechDocs](https://backstage.io/docs/features/techdocs/)

## Before you begin

Before publishing documentation for your software component, ensure that you have [registered your software component](../catalog/add.md) in Allen's software catalog.

## Add documentation to your repository

Create an `mkdocs.yml` file in the root of your repository with the following content:

```yaml
site_name: 'My documentation'

nav:
  - Home: index.md

plugins:
  - techdocs-core
```

Add the TechDocs annotation to your component's `catalog-info.yaml` file:

```yaml
metadata:
  annotations:
    backstage.io/techdocs-ref: dir:.
```

Create a `docs` folder in the root of the repository and an `index.md` file with the following content:

```md
# My documentation

My amazing documentation.
```

## Publish your documentation

To expose your documentation in Allen, you have two options:

- Use the TechDocs builder
- Publish your documentation via GitHub Actions

You only need to choose one of the options provided below.

### Option 1) TechDocs builder

The TechDocs builder is a service that will build and publish your documentation for your repositry automatically. It will keep track of the default branch of your repository and publish any changes that you push to it.

Enabling the TechDocs builder for your repository is as simple as installing the `ingka-techdocs` app to your github.com repository. You can enable TechDocs builder by clicking the **Enable** button on Allen's homepage for the software component that you want or you can use the [enable TechDocs builder page](https://allen.ingka.com/get-access/techdocs-builder) to install the app to your repository. Once it is enabled, the TechDocs builder will start tracking changes in `mkdocs.yml` and `docs/**` and build and publish your documentation.

**NOTE:** Upon enabling the TechDocs builder make sure to disable any existing jobs or GitHub actions that take care of building and publishing TechDocs.

### Option 2) GitHub Actions

If you need more control over when and how your documentation is built and published, you can make use of our reusable GitHub Actions workflow.

We support repositories in GHEC (https://github.com/ingka-group-digital) and GHES (https://git.build.ingka.ikea.com) instances.

#### Option 2a) GHEC

Create a workflows file in `.github/workflows/publish-techdocs.yaml` with the following content:

```yaml
name: Publish TechDocs

on:
  push:
    branches: [main]

jobs:
  publish-techdocs:
    permissions:
      contents: read
      id-token: write

    uses: ingka-group-digital/developer-portal/.github/workflows/publish-techdocs.yaml@main
    with:
      entity-name: <component name>
      entity-kind: Component
      environment: 'production' # or 'staging'
```

Make sure you swap `<component name>` with your actual component name defined in `catalog-info.yaml`.

#### Option 2b) GHES

Create a workflows file in `.github/workflows/publish-techdocs.yaml` with the following content:

```yaml
name: Publish TechDocs

on:
  push:
    branches: [main]

jobs:
  publish-techdocs:
    permissions:
      contents: read
      id-token: write

    uses: allen/workflows/.github/workflows/publish-techdocs.yaml@main
    with:
      entity-name: <component name>
      entity-kind: Component
      environment: 'production' # or 'staging'
```

Make sure you swap `<component name>` with your actual component name defined in `catalog-info.yaml`.
