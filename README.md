# YAML to Beamer Presentation Generator

A Python-based system for generating LaTeX Beamer presentations from structured YAML lesson plans.

## Overview

This project automates the creation of educational slide presentations by separating content (YAML) from formatting (LaTeX templates). Teachers can focus on lesson content while the system handles the technical details of presentation generation.

## Project Status

✅ **Minimal Working Example Complete** - 5 slides, 2 template types

## Features

- ✅ Define lesson content in simple YAML format
- ✅ YAML schema documentation
- ✅ Python generator script
- ✅ Two slide templates: `do_now` and `diagnostic_question`
- ✅ LaTeX math notation support
- ✅ Working example with 5 slides
- 🚧 Schema validation for YAML structure
- 📋 Additional slide templates (text, two-column, graphs, etc.)
- 📋 Animation support for step-by-step reveals

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

### Current (v0.1)
- **`do_now`** - Warm-up problems with numbered questions
  - Generates TWO slides: questions only, then questions with answers
  - Supports LaTeX math notation
  - Auto-numbered questions with customizable spacing

- **`diagnostic_question`** - Multiple choice assessment
  - Single question with labeled options (A, B, C, D, ...)
  - Correct answer marked with green checkmark
  - Supports LaTeX math in questions and answers

### Planned
- `purpose_slide` - Learning objectives/goals
- `text_slide` - Simple title and content
- `two_column_slide` - Split content layout
- `equation_slide` - Mathematical equations
- `graph_slide` - Coordinate plane graphs
- `image_slide` - Images with captions
- `code_slide` - Code listings

## Development Roadmap

### Phase 1: MVP ✅ Complete
- [x] Define project structure
- [x] Create 5-slide example
- [x] Build basic Python generator
- [x] Implement 2 core templates (`do_now`, `diagnostic_question`)
- [x] Test end-to-end workflow
- [x] Document YAML schema

### Phase 2: Core Features
- [ ] Add 5 more slide templates
- [ ] Implement YAML schema validation
- [ ] Add animation support
- [ ] Create comprehensive documentation
- [ ] Build test suite

### Phase 3: Math Support
- [ ] TikZ graph generation templates
- [ ] Equation formatting templates
- [ ] Step-by-step problem solving layouts
- [ ] Interactive overlays

### Phase 4: Polish
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
