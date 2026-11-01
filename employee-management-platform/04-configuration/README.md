# ConfigMap and Secret notes

- ConfigMap stores non-sensitive settings.
- Secret stores sensitive values, but base64 encoding alone is not encryption.
- Environment variables are fixed when the container starts; recreate Pods to consume changes.
- Mounted ConfigMap/Secret files are updated eventually (not when mounted using `subPath`);
  the application may still need to reload the file.
- Use RBAC and encryption at rest; prefer an external secret manager for production.
