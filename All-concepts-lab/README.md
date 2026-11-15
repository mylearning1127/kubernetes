# Kubernetes All-Concepts Practical Lab — Employee Directory
Browser frontend → API → PostgreSQL, plus worker and node agent. Apply manifests numerically.

## Build images (Minikube Docker driver)
```bash
eval "$(minikube docker-env)"
docker build -t employee-api:1.0 ./app/api
docker build -t employee-frontend:1.0 ./app/frontend
docker build -t employee-worker:1.0 ./app/worker
```
For containerd-based Minikube, use `minikube image build -t IMAGE PATH`.

## Apply in order
```bash
kubectl apply -f manifests/00-namespace.yaml
kubectl apply -f manifests/01-rbac-serviceaccount.yaml
kubectl apply -f manifests/02-configmap.yaml
kubectl apply -f manifests/03-secret-demo.yaml
kubectl apply -f manifests/04-postgres-storage.yaml
kubectl apply -f manifests/05-postgres-statefulset.yaml
kubectl apply -f manifests/06-api-deployment.yaml
kubectl apply -f manifests/07-api-service.yaml
kubectl apply -f manifests/08-worker-deployment.yaml
kubectl apply -f manifests/09-frontend-deployment.yaml
kubectl apply -f manifests/10-frontend-service.yaml
kubectl apply -f manifests/11-ingress.yaml
kubectl apply -f manifests/12-networkpolicy.yaml
kubectl apply -f manifests/13-pdb.yaml
kubectl apply -f manifests/14-hpa.yaml
kubectl apply -f manifests/15-cronjob.yaml
kubectl apply -f manifests/16-job.yaml
kubectl apply -f manifests/17-daemonset.yaml
```
Ingress, NetworkPolicy, HPA have prerequisites: enable ingress addon, use a policy-enforcing CNI, and metrics-server respectively. HPA may remain pending until metrics-server is ready.

## Verify
```bash
kubectl get all,pvc,ingress,networkpolicy,pdb,hpa,cronjob,job -n employee-platform
kubectl rollout status deploy/employee-api
kubectl logs deploy/employee-api
minikube service employee-frontend -n employee-platform
```
Demo password in Secret is deliberately insecure—training only. See `docs/19-practical-exercises.md` for practical drills including rollouts/undo, endpoints, probes, storage persistence, HPA, RBAC, scheduling, security, Helm, VPA, CRDs.
