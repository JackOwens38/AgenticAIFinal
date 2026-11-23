# CLAUDE.md — Raclin Murphy Museum Guide

## Project overview

This repository contains a Retrieval-Augmented Generation (RAG) museum guide chatbot for the **Raclin Murphy Museum of Art at the University of Notre Dame**. The guide is intended to answer visitor questions about the museum's collection, exhibitions, and finding locations inside the museum.

The goal is to provide **accurate, clear, useful, and source-grounded** answers. If the available museum materials do not support an answer, say what cannot be verified rather than guessing.

## Repository organization

- `code/` — Museum guide implementation, including the RAG system. Sprint Packet #3 reports a second version of the RAG model.
- `data/` — Museum information used by the guide, including exhibition and wayfinding data. Confirm the current file names and formats before modifying them.
- `tests/` — Test questions, evaluations, and related results. Consult existing files before adding cases or modifying the scoring process.
- `Sprint Packets/` — Team progress reports and sprint documentation.
- `README.md` — Human-facing project overview and instructions.

**Important:** The exact run command, model names, file paths, and dependency installation steps have not been verified in this document. Inspect the repository's current code and README before proposing commands or changes. Do not invent them.

## Current status (reported in Sprint Packet #3, November 2026)

- An initial RAG system and a second RAG version have been developed.
- The museum dataset and question evaluations have been updated through multiple rounds.
- The team reports using an LLM-as-a-judge evaluation approach.
- Sprint Packet #3 reports 30 questions evaluated for the updated system and a 90% score. These are *reported results*, not independently verified measurements here.
- The packet identifies remaining weaknesses involving artwork color questions, image caption or donor credit information, and exhibition-related question interpretation.

Do not claim that an improvement was implemented or improved accuracy unless a code change and before/after evaluation support that claim.

## Source and answer rules

1. Prefer official Raclin Murphy Museum information and other sources explicitly vetted by the team.
2. Ground factual claims in retrieved information. Do not invent artist names, artwork attributes, gallery locations, exhibition details, donors, or dates.
3. Distinguish a missing record from a confirmed negative answer. If a record lacks information, say that the available records do not establish the answer.
4. Treat temporary exhibitions and navigation information as potentially time-sensitive. Check available dates and location information rather than assuming they remain current.
5. Keep answers understandable to visitors without specialized art or technical knowledge.
6. Do not use unverified visual details to describe artwork colors or other image-dependent features.
7. If a visitor request goes beyond the museum records or the guide's capabilities, state the limitation and suggest a reasonable way to verify the information.

## Visitor privacy and responsible use

The team established these rules in Sprint Packet #2:

- Do not collect personal visitor information without clear consent.
- Do not permanently store visitor conversations without consent.
- Do not present unverified artwork information as fact.
- Do not require personal visitor information to give general exhibit suggestions; use voluntarily shared interests for personalization.
- Do not share visitor data with third parties without appropriate notice, authorization, and consent.

These are **project requirements**; do not assume every rule is already enforced in code. Include appropriate negative and decline-or-flag test cases.

## Evaluation guidelines

- Use the project's existing test questions and evaluation files. Avoid silently changing their identifiers or scoring rubric.
- Evaluate the baseline and updated guide on the **same test set** and **same grading criteria** for a fair comparison.
- Maintain tests for ordinary collection questions, exhibit details, wayfinding, ambiguous questions, unverified information, and privacy-related requests.
- Preserve generated responses and evaluation evidence in version-controlled results files where practical, without committing sensitive data.
- Keep human grades separate from automatic judge grades until the independent human review is complete.
- Document failures with the question, response, expected behavior, likely cause (clearly labeled if unverified), and a proposed correction.
- For each iteration, note what changed, why it changed, the test set used, scores before and after, and whether the change was kept.

## Known failure cases from Sprint Packet #3

### Artwork color description

For *Spring* by Natalia Goncharova, the guide could not verify artwork colors from the available written collection record. Investigate whether verified visual descriptions exist. Do not fabricate colors.

### Caption or credit-line retrieval

A question about the Bernard and Mary T. Norling Endowment for 18th- and 19th-Century Sculpture was not answered because the relevant caption or credit-line information was not retrieved. Check whether important captions and credit lines were omitted from the available dataset.

### Exhibition question interpretation

For *Mimmo Paladino: Present into Past*, the guide gave an incomplete response to a question about the exhibition. Test alternative phrasings and inspect whether the retrieved source actually contains the requested information.

## Guidance for contributors and AI coding assistants

- Read `README.md`, relevant code, and existing tests before making edits.
- Make small, reviewable changes and describe each change in the commit message or pull request.
- Do not replace existing datasets or test files without checking for current team changes.
- Do not invent measured results, source citations, model settings, or successful tests.
- Never commit API keys, credentials, private visitor information, or restricted material. Use environment variables and `.gitignore` for secrets.
- Preserve source attribution where feasible and respect data access and copyright restrictions.
- Ask for team review when changing the core RAG implementation, evaluation rubric, or source collection process.

## Before the final submission

Verify that the README explains how to run the current system and evaluation, that test results and human grades are saved, that iteration history is documented, and that the team has reviewed the accuracy and privacy requirements. Update this file whenever the architecture or evaluation process materially changes.
