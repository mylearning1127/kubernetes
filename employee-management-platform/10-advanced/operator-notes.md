# CRD vs Operator

- A **CRD** adds a new API resource type; a custom resource is an instance of that type.
- A **controller** watches resources and reconciles actual state toward desired state.
- An **Operator** packages domain-specific operational knowledge in one or more controllers,
  commonly alongside CRDs.

Applying a CRD and custom resource stores declarative data. Without a controller that watches
the custom resource, it will not automatically create a Deployment, Service, or database.
