# Integrate your components

## Introduction

By adding annotations to the component's `catalog-info.yaml` file you integrate it with tools and services cross the software lifecycle in order for Allen to act as a control plane and provide short feedback loops for the state of your software.

## Kubernetes clusters

In order to surface your Kubernetes objects in Allen in your component's Kubernetes tab, you need to setup the integration between your component and Kubernetes. By default, Allen has integration with the Managed GKE (MGKE) clusters but you can also register your own Google Kubernetes Engine (GKE) clusters.

### Connect your Kubernetes objects to your Allen components

There are two ways to do that, using a common label or a label selector query.

#### Common `backstage.io/kubernetes-id` label

In your `catalog-info.yaml` file, add the `backstage.io/kubernetes-id` annotation:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    backstage.io/kubernetes-id: my-service
  # ...
```

In your Kubernetes manifests, add a label with the same name as the annotation and apply them on the cluster:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-service
  labels:
    'backstage.io/kubernetes-id': my-service # Should match the annotation in `catalog-info.yaml`
spec:
  # ...
```

#### Label selector query annotation

In your `catalog-info.yaml` file, add the `backstage.io/kubernetes-label-selector` annotation:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    backstage.io/kubernetes-label-selector: 'app=my-app,component=my-app'
  # ...
```

This will prompt Allen to query for Kubernetes objects with those labels and surface them in the Kubernetes tab.

### Register your own GKE cluster

If you are not deploying to the Managed GKE (MGKE) clusters, you can register your own GKE cluster in Allen's catalog. Create a `catalog-info.yaml` in one of your repositories with the following content:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: my-cluster
  annotations:
    kubernetes.io/api-server: https://x.x.x.x
    kubernetes.io/api-server-certificate-authority: |
      -----BEGIN CERTIFICATE-----
      MIIDKzCCAhOgAwIBAgIRAIsm1BXXWPZPkkNgdAoU/6QwDQYJKoZIhvcNAQELBQAw
      LzEtMCsGA1UEAxMkODBlNzU1NTktMTk3OC00NDAzLTkwOGQtNDAyMWIxNDc2ZjA2
      MB4XDTIwMTAyMTEzNTgxMloXDTI1MTAyMDE0NTgxMlowLzEtMCsGA1UEAxMkODBl
      NzU1NTktMTk3OC00NDAzLTkwOGQtNDAyMWIxNDc2ZjA2MIIBIjANBgkqhkiG9w0B
      AQEFAAOCAQ8AMIIBCgKCAQEA1WuWdLGQB0QtJAt/rot4XA4/HLb7fvnExGdT6cXB
      Jfu1Eke9029k2f)(K#39fke0fke2m02KEkekK)DvgvWWB443a7mZnr4YkY2WU1Kd
      q2xvOkVBp4s6pofiiUmOaluxg+JLA6TlxWTZ3Dowm6HvxuEhEnJaw4Wn96WEMyPj
      YLYdNEzRhTymiOLXUm3blvVuQNrr7Ae91eXvs7iAO4KZM2P1EGFG21RuU2R8Btuf
      40EXsL4RjtDyAzQ2cqeWMpnMUIJOOxvkRO9bMhpnrV+qkwvrpS8jh3bkUT9uLxSv
      r2B8wcog2joqw3YcW7DXvUmBW7pn6aOOWoiDTRAevNaiYwIDAQABo0IwQDAOBgNV
      HQ8BAf8EBAMCAgQwDwYDVR0TAQH/BAUwAwEB/zjdBgNVHQ4EFgQUPiWvXBBxJjwS
      U7MnJB2S976k6QowDQYJKoZIhvcNAQELBQADggjBAAHWU5kMC5Ud6x7shGo1Jqiz
      RXfI9J1MGxuBQcsF98v6l5Qs+gp5zNlFmhbA6MztuvTW2rnj7cLi+UxfOj5XOTtg
      gdLKniaqkr2Yy3XXpdetjsqHTJddVBV5f1vaccCVMRGxxcauUpAIT0Ws5/Zhy2XK
      UV+wq4pb5jShEdjVBkcVe6lGSwKWYlaz3667qWgzQ6w2JBpHixa2Fd7ISg+SJczu
      8bYB9H1EhyrNCaSKdZKOsAh1YnwKbU8itnyMaqCWurl5XKzhyFzOQKqHIbZWw0p3
      mLEvvzUgVL9BghtP1u7kXKAiZrwkNxPFVTrgnmopcpbOAcVk1jv2IxRJnraE1uo=
      -----END CERTIFICATE-----
    kubernetes.io/auth-provider: google
    kubernetes.io/skip-tls-verify: 'true'
spec:
  type: kubernetes-cluster
  owner: my-team # Change to your team
```

Import this repository to Allen and the cluster will be registered.

Note that the CA certificate is not secret and it is only used by clients to verify the connection to the Kubernetes cluster, so it is safe to have it in Allen's catalog. It does not give access to the cluster by itself.

Access to the cluster is provided via Google OAuth which in turn uses your own personal credentials. If you have access to the cluster in GCP, only then you will be able to see the Kubernetes objects in Allen.

## Cloud Run

To see your Cloud Run service in the component entity page (Cloud Run tab), add the following annotation to the service's `catalog-info.yaml` file:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    google.com/cloud-run-service-id: {project}/{location}/{service} # ingka-dp-provisioner-stage/us-central1/cloud-run-test
    # ...
```

## Sentry

To see your Sentry issues in the Errors tab of your service, add the following annotation to the service's `catalog-info.yaml` file:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    sentry.io/project-slug: my-project-slug # Your Sentry project ID
  # ...
```

## Cloud Build

To see your Cloud Build pipelines in the CICD tab of your service, add the following annotation to the service's `catalog-info.yaml` file:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    google.com/cloudbuild-project-slug: my-project-slug # Your GCP Project ID
  # ...
```

## iLert

To show the iLert on-call schedule and incidents for your service:

Add the user `l-fe-pp-u-itsehbg@ikea.com` to your team if your on-call schedule is private.

Find your alert source integration key:

1. Open an alert source from [alert sources list](https://ingka.ilert.com/source/list.jsf)
2. In the settings tab of the alert source, the API key is your integration key.

Add the following annotation to the service's `catalog.info.yaml` file:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    ilert.com/integration-key: <alert source integration key>
  # ...
```

## Jira

To see Jira project issues and activity stream (from Jira Digital instance) on component entity page, add the following annotation to the component's `catalog-info.yaml` file:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: my-service
  annotations:
    # ...
    jira/project-key: my-project-id
    #jira/component: <example-component> # optional, you might skip value to fetch data for all components
    #jira/token-type: Bearer # optional, used for Activity stream feed. If you are using Basic auth you can skip this
  # ...
```

Next you would need to grant read-only access to the Service Account used to fetch data from your Jira project.

To do so go to [https://jira.digital.ingka.com/plugins/servlet/project-config/%3Cproject-id%3E/roles](https://jira.digital.ingka.com/plugins/servlet/project-config/<project-id>/roles) where <project-id> is your Jira project key. Then click on "Add users to role" button in the top right corner. The user should be set to "l-fe-pp-u-itsehbg@ikea.com" and the role to "Read Only".

If the integration was successful the component entity page should load issues and activity stream from the Jira Digital instance.
