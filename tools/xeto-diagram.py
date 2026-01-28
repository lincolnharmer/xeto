#!/usr/bin/env python3
"""
Generate inheritance diagrams from Xeto spec files.

Outputs:
  - Mermaid class diagrams (for GitHub markdown)
  - Text tree view (for terminal exploration)

Usage:
  ./xeto-diagram.py [OPTIONS] [FILES...]

Examples:
  # Generate diagram for all ph.attrs specs
  ./xeto-diagram.py src/xeto/ph.attrs/*.xeto

  # Generate diagram for just power.xeto
  ./xeto-diagram.py src/xeto/ph.attrs/power.xeto

  # Output Mermaid only
  ./xeto-diagram.py --mermaid src/xeto/ph.attrs/power.xeto

  # Output tree only
  ./xeto-diagram.py --tree src/xeto/ph.attrs/power.xeto

  # Filter to show only subtypes of a specific spec
  ./xeto-diagram.py --root PowerAttr src/xeto/ph.attrs/*.xeto
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class Spec:
    name: str
    parent: str
    is_abstract: bool
    markers: list[str]
    doc: str
    file: str
    line: int


def parse_xeto_file(filepath: Path) -> list[Spec]:
    """Parse a xeto file and extract spec definitions."""
    specs = []
    content = filepath.read_text()
    lines = content.split('\n')

    # Pattern: SpecName : ParentSpec <metadata> { markers }
    # or:      SpecName: ParentSpec <metadata> { markers }
    # Must start with uppercase letter (specs) to avoid matching slots (lowercase)
    spec_pattern = re.compile(
        r'^([A-Z]\w*)\s*:\s*([A-Z]\w*)\s*'  # Name : Parent (both uppercase)
        r'(?:<([^>]*)>)?\s*'                 # optional <metadata>
        r'(?:\{([^}]*)\})?'                  # optional { markers }
    )

    doc_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Collect doc comments
        if stripped.startswith('//'):
            comment = stripped[2:].strip()
            # Skip section headers and copyright
            if not comment.startswith('===') and not comment.startswith('Copyright') and not comment.startswith('Licensed') and not comment.startswith('History:') and not re.match(r'^\d+\s+\w+\s+\d+', comment):
                if comment and not comment.startswith('/'):
                    doc_lines.append(comment)
            continue

        # Try to match spec definition
        match = spec_pattern.match(stripped)
        if match:
            name = match.group(1)
            parent = match.group(2)
            metadata = match.group(3) or ''
            markers_str = match.group(4) or ''

            is_abstract = 'abstract' in metadata

            # Parse markers (comma-separated, may have key:value pairs)
            markers = []
            for m in markers_str.split(','):
                m = m.strip()
                if m and ':' not in m:  # Skip key:value pairs, keep simple markers
                    markers.append(m)

            doc = ' '.join(doc_lines) if doc_lines else ''

            specs.append(Spec(
                name=name,
                parent=parent,
                is_abstract=is_abstract,
                markers=markers,
                doc=doc,
                file=str(filepath),
                line=i + 1
            ))
            doc_lines = []
        elif stripped and not stripped.startswith('//'):
            doc_lines = []  # Reset if we hit non-comment, non-spec line

    return specs


def build_tree(specs: list[Spec], root: Optional[str] = None) -> dict:
    """Build a tree structure from specs."""
    children = defaultdict(list)
    spec_map = {s.name: s for s in specs}

    for spec in specs:
        children[spec.parent].append(spec.name)

    # If root specified, filter to only that subtree
    if root:
        def get_subtree(name):
            result = {name}
            for child in children.get(name, []):
                result.update(get_subtree(child))
            return result

        valid_names = get_subtree(root)
        specs = [s for s in specs if s.name in valid_names]
        children = defaultdict(list)
        for spec in specs:
            if spec.parent in valid_names or spec.name == root:
                children[spec.parent].append(spec.name)

    return children, spec_map


def generate_tree_text(specs: list[Spec], root: Optional[str] = None) -> str:
    """Generate a text tree representation."""
    children, spec_map = build_tree(specs, root)

    # Find root nodes (parents not in our spec set)
    all_names = {s.name for s in specs}
    roots = []
    for spec in specs:
        if spec.parent not in all_names:
            roots.append(spec.name)

    # If specific root requested, use that
    if root and root in all_names:
        roots = [root]

    lines = []

    def render_node(name: str, prefix: str = "", is_last: bool = True):
        spec = spec_map.get(name)
        connector = "└── " if is_last else "├── "

        # Format: Name (abstract) [markers]
        label = name
        if spec:
            if spec.is_abstract:
                label += " (abstract)"
            if spec.markers:
                label += f" [{', '.join(spec.markers)}]"

        lines.append(f"{prefix}{connector}{label}")

        child_prefix = prefix + ("    " if is_last else "│   ")
        child_names = sorted(children.get(name, []))
        for i, child in enumerate(child_names):
            render_node(child, child_prefix, i == len(child_names) - 1)

    for i, root_name in enumerate(sorted(roots)):
        if i > 0:
            lines.append("")
        spec = spec_map.get(root_name)
        label = root_name
        if spec:
            if spec.is_abstract:
                label += " (abstract)"
            if spec.markers:
                label += f" [{', '.join(spec.markers)}]"
        lines.append(label)

        child_names = sorted(children.get(root_name, []))
        for j, child in enumerate(child_names):
            render_node(child, "", j == len(child_names) - 1)

    return '\n'.join(lines)


def generate_mermaid(specs: list[Spec], root: Optional[str] = None, show_markers: bool = True) -> str:
    """Generate a Mermaid class diagram."""
    children, spec_map = build_tree(specs, root)

    all_names = {s.name for s in specs}

    lines = ["```mermaid", "classDiagram"]

    # Add inheritance relationships
    for spec in specs:
        if spec.parent in all_names or root is None:
            lines.append(f"    {spec.parent} <|-- {spec.name}")

    lines.append("")

    # Add class annotations
    for spec in specs:
        if spec.is_abstract:
            lines.append(f"    class {spec.name} {{")
            lines.append(f"        <<abstract>>")
            if show_markers and spec.markers:
                lines.append(f"        +{', '.join(spec.markers)}")
            lines.append(f"    }}")
        elif show_markers and spec.markers:
            lines.append(f"    class {spec.name} {{")
            lines.append(f"        +{', '.join(spec.markers)}")
            lines.append(f"    }}")

    lines.append("```")
    return '\n'.join(lines)


def generate_mermaid_subgraphs(specs: list[Spec], group_by_file: bool = True) -> str:
    """Generate Mermaid with subgraphs for each file/category."""
    if not group_by_file:
        return generate_mermaid(specs)

    # Group specs by file
    by_file = defaultdict(list)
    for spec in specs:
        filename = Path(spec.file).stem
        by_file[filename].append(spec)

    all_names = {s.name for s in specs}

    lines = ["```mermaid", "classDiagram"]

    # Add all inheritance relationships first
    for spec in specs:
        if spec.parent in all_names:
            lines.append(f"    {spec.parent} <|-- {spec.name}")

    lines.append("")

    # Add annotations
    for spec in specs:
        if spec.is_abstract:
            lines.append(f"    class {spec.name} {{")
            lines.append(f"        <<abstract>>")
            lines.append(f"    }}")

    lines.append("```")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate inheritance diagrams from Xeto spec files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('files', nargs='*', help='Xeto files to process')
    parser.add_argument('--mermaid', '-m', action='store_true',
                        help='Output Mermaid diagram only')
    parser.add_argument('--tree', '-t', action='store_true',
                        help='Output text tree only')
    parser.add_argument('--root', '-r',
                        help='Show only subtree starting from this spec')
    parser.add_argument('--no-markers', action='store_true',
                        help='Hide markers in Mermaid output')
    parser.add_argument('--output', '-o',
                        help='Write output to file instead of stdout')

    args = parser.parse_args()

    if not args.files:
        parser.print_help()
        sys.exit(1)

    # Parse all files
    all_specs = []
    for filepath in args.files:
        path = Path(filepath)
        if path.exists() and path.suffix == '.xeto':
            all_specs.extend(parse_xeto_file(path))

    if not all_specs:
        print("No specs found in the provided files.", file=sys.stderr)
        sys.exit(1)

    # Generate output
    output_parts = []

    if args.tree or (not args.mermaid and not args.tree):
        output_parts.append("## Inheritance Tree\n")
        output_parts.append(generate_tree_text(all_specs, args.root))
        output_parts.append("")

    if args.mermaid or (not args.mermaid and not args.tree):
        output_parts.append("\n## Class Diagram\n")
        output_parts.append(generate_mermaid(all_specs, args.root, not args.no_markers))

    output = '\n'.join(output_parts)

    if args.output:
        Path(args.output).write_text(output)
        print(f"Output written to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
