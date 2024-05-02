# API entity is linked to a Component entity

## Introduction

Verifies that the API entity has a relation to a component entity

## Entity kind

`API`

## Validation rules

- `spec.providesApis` is set for the component entity
- The component entity exists in the catalog (see [existing components](/catalog?filters%5Bkind%5D=component))

## How to fix

- Make sure that the component entity has `spec.providesApis` set and it contains reference to the API entity
- If your component does not exist yet, please follow the [guide](../catalog/add.md) on how to add one.

## More information

- [Add a component to the software catalog](../catalog/add.md)
- You can use the facts [endpoint](https://allen.ingka.com/api/ingka-team-insights/facts?factIds[]=apiComponentRelationFactRetriever&kind=api) to retrieve the facts for all API entities in the catalog
