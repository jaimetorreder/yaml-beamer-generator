# YAML Schema for Beamer Presentations

## Overview
This schema defines the structure for YAML lesson plans that can be converted to Beamer LaTeX presentations.

## Root Structure

```yaml
title: string          # Presentation title
author: string         # Author name (optional)
date: string          # Date (optional)
slides: array         # Array of slide objects
```

## Slide Types

### 1. Do Now Slide (`do_now`)

A slide with numbered questions for students to work on at the start of class.

```yaml
- type: do_now
  title: string       # Slide title (default: "Do Now")
  questions: array    # Array of question objects (typically 4 questions)
```

**Question Object:**
```yaml
- question: string    # The question text (supports LaTeX math)
  answer: string      # The answer (optional, for answer slide)
```

**Behavior:**
- Generates TWO slides: one with questions only, one with questions and answers
- Questions are automatically numbered
- Recommended: 4 questions per Do Now
- LaTeX math must be wrapped in `$...$` for inline or `$$...$$` for display

### 2. Diagnostic Question Slide (`diagnostic_question`)

A multiple-choice question slide for formative assessment with animated answer reveal.

```yaml
- type: diagnostic_question
  title: string          # Slide title
  question: string       # The question text (supports LaTeX math)
  options: array         # Array of answer options
  correct: integer       # Index of correct answer (0-based)
  explanation: string    # Optional explanation (appears with answer)
```

**Features:**
- Array of strings representing answer choices
- Automatically labeled A, B, C, D, etc.
- **Animation**: First overlay shows question and options only
- **Animation**: Second overlay reveals the correct answer with green checkmark
- Optional explanation appears on second overlay (supports LaTeX math)

## Complete Example

```yaml
title: "Linear Functions Review"
author: "Math Teacher"
date: "2025-10-22"
slides:
  - type: do_now
    title: "Do Now"
    questions:
      - question: "Solve: $2x + 5 = 13$"
        answer: "$x = 4$"
      - question: "What is the slope of $y = 3x - 2$?"
        answer: "$m = 3$"
      - question: "Find the y-intercept of $y = 2x - 7$"
        answer: "$b = -7$"
      - question: "Evaluate $3x + 2$ when $x = 5$"
        answer: "$17$"

  - type: diagnostic_question
    title: "Diagnostic: Slope"
    question: "What is the slope of a horizontal line?"
    options:
      - "0"
      - "1"
      - "Undefined"
      - "Negative"
    correct: 0
    explanation: "Horizontal lines have no vertical change, so slope $m = 0$."
```

## Notes

- All text fields support LaTeX math notation
- Use `$...$` for inline math: `$x^2 + y^2 = r^2$`
- Use `$$...$$` for display math (will be converted appropriately)
- Special characters should be LaTeX-escaped where necessary
