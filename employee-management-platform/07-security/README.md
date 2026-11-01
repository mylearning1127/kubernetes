# Security / RBAC

Apply ServiceAccounts, Role, RoleBinding, ClusterRole and ClusterRoleBinding separately.
Check permissions:

```bash
kubectl auth can-i list pods --as=system:serviceaccount:employee-platform:employee-viewer -n employee-platform
kubectl auth can-i delete pods --as=system:serviceaccount:employee-platform:employee-viewer -n employee-platform
kubectl auth can-i get nodes --as=system:serviceaccount:employee-platform:employee-viewer
```

`--as` impersonation requires the caller to have impersonation permission. A Role is
namespace-scoped; a ClusterRole can describe cluster-wide or reusable permissions.
A RoleBinding can bind a ClusterRole within one namespace; ClusterRoleBinding grants
cluster-wide scope. Follow least privilege.
