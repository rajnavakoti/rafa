# Valid system in System Master Catalog (SMC)

## Introduction

Verifies that entity has system set to a valid system in System Master Catalog (SMC)

## Entity type

`Component`

## Validation rules

- `spec.system`is set for entity
- System exists (see [existing systems](/catalog?filters%5Bkind%5D=system))

## How to fix

- Make sure entity has `spec.system` set to a valid system.
- If your system does not exist yet, please initiate a creation in SMC.

## More information

- [Catalog-info.yaml](../catalog/add.md#catalog-infoyaml)
- [Create a new system - quick guide](https://confluence.build.ingka.ikea.com/x/doQBGg)
