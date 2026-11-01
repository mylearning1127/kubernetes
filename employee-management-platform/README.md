# Employee Management Platform — Kubernetes Revision Lab

A lightweight, educational Employee Management Platform for practising Kubernetes.
It contains a small web frontend, Python API, background worker, PostgreSQL database,
batch jobs, manifests, security examples, scheduling examples, Helm chart, and labs.

> **Lab, not production:** credentials are demonstration-only, the API is intentionally
> simple, and several manifests are alternatives that should not all be applied at once.
> Review each file before applying it.

## Requirements

- Minikube with Docker driver (2 CPU / 4 GB RAM is enough for the core lab)
- kubectl, Docker, and optionally Helm
- A working internet connection to pull base images
- For optional features: NGINX Ingress addon, Metrics Server, and a CNI that enforces NetworkPolicy

## Quick start

```bash
minikube status
kubectl get nodes -o wide

# Build images inside Minikube's Docker environment.
eval "$(minikube docker-env)"
docker build -t employee-frontend:1.0 ./application/frontend
docker build -t employee-api:1.0 ./application/api
docker build -t employee-worker:1.0 ./application/worker

# Create namespace and configuration.
kubectl apply -f 02-workloads/namespace.yaml
kubectl apply -f 04-configuration/configmap.yaml
kubectl apply -f 04-configuration/secret.yaml

# Deploy PostgreSQL and application workloads.
kubectl apply -f 05-storage/postgres-pvc.yaml
kubectl apply -f 05-storage/postgres-deployment.yaml
kubectl apply -f 05-storage/postgres-service.yaml
kubectl apply -f 02-workloads/frontend-deployment.yaml
kubectl apply -f 02-workloads/api-deployment.yaml
kubectl apply -f 02-workloads/worker-deployment.yaml

# Expose frontend inside the cluster and on a Minikube node port.
kubectl apply -f 03-networking/clusterip.yaml
kubectl apply -f 03-networking/nodeport.yaml

kubectl get all -n employee-platform
kubectl get pvc -n employee-platform
kubectl get endpointslices -n employee-platform

# Open the app.
minikube service employee-frontend-nodeport -n employee-platform
```

If using `minikube docker-env` in a new terminal, run `eval "$(minikube docker-env)"`
again before rebuilding. The Deployments use `imagePullPolicy: IfNotPresent` so the
locally built images can be used.

## Suggested learning order

1. `01-architecture/architecture-notes.md`
2. `02-workloads/` — Pod, multi-container Pod, ReplicaSet, Deployment, DaemonSet, Job, CronJob
3. `03-networking/` — Service types, Ingress, DNS, EndpointSlices, NetworkPolicy
4. `04-configuration/` — ConfigMap, Secret, env vars and mounted files
5. `05-storage/` — emptyDir, PV, PVC, StorageClass, StatefulSet and snapshots
6. `06-reliability-scaling/` — probes, resources, HPA, VPA, PDB
7. `07-security/` — ServiceAccounts, RBAC and security context
8. `08-scheduling/` — selectors, affinity, anti-affinity, taints and tolerations
9. `09-operations/` — rollout, rollback and troubleshooting
10. `10-advanced/` — CRD and Operator concepts
11. `11-helm/` — package and release management

## Core workload map

| Component | Kubernetes resource | Purpose |
|---|---|---|
| Frontend | Deployment + Service | Web UI |
| API | Deployment + Service | Employee API |
| Worker | Deployment | Background task consumer |
| PostgreSQL | Deployment + PVC | Single lab database |
| Daily report | CronJob | Scheduled report |
| One-time report | Job | Batch task |

## Useful commands

```bash
kubectl get all -n employee-platform
kubectl get pods -n employee-platform -o wide
kubectl describe pod <pod-name> -n employee-platform
kubectl logs deployment/employee-api -n employee-platform
kubectl logs <pod-name> -n employee-platform --previous
kubectl exec -it deployment/employee-api -n employee-platform -- sh
kubectl get events -n employee-platform --sort-by=.metadata.creationTimestamp
kubectl top pods -n employee-platform
kubectl rollout status deployment/employee-api -n employee-platform
kubectl rollout history deployment/employee-api -n employee-platform
kubectl rollout undo deployment/employee-api -n employee-platform
kubectl auth can-i list pods --as=system:serviceaccount:employee-platform:employee-viewer -n employee-platform
```

## Cleanup

```bash
kubectl delete namespace employee-platform
```

This removes namespaced resources. A manually-created PV may remain depending on its
reclaim policy. Inspect PVs before deleting them. Minikube's hostPath data is lab data.
