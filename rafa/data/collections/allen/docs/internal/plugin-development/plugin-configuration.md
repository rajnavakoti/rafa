# Plugin configuration

The configuration for Allen is stored in [Vault](https://vault-prod.build.ingka.ikea.com). Plugins might require different configuration for production and staging which can include sensitive data, so to manage this configuration for your plugins follow these steps:

1. Open `./terraform/contributors/config.tfvars` and add your team in the `teams` variable.

```
teams = {
  # ...
  "<team-name>" : {
    allowedJSONPaths : ["<path1>", "<path2>"] # The yaml path prefix where your plugin configuration is defined e.g. `workflows.` if your configuration is under `workflows:`
  },
}
```

The above configuration will create two secrets in Vault for staging and production which value will be merged into `app-config.yaml` on application startup.

2. Open a pull request with the changes, specify the network IDs of the people that should have access to the config in the description, wait for it to be approved and merged.

3. Login to Vault [here](https://vault-prod.build.ingka.ikea.com/ui/vault/secrets/allen/list?namespace=provisioning-pipelines), choose "OIDC" in the method field and click "Sign in with Auth0".

4. You should be able to see the two entries: `production` and `staging`.

5. In each of the entries, there should be a `app-config.<team-name>.yaml` entry which contains the configuration for your plugin.

6. Open the entry and use the "create new version" button to edit it.

The configuration will be applied on the next deployment to the respective environment.
