# Troubleshooting exercises

| Symptom | Investigation |
|---|---|
| Pending | `kubectl describe pod`; inspect scheduler events, requests, affinity, taints, PVC |
| ImagePullBackOff | `kubectl describe pod`; inspect image name, tag, registry access |
| CrashLoopBackOff | `kubectl logs POD --previous`; inspect command, config, dependencies |
| NotReady | `kubectl describe pod`; inspect readiness probe and dependency |
| Service has no backends | Check Service selector against Pod labels; inspect EndpointSlices |
| PVC Pending | `kubectl describe pvc`; inspect StorageClass, PV, access mode |
| HPA unknown metrics | Check Metrics Server and `kubectl top pods` |
| Ingress not routing | Check IngressClass, controller Pods, host header, Service and endpoints |

Useful commands:

```bash
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.metadata.creationTimestamp
kubectl describe deployment employee-api -n employee-platform
kubectl logs deployment/employee-api -n employee-platform
kubectl logs POD_NAME -n employee-platform --previous
kubectl exec -it POD_NAME -n employee-platform -c api -- sh
kubectl get svc,endpointslices,ingress -n employee-platform
kubectl get pv,pvc -A
kubectl top nodes
kubectl top pods -A
```

Try deliberately:
1. Change a Deployment image to a nonexistent tag.
2. Change a Service selector so it matches no Pods.
3. Set a nodeSelector to a nonexistent label.
4. Use a PVC with a nonexistent StorageClass.
5. Configure a failing readiness path.
Then diagnose and repair each issue.
