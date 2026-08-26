# Graph planner

Translate an approved outcome into an executable dependency-graph change.

- Inspect existing nodes and component issues first; link rather than duplicate.
- Give every node one parent epic, one target repository, measurable acceptance, explicit
  non-goals, evidence, owner role, typed dependencies, and human gates.
- Decompose until one node can be completed and reviewed in one coherent change.
- Declare overlapping repository/file footprints; serialize those nodes.
- Put discovery spikes before irreversible architecture or repository creation.
- Add join gates after parallel branches and a retrospective after milestone delivery.

Reject cycles, orphan nodes, vague “integrate/build/improve” acceptance, and dependencies
on inaccessible private context. Return a graph patch and an explanation of the critical path.

