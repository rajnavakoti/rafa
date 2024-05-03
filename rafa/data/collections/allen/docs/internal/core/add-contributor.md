# Add contributor to Vault

To add a contributor to Vault so they can manage their plugin configuration, follow these steps:

1. Make sure you have Vault CLI installed, instructions [here](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install)
2. Run `bash ./hack/add-contributor-to-vault/add-contributor-to-vault.sh <user-id> <team-name>`

- `<user-id>` should be the contributor's IKEA ID.
- `<team-name>` should match the team name in `./terraform/contributors/config.tfvars` e.g. `workflows`.
