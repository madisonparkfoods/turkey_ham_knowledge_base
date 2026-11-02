# Publishing checklist

This covers what's still needed before submitting `madison-park-holiday-feast` to the Claude plugin directory and the OpenAI (ChatGPT/Codex) plugin directory. Requirements were checked on 2026-11-02 against the docs linked at the bottom. Re-check them before submitting.

The plugin folder is `plugins/madison-park-holiday-feast/`. Both directories read the plugin's manifest, README and LICENSE from there.

## Already done

- [x] **License.** Proprietary, free to use: [`LICENSE`](LICENSE), with a copy in the plugin folder. `license` is set in both manifests, and every single-skill zip includes the license. `build_dist.py` fails if the two copies differ.
- [x] **Distinctive name.** Renamed from the generic `holiday-feast` to `madison-park-holiday-feast`. The Claude directory holds names made only of generic words for a reviewer, and names can't be changed after publishing.
- [x] **Display name** `Madison Park Holiday Feast` in both manifests (26 of 30 characters allowed for OpenAI).
- [x] **OpenAI interface fields:**
  - `shortDescription` cut to 28 of 30 characters
  - `capabilities` (required) set to `[]`
  - `logo` and `composerIcon` added
  - `websiteURL` set to madisonparkfoods.com
  - `longDescription` states the limitations and the data behavior
- [x] **Brand color contrast.** `#B5562A` is 4.85:1 against white and 3.32:1 against `#212121`; OpenAI asks for at least 2:1 on each.
- [x] **README in the plugin folder.** The Claude listing description needs at least 40 words; this one has five example prompts plus sections on what the plugin does and doesn't do (no code, no data collection, the one optional web check), troubleshooting, support, privacy and license.
- [x] **Plugin folder contents:**
  - only text files and PNG images, with no binary files that would be held for review
  - about 190 files (the limit is 512), each well under 256 KiB
  - no hooks, MCP servers, `userConfig` or commands, so nothing has to be stripped for OpenAI's skills-only upload
- [x] **Claude-specific wording.** No skill text refers to Claude by name, so it works as written on OpenAI.
- [x] **Official artwork.** `assets/logo.png` (512×512) and `assets/composer-icon.png` (256×256) are the Madison Park Foods emblem, taken from the logo banner on madisonparkfoods.com (`wp-content/uploads/MPD-Logo-Slider-var2.jpg`, 1200×800) and centered on a square white canvas. For a sharper icon, replace them with higher-resolution art from the original design files. Keep them square, at least 48×48, PNG/JPEG/WebP/SVG and under 5 MiB.
- [x] **OpenAI upload archive.** `python3 scripts/build_dist.py` builds `dist/plugin/madison-park-holiday-feast.zip`.
- [x] **Local check.** `claude plugin validate .` and `claude plugin validate ./plugins/madison-park-holiday-feast` both pass.

## To do before submitting (you)

- [ ] **Support, privacy and terms URLs.** Replace each `TODO-replace-with-…` value in `plugins/madison-park-holiday-feast/.codex-plugin/plugin.json` (`supportURL`, `privacyPolicyURL`, `termsOfServiceURL`) and in the plugin README's "Support and privacy" section. Each must be an HTTPS link to a real page on madisonparkfoods.com or another site you control. The Anthropic Software Directory Policy also asks for a clear privacy policy link and verified support contact information. `build_dist.py` warns until every placeholder is gone.
- [ ] **Legal review of `LICENSE`.** I drafted it as a starting point, not legal advice. Check especially that section 2 still allows the directories to distribute the plugin.
- [x] **Promotional balance.** The Anthropic Software Directory Policy (section 4C) excludes software that "exists primarily as an advertising or promotional vehicle". On 2026-11-02 the knowledge base was trimmed back to product mentions that help the cook. Products appear only where a seasoning is used, with honest trade-offs in `16-madison-park-foods.md` and the `madison-park-pairing` skill. Keep it that way: cooking guidance first, products only where they help.
- [ ] **OpenAI category.** OpenAI doesn't publish its allowed `category` values. Confirm in the dashboard that `Lifestyle` exists, or pick the closest one.
- [ ] **Version.** Bump `version` in both plugin manifests and in `.claude-plugin/marketplace.json` for any change after the first submission.
- [ ] **Commit and push** to `madisonparkfoods/turkey_ham_knowledge_base`, with this folder as the repository root.
- [ ] **Existing installs.** Anyone who installed the old `holiday-feast` from this marketplace has to uninstall it and install `madison-park-holiday-feast@holiday-feast-marketplace`. Skill commands are now `/madison-park-holiday-feast:<skill>`.

## Submitting to the Claude plugin directory

1. In the developer portal at https://claude.ai/directory/manage, select **Submit new**, then **Plugin bundle**.
2. For **Source**, enter the GitHub repository with the plugin path `plugins/madison-park-holiday-feast`. The marketplace has only one plugin, but submit the plugin folder, not the repository root.
3. Select **Validate**. Fix every **Blocking** finding, push the fix, then select **Re-validate**.
4. Submit. The plugin goes through a security scan, and possibly a reviewer, before it lists. Agree to the Software Directory Terms when the portal asks.

## Submitting to the OpenAI plugin directory

1. The owning OpenAI organization needs verified individual or business identity. You need owner rights or **Apps Management** write access.
2. Run `python3 scripts/build_dist.py`, then go to https://platform.openai.com/plugins, choose **Create plugin**, then **Skills only**, and upload `dist/plugin/madison-park-holiday-feast.zip`.
3. Review the manifest that the portal generates (it fills in missing interface defaults), the listing fields and the country targeting. Then fix every scan result and complete the policy attestations.
4. Submit for OpenAI review. Skills-only plugins don't need test cases, a demo recording or reviewer credentials. Approval in the Claude directory doesn't carry over.

## Custom GPT (GPT Store)

This is a separate listing, set up as in [`custom-gpt/README.md`](custom-gpt/README.md). A GPT Store listing needs a verified builder profile. Add the privacy policy URL to the GPT's configuration once you have one.

## Sources

- Claude plugin pre-submission checklist: https://claude.com/docs/plugins/pre-submission-checklist
- Anthropic Software Directory Policy: https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
- OpenAI, submit a Claude plugin: https://developers.openai.com/plugins/guides/submit-claude-plugin
- OpenAI, plugin submission fields: https://developers.openai.com/plugins/deploy/submission
- OpenAI, plugin structure: https://developers.openai.com/plugins/build/plugins
