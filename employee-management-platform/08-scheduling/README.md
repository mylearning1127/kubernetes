# Scheduling labs

Label a node for the selector demo:

```bash
kubectl label node minikube lab-role=general
kubectl apply -f 08-scheduling/node-selector.yaml
kubectl describe pod employee-node-selector-demo -n employee-platform
```

Taint demonstration (be careful: this can affect other workloads):

```bash
kubectl taint nodes minikube dedicated=employee-lab:NoSchedule
kubectl apply -f 08-scheduling/taints-tolerations.yaml
kubectl taint nodes minikube dedicated=employee-lab:NoSchedule-
```

A toleration permits scheduling onto a tainted node; it does not attract a Pod there.
NodeSelector/required affinity constrain placement. Preferred affinity is a preference.
Pod anti-affinity and topology spread need enough eligible topology domains for meaningful
distribution. Remove demo Pods after testing.
