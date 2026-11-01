# Kubernetes concept map

- Desired state: manifests submitted to the API server.
- Controllers: reconciliation loops.
- Pod: smallest deployable unit.
- ReplicaSet: maintains a matching number of Pods.
- Deployment: manages ReplicaSets and rollout history.
- Service: stable virtual endpoint for matching Pods.
- Ingress: HTTP(S) routing rules; needs an Ingress controller.
- ConfigMap/Secret: inject configuration.
- PV/PVC/StorageClass: storage supply, claim, and provisioning class.
- StatefulSet: stable Pod identity and storage association.
- Job/CronJob: finite and scheduled work.
- DaemonSet: node-level workload.
- HPA/VPA: horizontal and vertical resource scaling.
- PDB: limits voluntary disruption.
- RBAC: API permissions.
- NetworkPolicy: Pod network traffic policy, if enforced by CNI.
- CRD/Operator: extend API and automate domain-specific reconciliation.
- Helm: package and release manager.
