# Rule: Mandatory Skill & MCP Tool Discovery ("Find the Right Tool First")

## Principle
Never reinvent the wheel or rely solely on baseline model weights when specialized Skills or MCP Tools exist in the environment. All user requests MUST undergo a mandatory skill-matching check before execution begins.

---

## Pre-Execution Workflow (Mandatory for Every Request)

### Step 1: Scan Available Skills & MCP Tools
Before generating code, planning, or running commands, scan the `<skills>` catalog in your system prompt and all available MCP tools against the user's prompt.

Perform domain matching:
- **UI / Frontend / Styling**: Check `modern-web-guidance`, `generative_ui`, `color-typography-design`, `a11y-debugging`, `chrome-devtools`, `chrome-extensions`.
- **Flutter / Dart / Mobile**: Check `flutter-*`, `dart-*`, `android-cli`.
- **Firebase & Cloud Databases**: Check `firebase-*`, `bigquery-*`, `dataform-*`, `dbt-*`, `gcp-*`, `discovering-gcp-data-assets`.
- **Data Science / ML / Analytics**: Check `ml-best-practices`, `notebook-guidance`, `bigquery-ai-ml`, `bigquery-bigframes`.
- **Performance & Debugging**: Check `debug-optimize-lcp`, `memory-leak-debugging`, `a11y-debugging`, `troubleshooting`.
- **Data Protection & Security**: Check `accidental-data-loss-prevention`, `gcs-security-assessment`, `firebase-security-rules-auditor`.
- **Life Sciences & Research**: Check `literature-search-*`, `pubchem-*`, `uniprot-*`, `pdb-*`, `chembl-*`, etc.

### Step 2: Unconditional Skill Activation
If ONE or MORE skills match the domain or task:
1. **Load Skill Instructions**: Immediately execute `view_file` on the `SKILL.md` path for each matching skill (or delegate to a subagent that follows the skill).
2. **Obey Workflow**: Follow the guidelines, required tools, and checklists specified in the activated `SKILL.md` files.

### Step 3: Transparent Tool Attribution
In the initial response or plan provided to the user, state clearly:
> *"Activated Skills & MCP Tools for this task: [Skill Name 1], [Skill Name 2], [MCP Server/Tool Name]"*
