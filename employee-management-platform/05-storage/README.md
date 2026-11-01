# Storage labs

- `emptydir.yaml`: shared scratch space; removed with the Pod.
- `persistent-volume.yaml` + `persistent-volume-claim.yaml`: static hostPath PV/PVC demo.
- `postgres-pvc.yaml` + `postgres-deployment.yaml`: core persistent database.
- `storageclass-example.yaml`: illustrative provisioner only; `example.com.invalid` is not real.
- `postgres-statefulset.yaml`: alternative StatefulSet with stable identity and per-Pod PVC.

Access modes:
- RWO: read/write mounted by one node (not necessarily only one Pod).
- ROX: read-only mounted by many nodes.
- RWX: read/write mounted by many nodes.
- RWOP: read/write by one Pod, where supported.

Reclaim policies: Retain, Delete, and legacy Recycle (deprecated/removed in modern versions).
CSI snapshots require a CSI driver, snapshot controller, and VolumeSnapshot CRDs.
