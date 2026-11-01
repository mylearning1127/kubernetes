# Reliability and scaling

```bash
minikube addons enable metrics-server
kubectl top nodes
kubectl top pods -n employee-platform
kubectl describe hpa employee-api-hpa -n employee-platform
```

HPA needs resource requests and working metrics. Scale-down is not immediate: stabilization
windows and scaling policies can delay/restrict it. VPA requires separately installed
components and its CRDs. Do not let HPA and VPA independently fight over CPU/memory
requests without understanding their interaction.

A PDB protects against some voluntary disruptions through the Eviction API; it does not
protect against node failure or direct Pod deletion. A single-node cluster cannot show
real node-level high availability.
