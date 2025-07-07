## Development 
### Kanban board
link to the Kanban board: https://github.com/orgs/AnkiGen/projects/2/views/1
| Column            | Entry Criteria |
|-------------------|----------------|
| To Do         | - Issue is created with a clear description<br>- Priority and estimation are added<br>- Follows the issue template<br>- Linked to a Milestone|
| In Progress   | - Branch created <br>- Assignee is set<br>|
| Ready to Deploy | - MR is approved<br>- No merge conflicts<br>- All review feedback is addressed |
| Done          | - User feedback is received<br>- Critical bugs are fixed (or split into new issues)<br>- Documentation updated (if needed) |

### Build and deployment
  #### Continuous Integration
      Link to CI: https://github.com/AnkiGen/anki_deck/blob/master/.github/workflows/main.yml
      List of tools:
        - ubuntu
        - unittest
        - pytest
      CI workflows runs: https://github.com/AnkiGen/anki_deck/blob/backend/test_results.txt
### How to launch using docker
```
Step 1. Install docker desktop on your computer
Step 2. open terminal from directory
Step 3. create .env with OPENAI_API_KEY=TOKEN and replace TOKEN with your GPT token 
Step 4. in terminal run command: "docker pull dkddjdjjfjdj/anki-deck"
Step 5. then in terminal run command: "docker run --env-file .env -p 8000:8000 dkddjdjjfjdj/anki-deck"
Link to the Docker Hub: "https://hub.docker.com/repository/docker/dkddjdjjfjdj/anki-deck/general"
```

### Git workflow
In our project we adapted base GitHub flow
1. Creating issues: we use several templates for the issues (https://github.com/AnkiGen/anki_deck/tree/templates/.github/ISSUE_TEMPLATE). The most commonly used are User Story, Issue and Bug report
2. Rules for creating issues: every change starts with an issue and must include: Priority (P0-P3), Estimation (Story Points), Milestone
3. Labelling Issues
- type: bug|feature|chore
- priority: P0-P3
3. Branching strategy
- naming convention
- creation
4. Commit messages
- format: use conventional commits
5. Pull requests
- Use PR Template
6. Code Reviews
- reviewers: assign 1-2 team members (not the author)
- feedback rules: be specific
7. Merging PRs
- who merges: author (after approval) or maintainer
- post-merge: delete the branch, update the issue status (e.g., "Done" in "somewhere")
8. Resolving Issues
- rlosed automatically when PR is merged (via Closes #123)
- reopen if bugs are found post-merge
### Git workflow using Gitgraph diagram
https://www.mermaidchart.com/app/projects/87fa344a-ba3a-4698-a8cc-fff8011d213c/diagrams/9806633b-e6e0-429a-8bf9-b6178f25629b/share/invite/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2N1bWVudElEIjoiOTgwNjYzM2ItZTZlMC00MjlhLThiZjktYjYxNzhmMjU2MjliIiwiYWNjZXNzIjoiVmlldyIsImlhdCI6MTc1MTgyNDIwMH0.wM7NipYQXLnSQ5szhIhBoJoWnuNj3Jegsmq-2Jji6bw
### Secrets management
To protect sensitive data (API keys, passwords, tokens), we follow:
1. Storage
- Environment Variables: Stored in GitHub Secrets (for CI/CD).
- Local Development: Use .env files (added to .gitignore).
- Production: Managed via AWS Parameter Store (or equivalent).
2. Rules
- Never Commit Secrets: Scan commits with git-secrets or truffleHog. Use placeholders (e.g., API_KEY=your_key_here in docs).
- Rotation: Secrets are rotated quarterly or after team changes.
- Access Control: Only maintainers and CI/CD systems have access.
