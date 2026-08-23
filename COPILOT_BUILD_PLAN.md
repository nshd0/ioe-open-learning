# IOE Open Learning — GitHub Copilot Build and Release Plan

## How to use this document

Open the `ioe-open-learning` repository in VS Code. Save this file in the repository root as `COPILOT_BUILD_PLAN.md`. Open **GitHub Copilot Chat** in Agent/Edit mode, then paste the prompt for the release you want to build.

**Important operating rule:** Ask Copilot to show the planned file changes first. Review the diff. Only then allow it to create or modify files. Run the validation checklist before committing and publishing.

---

# 1. Product Vision

Build **IOE Open Learning**, a free, public, mobile-first open learning portal for students, teachers, parents, and schools.

The first learning pathway is **Computational Thinking (CT) and Artificial Intelligence (AI) for Grades 3–8**. The portal should provide tangible, experiential, project-based learning—students should make, test, explain, improve, and share artifacts instead of only reading content.

The platform must be:

- Free to access publicly through GitHub Pages.
- Static-first: HTML, CSS, JavaScript, Markdown, downloadable files, and standalone H5P activities.
- Mobile-first and low-bandwidth conscious.
- Accessible: semantic HTML, keyboard navigation, visible focus states, sufficient colour contrast, image alt text, and reduced-motion support.
- Curriculum-aware: aligned in intent with NEP 2020, NCF-SE 2023, and the official CBSE Computational Thinking and AI curriculum for Grades 3–8.
- Safe: no student accounts, tracking, analytics, API keys, passwords, or collection of personal data in public releases.
- Reusable: content should be easy to adapt into H5P, Kolibri, Moodle, PDF, Google Docs, and teacher worksheets.

## Core Learning Promise

> Learn to think. Build to help.

Each learning experience should help a learner:

1. Notice or define a meaningful problem.
2. Break it into manageable parts.
3. Find patterns and relevant information.
4. Design a clear sequence, model, algorithm, or prototype.
5. Test the idea with a peer or a real example.
6. Improve it using evidence and feedback.
7. Consider fairness, safety, accuracy, privacy, and impact where AI is involved.

---

# 2. Technology Constraints

## Required stack

- Plain HTML5.
- Plain CSS3.
- Vanilla JavaScript only.
- GitHub Pages deployment from the `main` branch and repository root.
- No build step for Release 0.1.
- No framework dependency, package manager, server-side code, database, authentication, analytics, or paid service.

## Preferred future tools

- Lumi Desktop for authoring H5P activities.
- Standalone HTML exports of H5P activities stored in `assets/h5p/`.
- Markdown as the long-term source format for teacher material and curriculum documentation.
- GitHub Actions later for validation and deployment automation.

## Do not use

- React, Next.js, Vue, Tailwind CDN, Bootstrap CDN, jQuery, or external libraries unless explicitly approved in a future issue.
- Remote fonts; use a robust system font stack.
- External images that may break or introduce licensing concerns.
- Non-functional buttons or links.
- Placeholder text such as Lorem Ipsum.
- Claims of official endorsement by CBSE, NCERT, NEP, NCF, or any government body.

---

# 3. Information Architecture

```text
ioe-open-learning/
├── index.html
├── 404.html
├── README.md
├── LICENSE
├── COPILOT_BUILD_PLAN.md
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   │   ├── icons/
│   │   ├── grades/
│   │   └── projects/
│   └── h5p/
│       ├── grade-3/
│       ├── grade-4/
│       ├── grade-5/
│       ├── grade-6/
│       ├── grade-7/
│       └── grade-8/
├── grades/
│   ├── grade-3/
│   │   ├── index.html
│   │   └── lessons/
│   ├── grade-4/
│   │   ├── index.html
│   │   └── lessons/
│   ├── grade-5/
│   │   ├── index.html
│   │   └── lessons/
│   ├── grade-6/
│   │   ├── index.html
│   │   └── lessons/
│   ├── grade-7/
│   │   ├── index.html
│   │   └── lessons/
│   └── grade-8/
│       ├── index.html
│       └── lessons/
├── curriculum/
│   ├── master-ct-ai-grades-3-8.md
│   ├── alignment-notes.md
│   ├── grade-3.md
│   ├── grade-4.md
│   ├── grade-5.md
│   ├── grade-6.md
│   ├── grade-7.md
│   └── grade-8.md
├── teacher-toolkit/
│   ├── index.html
│   ├── unplugged-activities.md
│   ├── assessment-rubrics.md
│   ├── safeguarding-and-ai-use.md
│   └── project-guides/
├── downloads/
│   ├── activity-sheets/
│   └── project-templates/
└── .github/
    └── workflows/
        └── pages.yml
```

---

# 4. Shared Design System

## Brand tone

Use a warm, optimistic, confident education tone. The portal should feel credible to teachers and exciting to students. Avoid a corporate EdTech appearance and avoid a childish design for older grades.

## Shared colours

- Ink/navy: `#14213D`
- Deep indigo: `#312E81`
- Sky: `#38BDF8`
- Teal: `#14B8A6`
- Mango: `#FBBF24`
- Coral: `#FB7185`
- Cream: `#FFF9ED`
- Paper: `#FFFFFF`
- Slate body text: `#334155`

## Shared components

- Skip-to-content link.
- Sticky header with wordmark and a Home link.
- Mobile navigation that does not require JavaScript to access essential links.
- Breadcrumbs on all grade and lesson pages.
- Hero section.
- Unit cards.
- “You will make” artifact card.
- Learning goals list.
- Reflection prompt box.
- Honest release-status banner.
- Footer with CC BY-NC-SA 4.0 notice and GitHub repository link.

## Accessibility standards

- Use one `<h1>` per page and sensible nested heading structure.
- Use `<main>`, `<nav>`, `<header>`, `<footer>`, `<section>`, and `<article>` landmarks.
- Buttons need visible focus styles and accessible names.
- Use descriptive links, not “click here.”
- Images need concise, useful `alt` text; decorative images use empty `alt`.
- Honour `prefers-reduced-motion: reduce`.
- Avoid colour-only meaning.
- Test at 320px width and keyboard-only navigation.

---

# 5. Grade-Specific Experience Design

## Grade 3 — Playful Explorer

**Audience:** 8–9 years  
**Theme:** Sunny yellow, coral, rounded shapes, trails, arrow cards, friendly robot-grid mission  
**Learning mode:** Storytelling, movement, pair work, cards, drawing  
**Core concepts:** Patterns, sequence, clear instructions, debugging  
**Tangible artifact:** Paper Robot Grid Navigator

### Unit sequence

1. Pattern Detectives
2. Step-by-Step Stories
3. Robot Directions
4. Bug Hunt

## Grade 4 — Maker Studio

**Audience:** 9–10 years  
**Theme:** Orange, teal, construction tiles, puzzle pieces, making and testing  
**Learning mode:** Build, sort, repeat, peer test  
**Core concepts:** Decomposition, repetition, sorting, instructions  
**Tangible artifact:** Repeat-Art Generator or Algorithm Board Game

### Unit sequence

1. Puzzle Masters
2. Loop the Loop
3. Sort It Out
4. Make and Test

## Grade 5 — Map Lab

**Audience:** 10–11 years  
**Theme:** Leaf green, sky blue, routes, signposts, decision cards  
**Learning mode:** Explore, choose, map, debug  
**Core concepts:** Abstraction, conditionals, inputs, outputs, decisions  
**Tangible artifact:** Smart Classroom Decision Board

### Unit sequence

1. Map Makers
2. Choice Machines
3. Inputs and Outputs
4. Decision Debuggers

## Grade 6 — Logic Lab

**Audience:** 11–12 years  
**Theme:** Indigo, cyan, flowchart nodes, systems, block-code motifs  
**Learning mode:** Model, sequence, test, revise  
**Core concepts:** CT pillars, algorithms, flowcharts, debugging, AI vs automation  
**Tangible artifact:** Scratch Interactive Quiz or Story

### Unit sequence

1. Computational Thinking in Action
2. Flowchart Builders
3. Debugging Lab
4. Hello AI

## Grade 7 — Data Studio

**Audience:** 12–13 years  
**Theme:** Violet, turquoise, charts, label cards, language and classifier visuals  
**Learning mode:** Collect, classify, compare, question  
**Core concepts:** Data literacy, visualisation, NLP, training/testing, bias  
**Tangible artifact:** Classroom Data Story or Classifier Prototype

### Unit sequence

1. Data Detectives
2. Data Stories
3. Language and Machines
4. Fair or Flawed?

## Grade 8 — AI Futures

**Audience:** 13–14 years  
**Theme:** Navy, electric blue, aurora gradients, prototype cards, ethics shields  
**Learning mode:** Investigate, prototype, audit, present  
**Core concepts:** System decomposition, data quality, machine learning, generative AI, prompts, verification, privacy, fairness, safety, accountability  
**Tangible artifact:** AI for a Better School Capstone

### Unit sequence

1. Systems Thinkers
2. Data and Machine Learning
3. Generative AI with Judgement
4. Responsible AI
5. AI for a Better School

---

# 6. Releases and Copilot Prompts

## Release 0.1 — Public Portal Foundation

### Goal

Create a complete, functional, responsive static portal with grade navigation and grade-specific preview hubs. Do not claim full lessons exist yet.

### Files to create or update

```text
index.html
404.html
README.md
LICENSE
COPILOT_BUILD_PLAN.md
assets/css/style.css
assets/js/main.js
grades/grade-3/index.html
grades/grade-4/index.html
grades/grade-5/index.html
grades/grade-6/index.html
grades/grade-7/index.html
grades/grade-8/index.html
```

### Required homepage content

- Title: “IOE Open Learning”.
- Hero heading: “Learn to think. Build to help.”
- A concise explanation of free, project-based CT and AI learning for Grades 3–8.
- Three value cards: Think Clearly, Make Something Real, Use AI Responsibly.
- Preparatory Stage: Grades 3–5; unplugged, activity-first CT.
- Middle Stage: Grades 6–8; CT, data, AI concepts, responsible use, and projects.
- Six grade cards linking to the relevant relative URL.
- A release note clearly stating that full lessons, interactive H5P activities, printable sheets, and teacher materials are coming in later releases.

### Required grade-hub content

Each hub must include:

- Unique grade theme class on the `<body>` or main wrapper.
- Breadcrumb: Home → Grade X.
- Hero title and student-friendly promise.
- “You will explore” section with four to five learning ideas.
- “You will make” artifact section including purpose, materials, and how to share/test it.
- Four or five unit-preview cards.
- “Coming next” banner.
- Return to all grades link.

### Copilot prompt: Release 0.1

```text
You are working in the ioe-open-learning repository. Build Release 0.1 exactly according to COPILOT_BUILD_PLAN.md.

First, inspect the repository and show a concise file-change plan. Then create or update the Release 0.1 files only:
- index.html
- 404.html
- README.md
- LICENSE
- assets/css/style.css
- assets/js/main.js
- grades/grade-3/index.html through grades/grade-8/index.html

Use only semantic HTML, one shared CSS file, and one small vanilla JavaScript file. Do not use frameworks, CDNs, remote fonts, build tooling, tracking, analytics, APIs, student accounts, placeholders, or dead links.

Make all relative paths correct from every grade page. Use a shared design system and give every grade a visibly distinct theme as described in this plan. Keep the site responsive and accessible, including a skip link, keyboard-visible focus states, good contrast, and reduced-motion support.

Put real student-facing content on every page. Label the site clearly as Release 0.1 and state that full lessons and activities arrive in later releases.

After editing, run or simulate link/path checks, inspect for broken relative paths, and provide a concise summary of every changed file. Do not commit until I explicitly ask.
```

### Release 0.1 acceptance checklist

- [ ] Home page links to all six grade hubs.
- [ ] All grade hubs link back to home.
- [ ] CSS renders correctly from nested grade directories.
- [ ] Grade themes are visually differentiated while navigation remains consistent.
- [ ] Site works at 320px wide and on desktop.
- [ ] Keyboard focus is visible.
- [ ] No network dependency or personal-data collection is introduced.
- [ ] Every label and button has a purpose.
- [ ] README gives exact GitHub Pages deployment instructions.

---

# (Remaining plan omitted here for brevity)
