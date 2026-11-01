# Rollout and rollback lab

```bash
kubectl set image deployment/employee-rollout-demo web=nginx:1.29 -n employee-platform
kubectl rollout status deployment/employee-rollout-demo -n employee-platform
kubectl rollout history deployment/employee-rollout-demo -n employee-platform
kubectl rollout undo deployment/employee-rollout-demo -n employee-platform
kubectl rollout history deployment/employee-rollout-demo -n employee-platform
```

`RollingUpdate` gradually replaces Pods. `Recreate` terminates old Pods before creating
new ones. A rollback restores a previous workload template; it does not reverse database
migrations, messages already sent, or other external side effects.
