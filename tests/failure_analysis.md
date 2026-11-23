# Museum Guide AI — Failure Analysis

**Project:** Raclin Murphy Museum of Art AI Museum Guide  
**Prepared by:** Passion Hood  
**Source:** Team's submitted Sprint Packet #3 (November 2026)  
**Status:** Review and proposed follow-up tests; not a record of completed fixes

## Purpose

This document summarizes three failure types observed during the team's evaluation of the Museum Guide AI and recommends ways to test and improve the system. The submitted Sprint Packet #3 reports **30 system test cases**, a **90% automatic-judge score**, and **three failures**. These figures are reported from the packet, not independently reproduced here.

## 1. Unable to answer visual questions about artwork

**Example:** *Spring* by Natalia Goncharova (collection record `1994.027.007`).

**Observed behavior:** The agent explained that the available collection record did not specify the exact colors used in the artwork and therefore could not confirm its palette.

**Why it matters:** Museum visitors may ask about visual details that are not captured in text-only collection records. Not inventing colors is a responsible response, but it also reveals a limitation in the information available to the guide.

**Possible cause to investigate:** The retrieved source material lacks a verified visual description; the packet does not establish whether image understanding was available.

**Recommended improvement:** Check whether the museum offers an authorized image or verified visual description. If that information is unavailable, keep the agent's uncertainty rather than guessing.

**Proposed follow-up test:** Ask, "What colors appear in *Spring* by Natalia Goncharova?" Verify whether the agent uses an approved visual source or clearly states that the available records do not establish the colors.

## 2. Missing information contained in artwork captions

**Example:** Bernard Norling and Mary T. Norling Endowment for 18th- and 19th-Century Sculpture.

**Observed behavior:** The agent could not confirm the endowment's relationship to works in the collection, although the team's packet states that the relevant information appeared in an image caption not captured in the dataset.

**Why it matters:** If captions and credit lines are omitted during data collection, the guide may fail to answer questions about donors, artwork provenance, and collection information even when the museum publishes that information.

**Possible cause to investigate:** Data extraction did not preserve all caption or credit-line text.

**Recommended improvement:** Review the source page and, where permitted, include verified caption text and credit-line fields in the dataset. Preserve source links and artwork identifiers so the information can be traced back to museum records.

**Proposed follow-up test:** Ask a question about the Norling endowment using the exact wording of the verified caption. Check whether the relevant record is retrieved and whether the answer cites the correct source.

## 3. Misunderstood exhibition question

**Example:** *Mimmo Paladino: Present into Past*.

**Observed behavior:** In the example recorded in Sprint Packet #3, the agent replied with an exhibition location and dates, but said it could not confirm the size or number of works. The team categorized this as misunderstanding the question.

**Why it matters:** A response can mention the correct exhibition while still failing to answer what the visitor actually asked.

**Possible causes to investigate:** The source materials may lack the requested detail, the retrieval step may have missed it, or the language model may have misinterpreted the question. The packet does not establish which caused the error.

**Recommended improvement:** Test several paraphrases of the original question. Compare the retrieved passages with the source museum page before deciding whether to improve the data, retrieval process, or response instructions.

**Proposed follow-up test:** Ask the same fact-seeking question using several phrasings. Check whether the agent answers the requested fact when a verified source contains it, and declines to invent an answer otherwise.

## Summary of findings

| Failure type | Count reported in Sprint Packet #3 | Recommended action |
| --- | ---: | --- |
| Artwork visual information unavailable | 1 | Check approved visual descriptions; retain uncertainty where needed |
| Relevant caption data missing | 1 | Verify and capture permitted caption/credit-line information |
| Exhibition question misunderstood | 1 | Test paraphrases and inspect retrieval results |

## Proposed next steps

1. Locate the original question and test-case ID for each failure in the team's saved evaluation results.
2. Confirm the museum source record for each example and document its URL or identifier.
3. Add the three follow-up tests to the existing test set without duplicating questions.
4. Coordinate with the person updating the RAG pipeline before making changes to source data or retrieval logic.
5. Rerun the same questions after a specific change and record the before-and-after results in the lab notebook.
6. Keep automatic and human evaluations comparable by using the same questions and rubric.

## Important distinction

This document records **analysis and proposed improvements only**. It does **not** claim that the suggested fixes have been implemented, that the new tests have been run, or that scores have improved. Those outcomes must be recorded after the team performs and verifies the next evaluation.
