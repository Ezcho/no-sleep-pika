Source: https://no-sleep-pika.online/guide/parallel-ai-agents-git-worktree/
Language: en

MAC GUIDE · 2026-11-24

# Two AI agents editing the same files? Give them separate folders.

Git worktree gives each AI agent its own working folder. Here is how to separate tasks, review changes, and bring them together without mixing unfinished work.

## One folder, two agents: where edits collide

One agent updates the interface while another writes tests. If both use the same folder, they see and can change the same files. Creating two branch names does not give that one folder two independent sets of files. Switching branches there also changes the files the other agent is using.

A Git worktree is another working folder attached to the same repository. Each folder can have its own branch and checked-out files, while sharing repository history. It separates work in progress; it does not prevent two agents from eventually proposing conflicting changes.

- 1 Separate folders

- 2 Assign tasks

- 3 Review changes

- 4 Integrate one at a time

## Start with a reviewed baseline

Run the command below in your existing Git project. This example requires at least one commit, so HEAD points to a committed baseline. An empty status output means Git reports no tracked changes or untracked files; ignored files may still be present.

If anything is listed, review it first. Save only the intended, reviewed changes in a commit, or choose an already committed baseline. Do not blindly stage the entire folder: credentials and unrelated work must stay out. The new folders start from HEAD, not from your uncommitted edits.

```
git status --short
```

## Create two working folders

The commands below create ai-ui and ai-tests branches, with working folders beside your current project. Run both from the original project. Use branch names and destination paths that do not already exist; if they are taken, choose different names rather than forcing an overwrite.

These folders share Git history, but they do not automatically copy installed dependencies, ignored .env files, or every local setting. Install dependencies as required by the project. Supply only the credentials each task needs, and use different ports if both tasks start development servers. Worktrees are not security sandboxes: tools may still access other folders if their permissions allow it.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Give each agent a folder and a clear task

Open one agent in project-ai-ui and the other in project-ai-tests. Give each its exact absolute folder path and a narrow task: for example, “Edit only the interface component” and “Add tests for existing behavior; do not change application code.”

Name shared files that require coordination, such as dependency manifests and lockfiles. If both tasks need the same file, handle them in sequence or agree on which agent owns it. Ask each agent to report changed files, checks performed, and unfinished work before you accept its result.

## Review before bringing work together

In each working folder, run the three commands below. Status lists changed and untracked files. The first diff shows unstaged tracked edits; the cached diff shows staged edits. New untracked files do not appear in these diffs: open and review them separately.

Run the project's relevant checks, review the result, and commit the intended changes on that folder's branch. Then return to the original project and review and integrate one branch at a time into your intended destination branch. Worktrees never merge the results automatically. If changes overlap, resolve the conflict and check the combined result before adding the next branch.

```
git status --short
git diff
git diff --cached
```

## Where pika fits

pika can help keep your Mac awake while local agents work, subject to its session settings and safety protections. It does not assign tasks, merge branches, or resolve conflicts. In pika 1.3, QR access shows Mac status and approved power controls, not AI output or a reliable AI completion percentage. Use each agent's own output and your project checks to judge whether the work is done.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Installation help](https://no-sleep-pika.online/install/)

Sources and scope

This guide is written by the maker of no-sleep-pika. The workflow follows Git's official documentation and uses generic AI agents; it does not assume a particular agent's permissions or features. Follow your project's contribution and secret-handling rules as well.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Written by the maker of no-sleep-pika; this comparison includes our own app.

[How to keep your Mac awake: clamshell mode, caffeinate and pika →](https://no-sleep-pika.online/guide/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/parallel-ai-agents-git-worktree/index.md)
