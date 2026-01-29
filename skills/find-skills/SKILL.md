# Find Skills

This skill helps users discover and install skills from the open agent skills ecosystem. The "Find Skills" skill assists when users ask how to accomplish tasks or seek specialized capabilities.

## When to Use This Skill

Activate this skill when users:

- Ask "how do I do X" for potential existing skills
- Request "find a skill for X" or similar discovery queries
- Wonder if capabilities exist for specialized domains
- Seek to extend agent functionality
- Look for tools, templates, or workflows

## Skills CLI Fundamentals

The command-line interface (`npx skills`) functions as a package manager for agent skills—modular extensions providing specialized knowledge and workflows.

**Key Commands:**

- `npx skills find [query]` — Interactive or keyword-based searching
- `npx skills add <package>` — Install from GitHub or other sources
- `npx skills check` — Check for updates
- `npx skills update` — Refresh all installations

Browse options at: https://skills.sh/

## Four-Step Discovery Process

**Step 1: Identify Requirements**

Determine the domain, specific task, and whether a skill likely addresses it.

**Step 2: Execute Search**

Run `npx skills find [query]` with relevant terms. Results display install commands and skills.sh links.

**Step 3: Share Results**

Present skill names, descriptions, installation instructions, and documentation links clearly.

**Step 4: Enable Installation**

If interested, users run `npx skills add <owner/repo@skill> -g -y` (-g for global, -y for confirmation bypass).

## Common Categories

- **Web Development**: react, nextjs, typescript
- **Testing**: jest, playwright
- **DevOps**: docker, kubernetes
- **Documentation**: docs, changelog
- **Code Quality**: review, lint
- **Design**: ui, accessibility
- **Productivity**: workflow, automation

## Search Best Practices

- Use specific keywords over broad terms
- Try alternative terminology if initial searches fail
- Check established sources like `vercel-labs/agent-skills`

## No Results Protocol

When searches yield nothing:

1. Acknowledge the gap
2. Offer direct assistance
3. Suggest users create custom skills via `npx skills init`
