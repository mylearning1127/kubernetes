# Kubernetes architecture — quick recall

## Control plane
- **kube-apiserver:** authenticated and authorized API entry point; validates and persists desired state.
- **etcd:** key-value database holding cluster state.
- **kube-scheduler:** chooses a suitable node for unscheduled Pods.
- **kube-controller-manager:** runs controllers that reconcile actual state with desired state.
- **cloud-controller-manager:** optional integration with cloud infrastructure.

## Worker node
- **kubelet:** ensures assigned Pods and containers are running.
- **Container runtime:** containerd or CRI-O, reached through CRI.
- **CNI plugin:** configures Pod networking.
- **kube-proxy:** commonly implements Service forwarding; some clusters replace it.

## Reconciliation example
`kubectl apply` sends desired state to the API server. Controllers notice the Deployment,
create/update a ReplicaSet, and the ReplicaSet creates Pods. The scheduler assigns Pods
to nodes. Kubelet asks the runtime to start containers. Readiness and Service endpoints
determine whether traffic should reach a Pod.

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods -n kube-system -o wide
kubectl api-resources
kubectl describe node
```
