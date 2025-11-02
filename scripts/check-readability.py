#!/usr/bin/env python3
"""
Readability Checker for Markdown Content

Analyzes text using multiple readability metrics to determine
appropriate grade level for content.
"""

import sys
import re
import textstat
from pathlib import Path


def extract_text_from_markdown(content):
    """Extract plain text from markdown, removing code blocks and front matter."""
    # Remove front matter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove markdown links but keep the text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove markdown formatting
    content = re.sub(r'[*_~#>-]', '', content)
    
    # Remove extra whitespace
    content = re.sub(r'\n+', ' ', content)
    content = re.sub(r'\s+', ' ', content)
    
    return content.strip()


def analyze_readability(text, filename=""):
    """Analyze text using multiple readability metrics."""
    
    print(f"\n{'='*70}")
    print(f"Readability Analysis: {filename}")
    print(f"{'='*70}\n")
    
    print(f"Word Count: {textstat.lexicon_count(text, removepunct=True)}")
    print(f"Sentence Count: {textstat.sentence_count(text)}")
    print(f"Syllable Count: {textstat.syllable_count(text)}\n")
    
    print("Grade Level Metrics:")
    print(f"  Flesch-Kincaid Grade:     {textstat.flesch_kincaid_grade(text):.1f}")
    print(f"  Gunning Fog Index:        {textstat.gunning_fog(text):.1f}")
    print(f"  SMOG Index:               {textstat.smog_index(text):.1f}")
    print(f"  Coleman-Liau Index:       {textstat.coleman_liau_index(text):.1f}")
    print(f"  Automated Readability:    {textstat.automated_readability_index(text):.1f}")
    print(f"  Dale-Chall Score:         {textstat.dale_chall_readability_score(text):.1f}")
    
    # Average grade level
    avg_grade = (
        textstat.flesch_kincaid_grade(text) +
        textstat.gunning_fog(text) +
        textstat.smog_index(text) +
        textstat.coleman_liau_index(text) +
        textstat.automated_readability_index(text)
    ) / 5
    
    print(f"\n  AVERAGE GRADE LEVEL:      {avg_grade:.1f}")
    
    # Flesch Reading Ease (higher = easier)
    ease = textstat.flesch_reading_ease(text)
    print(f"\nFlesch Reading Ease: {ease:.1f}")
    if ease >= 90:
        print("  → Very Easy (5th grade)")
    elif ease >= 80:
        print("  → Easy (6th grade)")
    elif ease >= 70:
        print("  → Fairly Easy (7th grade)")
    elif ease >= 60:
        print("  → Standard (8th-9th grade)")
    elif ease >= 50:
        print("  → Fairly Difficult (10th-12th grade)")
    elif ease >= 30:
        print("  → Difficult (College)")
    else:
        print("  → Very Difficult (College graduate)")
    
    print(f"\n{'='*70}")
    
    # Target assessment
    target_grade = 4.5  # 4th-5th grade
    if avg_grade <= target_grade:
        print(f"✅ MEETS TARGET: Content is at ~{avg_grade:.1f} grade level")
        print("   (Target: 4th-5th grade)")
    else:
        print(f"⚠️  ABOVE TARGET: Content is at ~{avg_grade:.1f} grade level")
        print(f"   (Target: 4th-5th grade, currently {avg_grade - target_grade:.1f} grades above)")
        print("\nSuggestions to simplify:")
        print("  • Use shorter sentences")
        print("  • Replace complex words with simpler alternatives")
        print("  • Break up long paragraphs")
        print("  • Use more active voice")
    
    print(f"{'='*70}\n")
    
    return avg_grade


def main():
    if len(sys.argv) < 2:
        print("Usage: python check-readability.py <file.md>")
        print("   or: python check-readability.py _chapters/01/index.md")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    
    content = filepath.read_text(encoding='utf-8')
    text = extract_text_from_markdown(content)
    
    analyze_readability(text, filepath.name)


if __name__ == '__main__':
    main()
