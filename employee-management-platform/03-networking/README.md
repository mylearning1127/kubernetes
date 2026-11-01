# Networking labs

Apply `clusterip.yaml` and `frontend-service.yaml` for the core app.
`nodeport.yaml`, `loadbalancer.yaml`, and Ingress are alternative exposure methods;
you can keep more than one for comparison, but remove unused resources afterwards.

```bash
kubectl get svc -n employee-platform
kubectl get endpointslices -n employee-platform
kubectl get ingress -n employee-platform
kubectl describe svc employee-api -n employee-platform
kubectl port-forward svc/employee-api 8080:80 -n employee-platform
curl http://127.0.0.1:8080/
```

DNS examples from a Pod:
- Same namespace: `employee-api`
- Cross namespace: `employee-api.employee-platform`
- Full name: `employee-api.employee-platform.svc.cluster.local`

NetworkPolicy is only enforced if the cluster networking implementation supports it.
