# Reusability

### Api Reusability Classifications - Business & System

We have introduced the possibility to tag your API accordingly to the corresponding API Reusability Classifications while publishing or updating your api. Simply add "reusability": "value" to the request body. There is two potential classification values to choose from, system and business. If none is passed while publishing the value will default to 'business'.


### Business API

- A Business API is a reusable Published API that has a distinct capability within a corporate domain that can be functional or technical
- A Business API has a lifecycle that is independent of any software system that implements the API
- A Business API is designed using system independent API schema standards and technologies such as Open API/Swagger
- A Business API is designed to be part of an Ingka API Catalog that should be perceived as an engineered whole by API consumers
- A Business API follows strict design policies and guidelines related to naming, security, logging, header etc.
- A Business API can be based on any type of API Style (see previous section)
- A Business API must be based on a corporate Data Concept model
- A Business API can be based on a detailed, canonical Data Entity model that represents core API schema payload objects
- Business API design responsibility can sit with team that owns a core system that implements the Business API or with a separate "Canonical API design team" on domain level 
- Business API design and evolution is governed by domain level architects/engineers
- Business APIs represent a key concept for managing system landscape modernization in terms of keeping APIs and substituting underlying software systems

### System Specific API

- A System Specific API is a Published API that is based on System specific data models and design guidelines shared by a single or limited group of consumer systems
- A System Specific API does not have  not expected to live longer than the specific software system
- From an Ingka perspective vendors and partners typically provide System Specific API. In some cases these external APIs can be "promoted" into Business APIscan be  A System 