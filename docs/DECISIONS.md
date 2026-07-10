# Architecture Decision Log

This file records major architectural decisions made during the project.

---

## ADR-001

### Decision

Use FastAPI as the backend framework.

### Reason

- High performance
- Automatic OpenAPI documentation
- Excellent typing support
- Modern Python ecosystem

### Alternatives

- Flask
- Django

### Result

Accepted

---

## ADR-002

### Decision

Use Docker for every backend service.

### Reason

Ensures consistent environments across development and deployment.

### Result

Accepted

---

## ADR-003

### Decision

Use Kubernetes for orchestration.

### Reason

Demonstrates production deployment, scalability, and cloud-native design.

### Alternatives

Docker Compose only

### Result

Accepted

---

## ADR-004

### Decision

Support multiple LLM providers through a provider abstraction layer.

### Reason

Avoid vendor lock-in.

Improve extensibility.

### Alternatives

Hardcode Gemini.

### Result

Accepted

---

## ADR-005

### Decision

Use an Adaptive Planner instead of direct LLM invocation.

### Reason

Separates orchestration from intelligence.

Supports multi-agent workflows.

### Result

Accepted

---

## ADR-006

### Decision

Use observability from the beginning.

### Reason

Every major component should expose metrics for monitoring and debugging.

### Result

Accepted