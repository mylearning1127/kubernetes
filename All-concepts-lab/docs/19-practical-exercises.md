# Exercises — complete in this order
1. Labels/selectors: `kubectl get pods --show-labels`; `kubectl get pods -l app=employee-api`.
2. ReplicaSets: scale API Deployment to 3 and inspect ReplicaSets; return to 2.
3. Rolling update and undo: build API image 2.0, update image, `rollout status`, `rollout history`, `rollout undo`.
4. ConfigMap change: alter DB host and observe environment update behavior (restart Pods).
5. Secret: learn secretKeyRef; demo credential is not for production.
6. Service/endpoints: `kubectl get endpoints employee-api`; delete a pod and observe endpoint recovery.
7. Ingress: enable addon, configure employees.local resolution; compare NodePort access.
8. PVC/PV: remove PostgreSQL Pod and verify records remain on persistent volume.
9. Probes: intentionally set wrong readiness path and compare Running/Ready.
10. Resource requests/limits: create too-high requests and diagnose Pending events.
11. HPA: enable metrics-server, check `kubectl top pods`, generate load through `/api/demo-load?seconds=8`.
12. PDB: test drain/eviction in a multi-node cluster.
13. Job/CronJob: view Jobs and logs; create one-off job from CronJob.
14. DaemonSet: desired/current Pod counts across nodes.
15. RBAC: `kubectl auth can-i list pods --as=system:serviceaccount:employee-platform:employee-app -n employee-platform`.
16. NetworkPolicy: verify CNI enforcement.
17. Scheduling: experiment with nodeSelector, affinity, anti-affinity, taints/tolerations.
18. Security: add runAsNonRoot, readOnlyRootFilesystem, drop capabilities and test.
19. Helm: convert manifests into chart templates and values for replica/image settings.
20. VPA: install VPA components separately; start in recommendation-only mode.
21. CRD/operator: study custom resources/operators after core concepts.
22. Debug: `describe`, Events, logs, exec, port-forward, rollout history.
