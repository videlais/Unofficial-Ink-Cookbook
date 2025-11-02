#!/usr/bin/env python3
"""
Batch analyze all chapter files for readability.
"""

import os
import sys
import glob
from pathlib import Path
import re
import textstat

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

def analyze_file(filepath):
    """Analyze a single markdown file and return metrics."""
    text = extract_text_from_markdown(filepath)
    
    if not text or len(text.strip()) < 100:
        return None
    
    # Calculate metrics
    word_count = textstat.lexicon_count(text, removepunct=True)
    sentence_count = textstat.sentence_count(text)
    syllable_count = textstat.syllable_count(text)
    
    if sentence_count == 0 or word_count == 0:
        return None
    
    fk_grade = textstat.flesch_kincaid_grade(text)
    fog_index = textstat.gunning_fog(text)
    smog_index = textstat.smog_index(text)
    cli_index = textstat.coleman_liau_index(text)
    ari = textstat.automated_readability_index(text)
    dale_chall = textstat.dale_chall_readability_score(text)
    
    avg_grade = (fk_grade + fog_index + smog_index + cli_index + ari + dale_chall) / 6
    
    flesch_ease = textstat.flesch_reading_ease(text)
    
    return {
        'filepath': filepath,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'syllable_count': syllable_count,
        'avg_grade': avg_grade,
        'fk_grade': fk_grade,
        'fog_index': fog_index,
        'smog_index': smog_index,
        'cli_index': cli_index,
        'ari': ari,
        'dale_chall': dale_chall,
        'flesch_ease': flesch_ease
    }

def main():
    # Find all chapter index.md files
    chapter_pattern = "_chapters/*/index.md"
    chapter_files = sorted(glob.glob(chapter_pattern))
    
    if not chapter_files:
        print("No chapter files found!")
        return 1
    
    print("=" * 80)
    print("READABILITY ANALYSIS - ALL CHAPTERS")
    print("=" * 80)
    print()
    
    results = []
    
    for filepath in chapter_files:
        chapter_num = os.path.basename(os.path.dirname(filepath))
        result = analyze_file(filepath)
        
        if result:
            result['chapter'] = chapter_num
            results.append(result)
    
    # Print summary table
    print(f"{'Ch':<4} {'Words':<7} {'Sents':<7} {'Avg Grade':<10} {'Status':<15}")
    print("-" * 80)
    
    total_above_target = 0
    total_at_target = 0
    
    for r in results:
        status = "✅ AT TARGET" if r['avg_grade'] <= 5.5 else "⚠️  NEEDS WORK"
        if r['avg_grade'] > 5.5:
            total_above_target += 1
        else:
            total_at_target += 1
        
        print(f"{r['chapter']:<4} {r['word_count']:<7} {r['sentence_count']:<7} {r['avg_grade']:<10.1f} {status:<15}")
    
    print("-" * 80)
    print()
    
    # Print detailed results
    print("\nDETAILED METRICS:")
    print("=" * 80)
    
    for r in results:
        print(f"\nChapter {r['chapter']}")
        print(f"  Words: {r['word_count']}, Sentences: {r['sentence_count']}, Syllables: {r['syllable_count']}")
        print(f"  Flesch-Kincaid Grade:     {r['fk_grade']:.1f}")
        print(f"  Gunning Fog Index:        {r['fog_index']:.1f}")
        print(f"  SMOG Index:               {r['smog_index']:.1f}")
        print(f"  Coleman-Liau Index:       {r['cli_index']:.1f}")
        print(f"  Automated Readability:    {r['ari']:.1f}")
        print(f"  Dale-Chall Score:         {r['dale_chall']:.1f}")
        print(f"  AVERAGE GRADE LEVEL:      {r['avg_grade']:.1f}")
        print(f"  Flesch Reading Ease:      {r['flesch_ease']:.1f}")
        
        if r['avg_grade'] <= 5.5:
            print(f"  ✅ AT TARGET (4th-5th grade)")
        else:
            diff = r['avg_grade'] - 4.5
            print(f"  ⚠️  ABOVE TARGET by {diff:.1f} grades")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total chapters analyzed: {len(results)}")
    print(f"At target (≤5.5 grade):  {total_at_target}")
    print(f"Needs work (>5.5 grade): {total_above_target}")
    
    if total_above_target > 0:
        print(f"\n⚠️  {total_above_target} chapter(s) need simplification to reach 4th-5th grade level")
    else:
        print(f"\n✅ All chapters meet the 4th-5th grade reading level target!")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
