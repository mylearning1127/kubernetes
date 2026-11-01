# Coverage checklist

This project intentionally includes both runnable core manifests and optional comparison
manifests. Some resources are mutually exclusive or require cluster add-ons.

- [x] Namespace, standalone Pod, multi-container Pod, ReplicaSet, Deployment
- [x] DaemonSet, Job, CronJob
- [x] ClusterIP, NodePort, LoadBalancer, Ingress, path routing, NetworkPolicy
- [x] ConfigMap, Secret, environment variables, mounted configuration
- [x] emptyDir, PV, PVC, StorageClass example, PostgreSQL PVC, StatefulSet
- [x] Liveness, readiness, startup probes; requests and limits
- [x] HPA, VPA, PDB
- [x] ServiceAccounts, Role, RoleBinding, ClusterRole, ClusterRoleBinding
- [x] Security context
- [x] NodeSelector, node affinity, Pod affinity/anti-affinity, taints/tolerations,
      topology spread
- [x] RollingUpdate, Recreate, rollback and troubleshooting exercises
- [x] CRD, custom resource, Operator explanation
- [x] Helm chart
- [x] Architecture and concept notes

See each directory's README and the root README before applying optional resources.
