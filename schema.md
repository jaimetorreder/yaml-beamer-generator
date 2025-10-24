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

### 2. Learning Goals Slide (`learning_goals`)

A simple slide displaying the lesson's learning objectives.

```yaml
- type: learning_goals
  title: string       # Slide title (default: "Learning Goals")
  goals: array        # Array of learning goal strings (1-3 recommended)
```

**Features:**
- Large font for readability
- Bulleted list format
- Typically 1-3 learning objectives
- Supports LaTeX math notation in goal text

**Example:**
```yaml
- type: learning_goals
  title: "Today's Focus"
  goals:
    - "Find x- and y-intercepts algebraically and graph lines"
    - "Calculate slope from graphs, equations, or two points"
    - "Write equations of lines using point-slope and slope-intercept forms"
```

### 3. Diagnostic Question Slide (`diagnostic_question`)

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

  - type: learning_goals
    title: "Today's Focus"
    goals:
      - "Find x- and y-intercepts algebraically and graph lines"
      - "Calculate slope from graphs, equations, or two points"
      - "Write equations of lines using point-slope and slope-intercept forms"

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

### 4. New Atom: Fact Slide (`new_atom_fact`)

Introduces a new fact or property with multiple examples demonstrating it.

```yaml
- type: new_atom_fact
  title: string        # Slide title
  examples: array      # Array of example objects
```

**Example Object:**
```yaml
- statement: string   # The statement or expression
  result: string      # The result or evaluation
```

**Features:**
- Progressive reveal with `\pause` between examples
- Great for showing property evaluations or yes/no determinations
- Examples shown side-by-side with results

### 5. New Atom: Category Slide (`new_atom_category`)

Shows categorization or classification of concepts.

```yaml
- type: new_atom_category
  title: string        # Slide title
  categories: array    # Array of category objects
```

**Category Object:**
```yaml
- name: string         # Category name
  description: string  # Brief description
  examples: array      # Array of example strings (optional)
```

**Features:**
- Progressive reveal of each category
- Examples shown as bulleted lists
- Good for teaching types or classifications

### 6. New Atom: Transformation Slide (`new_atom_transformation`)

Shows step-by-step transformations from one form to another.

```yaml
- type: new_atom_transformation
  title: string             # Slide title
  transformations: array    # Array of transformation objects
```

**Transformation Object:**
```yaml
- from: string   # Starting expression
  to: string     # Resulting expression
```

**Features:**
- Shows transformation with arrow: `from → to`
- Progressive reveal with pause between each
- Ideal for showing algebraic manipulations or simplifications

### 7. I Do Slide (`i_do`)

Teacher-led worked example with detailed step-by-step solution.

```yaml
- type: i_do
  title: string     # Slide title (default: "I Do")
  problem: string   # The problem statement
  steps: array      # Array of step objects
  answer: string    # Final answer (optional)
```

**Step Object:**
```yaml
- label: string    # Step label (e.g., "Step 1: Isolate")
  content: string  # Step content/work
```

**Features:**
- Progressive reveal of each step
- Final answer displayed in large font
- Use `\\\\` for line breaks within step content

### 8. We Do Slide (`we_do`)

Guided practice problem for student participation.

```yaml
- type: we_do
  title: string     # Slide title (default: "We Do")
  problem: string   # The problem statement
  steps: array      # Array of step objects
  answer: string    # Final answer (optional)
```

**Note:** Currently implemented identically to `i_do` template. Future versions may differentiate for collaborative work.

### 9. Practice Slide (`practice`)

Multiple practice problems with progressive answer reveal.

```yaml
- type: practice
  title: string      # Slide title (default: "Practice")
  problems: array    # Array of problem objects
```

**Problem Object:**
```yaml
- question: string  # The problem/question
  answer: string    # The answer
```

**Features:**
- All problems shown initially
- Answers revealed progressively (overlay 2, 3, 4, ...)
- Good for independent practice with quick answer checking

### 10. Closure Slide (`closure`)

Summarizes what was learned in the lesson.

```yaml
- type: closure
  title: string    # Slide title (default: "Closure")
  topics: array    # Array of topic objects
```

**Topic Object:**
```yaml
- title: string   # Topic title
  points: array   # Array of bullet point strings
```

**Features:**
- Large "What We Learned Today" heading
- Multiple topics with bulleted key points
- Perfect for lesson wrap-up and review

## Notes

- All text fields support LaTeX math notation
- Use `$...$` for inline math: `$x^2 + y^2 = r^2$`
- Use `$$...$$` for display math (will be converted appropriately)
- Special characters should be LaTeX-escaped where necessary
- Use `\\\\` for line breaks within text content
- Beamer `\pause` and `\uncover` commands are used for animations
