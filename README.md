## Development
*Policies and workflows used during Sprint 5.*

---

#### Column Entry Criteria:

| Column           | Entry Criteria                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **To Do**        | - Issue created using a [template](#) (User Story/Bug/Tech Task) <br> - Estimated (time/points) |
| **In Progress**  | - Assigned to team member <br> - Branch created (`feat/xxx` or `fix/xxx`)      |
| **In Review**    | - PR opened with linked issue <br> - PR description uses [template](#) <br> - All CI checks pass |
| **Ready to Deploy** | - PR approved by ≥1 reviewer <br> - Manual tested (if applicable)           |
| **Done**         | - Merged to `main` <br> - Issue closed with resolution notes                 |

---

### Git Workflow
**Base Workflow**: Adapted **GitHub Flow** (trunk-based development)

#### Rules:

skibibi

#### Gitgraph Diagram:
```mermaid
gitGraph
  commit
  branch feat/word-selection
  commit
  commit
  checkout main
  merge feat/word-selection
  branch fix/api-timeout
  commit
  checkout main
  merge fix/api-timeout
