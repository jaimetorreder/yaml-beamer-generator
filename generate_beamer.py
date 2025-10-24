#!/usr/bin/env python3
"""
YAML to Beamer LaTeX Generator

Reads a YAML lesson plan and generates a Beamer presentation.
"""

import yaml
import sys
from typing import Dict, List, Any


class BeamerGenerator:
    """Generates Beamer LaTeX from YAML lesson plans."""

    def __init__(self, yaml_data: Dict[str, Any]):
        self.data = yaml_data
        self.title = yaml_data.get('title', 'Untitled Presentation')
        self.author = yaml_data.get('author', '')
        self.date = yaml_data.get('date', r'\today')
        self.slides = yaml_data.get('slides', [])

    def generate_preamble(self) -> str:
        """Generate the LaTeX preamble and title page."""
        preamble = r"""\documentclass{beamer}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{color}

\usetheme{Madrid}
\usecolortheme{default}

"""
        preamble += f"\\title{{{self.title}}}\n"
        if self.author:
            preamble += f"\\author{{{self.author}}}\n"
        preamble += f"\\date{{{self.date}}}\n"
        preamble += r"""
\begin{document}

\frame{\titlepage}

"""
        return preamble

    def generate_footer(self) -> str:
        """Generate the LaTeX footer."""
        return r"\end{document}" + "\n"

    def generate_do_now_slide(self, slide: Dict[str, Any]) -> str:
        """Generate Do Now slides (questions and answers)."""
        title = slide.get('title', 'Do Now')
        questions = slide.get('questions', [])

        # Questions slide
        latex = f"% SLIDE: {title} - Questions\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += r"\textbf{Solve the following problems:}" + "\n\n"
        latex += r"\vspace{0.5cm}" + "\n\n"

        for i, q in enumerate(questions, 1):
            question_text = q.get('question', '')
            latex += f"\\textbf{{{i}.}} {question_text}\n\n"
            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        # Answers slide
        latex += f"% SLIDE: {title} - Answers\n"
        latex += r"\begin{frame}{" + title + " - Answers}\n"

        for i, q in enumerate(questions, 1):
            question_text = q.get('question', '')
            answer_text = q.get('answer', '')

            latex += f"\\textbf{{{i}.}} {question_text}\n\n"
            latex += f"\\quad \\textbf{{Answer:}} {{\\color{{green}}{answer_text}}}\n\n"
            latex += r"\vspace{0.3cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_diagnostic_question_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a diagnostic question slide with multiple choice options.

        Uses Beamer overlays to show the answer on a second slide.
        First shows question and options, then reveals the checkmark and optional explanation.
        """
        title = slide.get('title', 'Diagnostic Question')
        question = slide.get('question', '')
        options = slide.get('options', [])
        correct = slide.get('correct', 0)
        explanation = slide.get('explanation', '')  # Optional explanation

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += f"\\textbf{{{question}}}\n\n"
        latex += r"\vspace{1cm}" + "\n\n"

        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for i, option in enumerate(options):
            label = labels[i] if i < len(labels) else str(i)
            # Checkmark appears only on overlay 2+
            checkmark = r" \quad {\color{green}\checkmark}" if i == correct else ""
            if checkmark:
                latex += f"\\textbf{{{label}.}} {option}\\onslide<2->{{{checkmark}}}\n\n"
            else:
                latex += f"\\textbf{{{label}.}} {option}\n\n"

        # Add explanation on overlay 2+ if provided
        if explanation:
            latex += r"\vspace{0.5cm}" + "\n\n"
            latex += r"\onslide<2->{" + "\n"
            latex += r"\textbf{Explanation:} {\color{green}" + explanation + "}\n"
            latex += "}\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_learning_goals_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a Learning Goals slide with a bulleted list.

        Displays 1-3 learning objectives in a large font with bullet points.
        """
        title = slide.get('title', 'Learning Goals')
        goals = slide.get('goals', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += r"\Large" + "\n"
        latex += r"\begin{itemize}" + "\n"

        for goal in goals:
            latex += f"\\item {goal}\n"

        latex += r"\end{itemize}" + "\n"
        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_new_atom_fact_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a New Atom: Fact slide.

        Shows a fact or property with multiple examples demonstrating it.
        """
        title = slide.get('title', 'New Atom: Fact')
        examples = slide.get('examples', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"

        for example in examples:
            statement = example.get('statement', '')
            result = example.get('result', '')

            latex += f"{statement} \\pause \\quad {result}\n\n"
            latex += r"\pause" + "\n"
            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_new_atom_category_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a New Atom: Category slide.

        Shows categorization or classification of concepts.
        """
        title = slide.get('title', 'New Atom: Category')
        categories = slide.get('categories', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"

        for category in categories:
            name = category.get('name', '')
            description = category.get('description', '')
            examples = category.get('examples', [])

            latex += f"\\textbf{{{name}:}} {description}\n\n"
            latex += r"\pause" + "\n"

            if examples:
                latex += r"\begin{itemize}" + "\n"
                for ex in examples:
                    latex += f"\\item {ex} \\pause\n"
                latex += r"\end{itemize}" + "\n\n"

            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_new_atom_transformation_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a New Atom: Transformation slide.

        Shows step-by-step transformations from one form to another.
        """
        title = slide.get('title', 'New Atom: Transformation')
        transformations = slide.get('transformations', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"

        for transform in transformations:
            from_expr = transform.get('from', '')
            to_expr = transform.get('to', '')

            latex += f"{from_expr} \\pause $\\rightarrow$ {to_expr}\n\n"
            latex += r"\pause" + "\n"
            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_i_do_slide(self, slide: Dict[str, Any]) -> str:
        """Generate an I Do slide.

        Teacher-led worked example with detailed steps.
        """
        title = slide.get('title', 'I Do')
        problem = slide.get('problem', '')
        steps = slide.get('steps', [])
        answer = slide.get('answer', '')

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += f"\\textbf{{Solve:}} {problem}\n\n"
        latex += r"\pause" + "\n"
        latex += r"\vspace{0.3cm}" + "\n\n"

        for i, step in enumerate(steps, 1):
            step_label = step.get('label', f'Step {i}')
            step_content = step.get('content', '')

            latex += f"\\textbf{{{step_label}:}} {step_content}\n\n"
            latex += r"\pause" + "\n"
            latex += r"\vspace{0.3cm}" + "\n\n"

        if answer:
            latex += r"\Large \textbf{Answer:} " + answer + "\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_we_do_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a We Do slide.

        Guided practice problem (similar to I Do but for student participation).
        For now, implemented identically to I Do.
        """
        # Reuse I Do template
        return self.generate_i_do_slide(slide)

    def generate_practice_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a Practice slide.

        Multiple practice problems with answers revealed progressively.
        """
        title = slide.get('title', 'Practice')
        problems = slide.get('problems', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += r"\textbf{Solve the following:}" + "\n\n"
        latex += r"\vspace{0.5cm}" + "\n\n"

        for i, problem in enumerate(problems, 1):
            question = problem.get('question', '')
            answer = problem.get('answer', '')

            latex += f"\\textbf{{{i}.}} {question} "
            latex += f"\\uncover<{i+1}->{{\\hfill {answer}}}\n\n"
            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_closure_slide(self, slide: Dict[str, Any]) -> str:
        """Generate a Closure slide.

        Summarizes what was learned in the lesson.
        """
        title = slide.get('title', 'Closure')
        topics = slide.get('topics', [])

        latex = f"% SLIDE: {title}\n"
        latex += r"\begin{frame}{" + title + "}\n"
        latex += r"\Large" + "\n"
        latex += r"\textbf{What We Learned Today:}" + "\n\n"
        latex += r"\vspace{0.5cm}" + "\n\n"
        latex += r"\normalsize" + "\n"

        for topic in topics:
            topic_title = topic.get('title', '')
            points = topic.get('points', [])

            latex += f"\\textbf{{{topic_title}:}}\n"
            latex += r"\begin{itemize}" + "\n"

            for point in points:
                latex += f"\\item {point}\n"

            latex += r"\end{itemize}" + "\n\n"
            latex += r"\vspace{0.5cm}" + "\n\n"

        latex += r"\end{frame}" + "\n\n"

        return latex

    def generate_slide(self, slide: Dict[str, Any]) -> str:
        """Generate LaTeX for a single slide based on its type."""
        slide_type = slide.get('type', '')

        if slide_type == 'do_now':
            return self.generate_do_now_slide(slide)
        elif slide_type == 'learning_goals':
            return self.generate_learning_goals_slide(slide)
        elif slide_type == 'diagnostic_question':
            return self.generate_diagnostic_question_slide(slide)
        elif slide_type == 'new_atom_fact':
            return self.generate_new_atom_fact_slide(slide)
        elif slide_type == 'new_atom_category':
            return self.generate_new_atom_category_slide(slide)
        elif slide_type == 'new_atom_transformation':
            return self.generate_new_atom_transformation_slide(slide)
        elif slide_type == 'i_do':
            return self.generate_i_do_slide(slide)
        elif slide_type == 'we_do':
            return self.generate_we_do_slide(slide)
        elif slide_type == 'practice':
            return self.generate_practice_slide(slide)
        elif slide_type == 'closure':
            return self.generate_closure_slide(slide)
        else:
            print(f"Warning: Unknown slide type '{slide_type}'", file=sys.stderr)
            return ""

    def generate(self) -> str:
        """Generate the complete Beamer presentation."""
        latex = self.generate_preamble()

        for slide in self.slides:
            latex += self.generate_slide(slide)

        latex += self.generate_footer()

        return latex


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python generate_beamer.py <input.yaml> [output.tex]")
        print("\nExample:")
        print("  python generate_beamer.py example_lesson.yaml output.tex")
        print("  python generate_beamer.py example_lesson.yaml  # outputs to stdout")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Read YAML file
    try:
        with open(input_file, 'r') as f:
            yaml_data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate LaTeX
    generator = BeamerGenerator(yaml_data)
    latex = generator.generate()

    # Output
    if output_file:
        with open(output_file, 'w') as f:
            f.write(latex)
        print(f"Generated: {output_file}")
    else:
        print(latex)


if __name__ == '__main__':
    main()
