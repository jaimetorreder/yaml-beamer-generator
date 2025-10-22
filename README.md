# YAML to Beamer Presentation Generator

A Python-based system for generating LaTeX Beamer presentations from structured YAML lesson plans.

## Overview

This project automates the creation of educational slide presentations by separating content (YAML) from formatting (LaTeX templates). Teachers can focus on lesson content while the system handles the technical details of presentation generation.

## Project Status

🚧 **Currently in Development** - Starting with a minimal viable product (5 slides, 2 templates)

## Features (Planned)

- ✅ Define lesson content in simple YAML format
- ✅ Modular LaTeX templates for different slide types
- ✅ Python generator validates and compiles presentations
- 🚧 Multiple slide templates (text, two-column, graphs, etc.)
- 🚧 Animation support for step-by-step reveals
- 🚧 Schema validation for YAML structure
- 📋 Full math lesson support with equations and graphs

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

# Install Python dependencies
pip install -r requirements.txt

# Verify LaTeX installation
pdflatex --version
```

### Basic Usage

```bash
# Generate presentation from YAML
python generate_presentation.py lesson.yaml

# Output will be: lesson.tex and lesson.pdf
```

## Project Structure

```
yaml-beamer-generator/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── schema.yaml              # YAML structure definition
├── generate_presentation.py # Main generator script
├── templates/               # LaTeX slide templates
│   ├── text_slide.tex
│   ├── two_column_slide.tex
│   └── ...
├── examples/                # Example lesson plans
│   ├── simple_lesson.yaml
│   └── math_lesson.yaml
├── tests/                   # Unit tests
│   └── test_generator.py
└── docs/                    # Documentation
    ├── yaml_guide.md
    └── template_guide.md
```

## YAML Lesson Format

Example lesson structure:

```yaml
presentation:
  title: "Introduction to Linear Equations"
  author: "Your Name"
  date: "2025"

slides:
  - type: text_slide
    title: "Learning Objectives"
    content: |
      By the end of this lesson, students will:
      - Understand slope-intercept form
      - Graph linear equations
      - Solve real-world problems

  - type: two_column_slide
    title: "Example Problem"
    left_content: "Graph: y = 2x + 3"
    right_content: |
      Steps:
      1. Identify slope: m = 2
      2. Identify y-intercept: b = 3
      3. Plot points and draw line
```

## Available Slide Templates

### Current (v0.1)
- `text_slide` - Simple title and content
- `two_column_slide` - Split content layout

### Planned
- `title_slide` - Presentation title page
- `bullet_slide` - Bulleted lists with animations
- `equation_slide` - Mathematical equations
- `graph_slide` - Coordinate plane graphs
- `image_slide` - Images with captions
- `code_slide` - Code listings
- `quiz_slide` - Multiple choice questions

## Development Roadmap

### Phase 1: MVP (Current)
- [x] Define project structure
- [ ] Create 5-slide example
- [ ] Build basic Python generator
- [ ] Implement 2 core templates
- [ ] Test end-to-end workflow

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
