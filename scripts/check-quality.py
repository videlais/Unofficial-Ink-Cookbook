#!/usr/bin/env python3
"""
Enhanced readability checker with grammar and style analysis.
Combines textstat (readability) with language-tool-python (grammar/style).
"""

import sys
import re
import textstat
import language_tool_python
from pathlib import Path

def extract_text_from_markdown(filepath):
    """Extract plain text from markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove front matter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove headings markers but keep text
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
    
    # Remove emphasis markers
    content = re.sub(r'\*\*([^\*]+)\*\*', r'\1', content)
    content = re.sub(r'\*([^\*]+)\*', r'\1', content)
    content = re.sub(r'__([^_]+)__', r'\1', content)
    content = re.sub(r'_([^_]+)_', r'\1', content)
    
    # Remove list markers
    content = re.sub(r'^\s*[-*+]\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*\d+\.\s+', '', content, flags=re.MULTILINE)
    
    # Remove horizontal rules
    content = re.sub(r'^---+\s*$', '', content, flags=re.MULTILINE)
    
    # Remove extra whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = content.strip()
    
    return content

def get_readability_ease_description(score):
    """Convert Flesch Reading Ease score to description."""
    if score >= 90:
        return "Very Easy (5th grade)"
    elif score >= 80:
        return "Easy (6th grade)"
    elif score >= 70:
        return "Fairly Easy (7th grade)"
    elif score >= 60:
        return "Standard (8th-9th grade)"
    elif score >= 50:
        return "Fairly Difficult (10th-12th grade)"
    elif score >= 30:
        return "Difficult (College)"
    else:
        return "Very Difficult (College graduate)"

def analyze_readability(text):
    """Analyze text readability using textstat."""
    word_count = textstat.lexicon_count(text, removepunct=True)
    sentence_count = textstat.sentence_count(text)
    syllable_count = textstat.syllable_count(text)
    
    fk_grade = textstat.flesch_kincaid_grade(text)
    fog_index = textstat.gunning_fog(text)
    smog_index = textstat.smog_index(text)
    cli_index = textstat.coleman_liau_index(text)
    ari = textstat.automated_readability_index(text)
    dale_chall = textstat.dale_chall_readability_score(text)
    
    avg_grade = (fk_grade + fog_index + smog_index + cli_index + ari + dale_chall) / 6
    
    flesch_ease = textstat.flesch_reading_ease(text)
    ease_desc = get_readability_ease_description(flesch_ease)
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'syllable_count': syllable_count,
        'fk_grade': fk_grade,
        'fog_index': fog_index,
        'smog_index': smog_index,
        'cli_index': cli_index,
        'ari': ari,
        'dale_chall': dale_chall,
        'avg_grade': avg_grade,
        'flesch_ease': flesch_ease,
        'ease_desc': ease_desc
    }

def analyze_grammar_and_style(text, tool):
    """Analyze grammar and style issues using LanguageTool."""
    matches = tool.check(text)
    
    issues = {
        'passive_voice': [],
        'long_sentences': [],
        'complex_words': [],
        'wordiness': [],
        'grammar': [],
        'spelling': [],
        'punctuation': [],
        'style': []
    }
    
    for match in matches:
        rule_id = match.ruleId.upper()
        
        # Categorize by rule type
        if 'PASSIVE' in rule_id:
            issues['passive_voice'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        elif 'SENTENCE_LENGTH' in rule_id or 'TOO_LONG' in rule_id:
            issues['long_sentences'].append({
                'message': match.message,
                'context': match.context
            })
        elif 'COMPLEX' in rule_id or 'SIMPLIFY' in rule_id:
            issues['complex_words'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        elif 'WORDY' in rule_id or 'REDUNDANT' in rule_id:
            issues['wordiness'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        elif match.ruleIssueType == 'misspelling':
            issues['spelling'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        elif match.ruleIssueType == 'grammar':
            issues['grammar'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        elif 'PUNCTUATION' in rule_id or match.ruleIssueType == 'typographical':
            issues['punctuation'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
        else:
            issues['style'].append({
                'message': match.message,
                'context': match.context,
                'suggestions': match.replacements[:3]
            })
    
    return issues, len(matches)

def print_readability_report(filepath, metrics):
    """Print readability analysis report."""
    filename = Path(filepath).name
    
    print("=" * 70)
    print(f"Readability Analysis: {filename}")
    print("=" * 70)
    print()
    print(f"Word Count: {metrics['word_count']}")
    print(f"Sentence Count: {metrics['sentence_count']}")
    print(f"Syllable Count: {metrics['syllable_count']}")
    print()
    print("Grade Level Metrics:")
    print(f"  Flesch-Kincaid Grade:     {metrics['fk_grade']:.1f}")
    print(f"  Gunning Fog Index:        {metrics['fog_index']:.1f}")
    print(f"  SMOG Index:               {metrics['smog_index']:.1f}")
    print(f"  Coleman-Liau Index:       {metrics['cli_index']:.1f}")
    print(f"  Automated Readability:    {metrics['ari']:.1f}")
    print(f"  Dale-Chall Score:         {metrics['dale_chall']:.1f}")
    print()
    print(f"  AVERAGE GRADE LEVEL:      {metrics['avg_grade']:.1f}")
    print()
    print(f"Flesch Reading Ease: {metrics['flesch_ease']:.1f}")
    print(f"  → {metrics['ease_desc']}")
    print()

def print_grammar_report(issues, total):
    """Print grammar and style issues report."""
    print("=" * 70)
    print("Grammar & Style Analysis")
    print("=" * 70)
    print()
    print(f"Total Issues Found: {total}")
    print()
    
    # Passive Voice
    if issues['passive_voice']:
        print(f"🔴 PASSIVE VOICE ({len(issues['passive_voice'])} instances)")
        print("   → Consider using active voice for clarity")
        for i, issue in enumerate(issues['passive_voice'][:3], 1):
            print(f"   {i}. {issue['message']}")
            if issue['suggestions']:
                print(f"      Suggestion: {', '.join(issue['suggestions'])}")
        if len(issues['passive_voice']) > 3:
            print(f"   ... and {len(issues['passive_voice']) - 3} more")
        print()
    
    # Long Sentences
    if issues['long_sentences']:
        print(f"🟡 LONG SENTENCES ({len(issues['long_sentences'])} instances)")
        print("   → Break into shorter sentences for readability")
        for i, issue in enumerate(issues['long_sentences'][:3], 1):
            print(f"   {i}. {issue['message']}")
        if len(issues['long_sentences']) > 3:
            print(f"   ... and {len(issues['long_sentences']) - 3} more")
        print()
    
    # Complex Words
    if issues['complex_words']:
        print(f"🟡 COMPLEX WORDS ({len(issues['complex_words'])} instances)")
        print("   → Use simpler alternatives")
        for i, issue in enumerate(issues['complex_words'][:3], 1):
            print(f"   {i}. {issue['message']}")
            if issue['suggestions']:
                print(f"      Suggestion: {', '.join(issue['suggestions'])}")
        if len(issues['complex_words']) > 3:
            print(f"   ... and {len(issues['complex_words']) - 3} more")
        print()
    
    # Wordiness
    if issues['wordiness']:
        print(f"🟡 WORDINESS ({len(issues['wordiness'])} instances)")
        print("   → Remove redundant words")
        for i, issue in enumerate(issues['wordiness'][:3], 1):
            print(f"   {i}. {issue['message']}")
            if issue['suggestions']:
                print(f"      Suggestion: {', '.join(issue['suggestions'])}")
        if len(issues['wordiness']) > 3:
            print(f"   ... and {len(issues['wordiness']) - 3} more")
        print()
    
    # Grammar Errors
    if issues['grammar']:
        print(f"🔴 GRAMMAR ERRORS ({len(issues['grammar'])} instances)")
        for i, issue in enumerate(issues['grammar'][:5], 1):
            print(f"   {i}. {issue['message']}")
            if issue['suggestions']:
                print(f"      Suggestion: {', '.join(issue['suggestions'])}")
        if len(issues['grammar']) > 5:
            print(f"   ... and {len(issues['grammar']) - 5} more")
        print()
    
    # Spelling
    if issues['spelling']:
        print(f"🔴 SPELLING ({len(issues['spelling'])} instances)")
        for i, issue in enumerate(issues['spelling'][:5], 1):
            print(f"   {i}. {issue['message']}")
            if issue['suggestions']:
                print(f"      Suggestion: {', '.join(issue['suggestions'])}")
        if len(issues['spelling']) > 5:
            print(f"   ... and {len(issues['spelling']) - 5} more")
        print()
    
    # Other Style Issues
    other_count = len(issues['style']) + len(issues['punctuation'])
    if other_count > 0:
        print(f"ℹ️  OTHER STYLE/PUNCTUATION ({other_count} instances)")
        print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python check-quality.py <markdown-file>")
        print("Example: python check-quality.py _chapters/01/index.md")
        return 1
    
    filepath = sys.argv[1]
    
    if not Path(filepath).exists():
        print(f"Error: File '{filepath}' not found")
        return 1
    
    print("Loading text and initializing grammar checker...")
    text = extract_text_from_markdown(filepath)
    
    if len(text.strip()) < 100:
        print("Error: Not enough text to analyze")
        return 1
    
    # Initialize LanguageTool
    # Using public API (no Java required, but requires internet)
    print("Connecting to LanguageTool API...")
    tool = language_tool_python.LanguageToolPublicAPI('en-US')
    
    print("Analyzing readability...")
    readability = analyze_readability(text)
    
    print("Analyzing grammar and style...")
    issues, total_issues = analyze_grammar_and_style(text, tool)
    
    # Print reports
    print("\n")
    print_readability_report(filepath, readability)
    print_grammar_report(issues, total_issues)
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    if readability['avg_grade'] <= 5.5:
        print("✅ Readability: AT TARGET (4th-5th grade)")
    else:
        diff = readability['avg_grade'] - 4.5
        print(f"⚠️  Readability: ABOVE TARGET by {diff:.1f} grades")
    
    critical_issues = len(issues['grammar']) + len(issues['spelling'])
    if critical_issues == 0:
        print("✅ Grammar & Spelling: No errors found")
    else:
        print(f"🔴 Grammar & Spelling: {critical_issues} error(s) need fixing")
    
    style_issues = (len(issues['passive_voice']) + len(issues['long_sentences']) + 
                   len(issues['complex_words']) + len(issues['wordiness']))
    if style_issues == 0:
        print("✅ Style: Excellent")
    elif style_issues < 5:
        print(f"🟡 Style: {style_issues} suggestion(s) for improvement")
    else:
        print(f"🟡 Style: {style_issues} issues - focus on active voice and simplicity")
    
    print("=" * 70)
    
    # Cleanup
    tool.close()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
