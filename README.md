# YAML to Beamer Presentation Generator

A Python-based system for generating LaTeX Beamer presentations from structured YAML lesson plans.

## Overview

This project automates the creation of educational slide presentations by separating content (YAML) from formatting (LaTeX templates). Teachers can focus on lesson content while the system handles the technical details of presentation generation.

## Project Status

✅ **Full Template System Complete** - 10 slide template types

## Features

- ✅ Define lesson content in simple YAML format
- ✅ YAML schema documentation
- ✅ Python generator script
- ✅ **10 slide templates** covering full lesson workflow
- ✅ LaTeX math notation support
- ✅ Beamer animation support (overlays, progressive reveals)
- ✅ Working examples (simple and comprehensive)
- 🚧 Schema validation for YAML structure
- 📋 Additional slide templates (graphs, images, etc.)

## Quick Start

### Prerequisites

- Python 3.8+
- LaTeX distribution with Beamer (TeX Live, MiKTeX, etc.)
- pdflatex command available in PATH

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yaml-beamer-generator.git
cd yaml-beamer-generator

# Install Python dependencies (only PyYAML required)
pip install pyyaml

# (Optional) Verify LaTeX installation to compile PDFs
pdflatex --version
```

### Basic Usage

```bash
# Generate LaTeX from YAML
python generate_beamer.py example_lesson.yaml output.tex

# Or output to stdout
python generate_beamer.py example_lesson.yaml

# Compile to PDF (if you have pdflatex)
pdflatex output.tex
```

## Project Structure

```
yaml-beamer-generator/
├── README.md                 # This file
├── schema.md                 # YAML structure documentation
├── generate_beamer.py        # Main generator script
├── example_lesson.yaml       # Example lesson with 5 slides
└── example_output.tex        # Generated LaTeX output
```

## YAML Lesson Format

See [schema.md](schema.md) for complete documentation.

Example lesson structure:

```yaml
title: "Linear Functions Review"
author: "Math Teacher"
date: "2025-10-22"

slides:
  # Do Now - generates 2 slides (questions + answers)
  - type: do_now
    title: "Do Now"
    questions:
      - question: "Solve: $2x + 5 = 13$"
        answer: "$x = 4$"
      - question: "What is the slope of $y = 3x - 2$?"
        answer: "$m = 3$"

  # Diagnostic Question - multiple choice
  - type: diagnostic_question
    title: "Diagnostic: Slope"
    question: "What is the slope of a horizontal line?"
    options:
      - "0"
      - "1"
      - "Undefined"
      - "Negative"
    correct: 0  # Index of correct answer (0-based)
```

## Available Slide Templates

### Current (v1.0) - Complete Lesson Workflow

#### 1. **`do_now`** - Warm-up Problems
- Generates TWO slides: questions only, then questions with answers
- Auto-numbered questions (typically 4)
- Answers displayed in green

#### 2. **`learning_goals`** - Learning Objectives
- Large font bulleted list
- Typically 1-3 learning goals

#### 3. **`diagnostic_question`** - Formative Assessment (Seen Atom)
- Multiple choice with A, B, C, D options
- Animated reveal of green checkmark
- Optional explanation in green

#### 4. **`new_atom_fact`** - Introduce Facts/Properties
- Shows fact with multiple examples
- Progressive reveal with pause
- Side-by-side statement and result

#### 5. **`new_atom_category`** - Teach Classifications
- Shows categories with descriptions
- Examples as bulleted lists
- Progressive reveal

#### 6. **`new_atom_transformation`** - Show Transformations
- Step-by-step transformations (from → to)
- Progressive reveal between steps
- Great for algebraic manipulations

#### 7. **`i_do`** - Teacher Demonstration
- Worked example with labeled steps
- Progressive reveal of each step
- Final answer in large font

#### 8. **`we_do`** - Guided Practice
- Similar to I Do but for collaboration
- Currently identical to `i_do` template

#### 9. **`practice`** - Independent Practice
- Multiple problems with answers
- Progressive answer reveal (overlay animations)
- All questions visible from start

#### 10. **`closure`** - Lesson Summary
- "What We Learned Today" heading
- Multiple topics with bullet points
- Perfect for wrapping up

### Planned
- `graph_slide` - Coordinate plane graphs with TikZ
- `image_slide` - Images with captions
- `two_column_slide` - Split content layout

## Development Roadmap

### Phase 1: MVP ✅ Complete
- [x] Define project structure
- [x] Create initial examples
- [x] Build basic Python generator
- [x] Implement core templates
- [x] Test end-to-end workflow

### Phase 2: Full Template System ✅ Complete
- [x] Implement 10 slide templates covering full lesson workflow
- [x] Add Beamer animation support (`\pause`, `\uncover`)
- [x] New Atom templates (Fact, Category, Transformation)
- [x] Teaching workflow templates (I Do, We Do, Practice, Closure)
- [x] Comprehensive example with all templates
- [x] Complete schema documentation

### Phase 3: Enhancements (Current)
- [ ] Add YAML schema validation
- [ ] Build test suite
- [ ] CLI improvements (error messages, validation)

### Phase 4: Advanced Features
- [ ] TikZ graph slide template
- [ ] Image slide template
- [ ] Two-column slide template
- [ ] Advanced math formatting options
- [ ] Step-by-step problem solving layouts with custom animations

### Phase 5: Polish
- [ ] CLI with options and flags
- [ ] Error handling and validation
- [ ] Template customization system
- [ ] Web-based YAML editor (stretch goal)

## Contributing

Contributions are welcome! This project is in early development.

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-template`)
3. Test your changes thoroughly
4. Commit your changes (`git commit -m 'Add amazing template'`)
5. Push to the branch (`git push origin feature/amazing-template`)
6. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Check code style
flake8 generate_presentation.py
black --check .
```

## Testing

```bash
# Run all tests
python -m pytest

# Run specific test
python -m pytest tests/test_generator.py

# Generate coverage report
python -m pytest --cov=. --cov-report=html
```

## Documentation

- [YAML Structure Guide](docs/yaml_guide.md)
- [Template Development Guide](docs/template_guide.md)
- [Examples](examples/)

## Known Issues

See [Issues](https://github.com/yourusername/yaml-beamer-generator/issues) for current bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for educators creating math presentations
- Inspired by the need to separate content from formatting
- Uses LaTeX Beamer for high-quality presentation output

## Support

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/yaml-beamer-generator/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/yaml-beamer-generator/discussions)

## Citation

If you use this project in your work, please cite:

```bibtex
@software{yaml_beamer_generator,
  title = {YAML to Beamer Presentation Generator},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/yourusername/yaml-beamer-generator}
}
```

---

**Status**: 🚧 In Development | **Version**: 0.1.0-alpha | **Last Updated**: October 2025
