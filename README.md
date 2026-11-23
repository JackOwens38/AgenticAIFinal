# AgenticAIFinal

## Project Description
Repository for the Agentic AI Final Project: a Retrieval-Augmented Generation (RAG) **Museum Guide** chatbot for the [Raclin Murphy Museum of Art](https://raclinmurphymuseum.nd.edu/) at the University of Notre Dame. The assistant answers visitor questions about the collection, current and past exhibitions, and wayfinding ("Where is the chapel?", "How do I get to Studio B from the main lobby?").

## Team Members
- Jack Owens
- Passion Hood
- Luke Collins

## How It Works
Museum content was scraped from the Raclin Murphy site and the Marble collection platform (`marble.nd.edu`), cleaned and de-duplicated (one row per artwork/exhibit, keyed on accession number), and stored as a multi-tab Excel workbook. The RAG notebook loads those tabs into a Chroma vector store (OpenAI `text-embedding-3-small` embeddings) and answers questions with a `ChatOpenAI` generator. A second notebook adds an **LLM-as-judge** evaluation that scores answers against reference answers on an anchored rubric.

## Repository Structure

### `code/`
- **`Museum_Guide_RAG_v2_with_judge.ipynb`** — Current RAG pipeline. Generator model `gpt-5.4-mini`, retrieval `k=6`, loads all 6 data tabs. Includes the LLM-as-judge evaluation (anchored rubric: fluency / correctness / completeness / groundedness, scored 1–5) over a 30-question test set.
- **`Museum_Guide_RAG_Starter (1).ipynb`** — Original starter RAG notebook (`gpt-4o-mini`), kept for reference and baseline comparison.
- **`add_image_captions.py`** — Vision pipeline that fills the Artworks "Visual Description" column by sending each artwork image to a vision model. Run this in Colab (where the museum image URLs are reachable) to give the text-only RAG basic "sight" of color and appearance.
- **`chatbotassistant.py`** — Chatbot assistant helper code.

### `data/`
- **`Raclin_Murphy_Museum_Galleries_Dataset.xlsx`** — The core knowledge base the RAG loads. Seven tabs:

  | Tab | Rows* | Contents |
  |-----|------|----------|
  | Galleries | 13 | Gallery/space names and descriptions |
  | Themes (Marble portfolios) | 28 | Marble collection themes |
  | Artworks | 323 | Per-artwork: accession, title, creator, date, medium, dimensions, credit line, location, description, visual description, image URL |
  | Exhibitions | 122 | Current, upcoming, and past exhibitions with dates |
  | Floor Plan Directory | 33 | Rooms/destinations mapped to levels |
  | Wayfinding | 400 | Natural-language routes, locations, and adjacencies for navigation questions |
  | README — method & notes | — | In-workbook documentation of sources and method |

  \*Includes header/banner rows; data starts at row 4 (read with `header=3` in pandas).
- **`Museum_Guide_Question_Tests_RAG2.xlsx`** — Evaluation sheet. Three tabs: `GPT 4o-mini` and `Initial RAG` (baseline question/answer tests), and `RAG Tests 2` (30 questions with v2 answers, reference answers, the LLM-as-judge pass/fail verdict, and the four sub-scores).
- **`exhibitions.md`** — Human-readable exhibitions reference.
- **`floorplan_wayfinding.md`** / **`floor_plan_model.json`** — Human-readable and structured floor-plan / wayfinding model.
- **`GPT Question Tests*.xlsx`** — Earlier two-tab test sheets (superseded by `Museum_Guide_Question_Tests_RAG2.xlsx`).

### `tests/`
Test notebooks and earlier question sheets used while developing and validating the RAG.

### `Sprint Packets/`
Course sprint deliverables (`AAI Sprint Packet 1`, `AAI Sprint Packet 2`; Sprint Packet 3 to be added).

## Current Evaluation Results (RAG v2 + LLM-as-judge)
- **27 / 30** questions passed (correctness ≥ 4 on the anchored rubric)
- Mean correctness **4.63 / 5**
- Remaining misses: a Goncharova *Spring* color question (addressed by running `add_image_captions.py`), a Norling endowment detail, and a Mimmo Paladino dimension not yet in the dataset.

## Running the Pipeline
1. Open `code/Museum_Guide_RAG_v2_with_judge.ipynb` (Colab recommended).
2. Set your `OPENAI_API_KEY`.
3. Ensure `data/Raclin_Murphy_Museum_Galleries_Dataset.xlsx` is available to the notebook (same filename the `SHEETS` config expects).
4. Run all cells to build the vector store, answer the test questions, and run the LLM-as-judge evaluation.
5. (Optional) Run `code/add_image_captions.py` first to populate visual descriptions, then rebuild.
