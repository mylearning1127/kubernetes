# Helm quick lab

```bash
helm lint 11-helm/employee-platform
helm template employee-lab 11-helm/employee-platform
helm install employee-lab 11-helm/employee-platform
helm list -A
helm get values employee-lab -n employee-platform
helm upgrade employee-lab 11-helm/employee-platform --set frontend.replicas=3
helm history employee-lab -n employee-platform
helm rollback employee-lab 1 -n employee-platform
helm uninstall employee-lab -n employee-platform
```

This starter chart is intentionally small. The full core lab manifests remain the primary
learning path; extend the chart to include ConfigMaps, Secrets, probes, resources, and storage.
