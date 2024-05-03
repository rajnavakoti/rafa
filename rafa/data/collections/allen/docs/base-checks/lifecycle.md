# Lifecycle check

## Introduction

Verifies that entity has lifecycle set to a valid value. We implement the lifecycle model [published by EA](https://confluence.build.ingka.ikea.com/x/UE_3Hg)

## Entity type

`Component`

## Validation rules

- `spec.lifecycle`is set for entity
- Value in [`experimental`, `emerging`, `production`, `deprecated`, `sunset`, `retired`]

## How to fix

- Make sure entity has `spec.lifecycle` set.
- Make sure value is supported

## More information

- [Catalog-info.yaml](../catalog/add.md#catalog-infoyaml)
