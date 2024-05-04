# Ownership check

## Introduction

Verifies that an entity has owner set to a valid group or user

## Entity type

`Component`

## Validation rules

- `spec.owner`is set for entity with either `user:name` or `group:name`
- If you choose to leave out the kind from `spec.owner` the checker assumes that the owner is a group and performs the validation as such
- Group or user exists (see existing [groups](/catalog?filters%5Bkind%5D=group) or [users](/catalog?filters%5Bkind%5D=user))

## How to fix

- Make sure entity has `spec.owner` set to a valid group or user i.e. `user:name` or `group:name`.
- If your group does not exist, it can be self-serve created in [myidentity.apps.ikea.com](https://myidentity.apps.ikea.com/).

## More information

- [Catalog-info.yaml](../catalog/add.md#catalog-infoyaml)
- [IAM documentation on IAM team groups](https://confluence.build.ingka.ikea.com/display/EKR234IA/Team+Groups+in+Azure+AD)
