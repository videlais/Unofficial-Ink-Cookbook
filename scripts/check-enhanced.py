#!/usr/bin/env python3
"""
Enhanced readability checker with basic style analysis (no Java required).
Uses textstat for readability + custom checks for common issues.
"""

import sys
import re
import textstat
from pathlib import Path
from collections import Counter

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

def find_passive_voice(text):
    """Find potential passive voice constructions using regex patterns."""
    # Common passive voice patterns
    passive_patterns = [
        r'\b(is|are|was|were|be|been|being)\s+\w+ed\b',
        r'\b(is|are|was|were|be|been|being)\s+\w+en\b',
    ]
    
    passive_instances = []
    sentences = re.split(r'[.!?]+', text)
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        for pattern in passive_patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                passive_instances.append(sentence)
                break
    
    return passive_instances

def find_long_sentences(text, threshold=20):
    """Find sentences longer than threshold words."""
    sentences = re.split(r'[.!?]+', text)
    long_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        word_count = len(sentence.split())
        if word_count > threshold:
            long_sentences.append((sentence, word_count))
    
    return long_sentences

def find_complex_words(text):
    """Find words with 4+ syllables (potentially complex)."""
    # Simple syllable counter
    def count_syllables(word):
        word = word.lower()
        vowels = 'aeiouy'
        syllables = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllables += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent e
        if word.endswith('e'):
            syllables -= 1
        
        # Every word has at least one syllable
        if syllables == 0:
            syllables = 1
        
        return syllables
    
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    complex_words = []
    
    for word in words:
        if len(word) > 3 and count_syllables(word) >= 4:
            complex_words.append(word.lower())
    
    # Count occurrences
    word_counts = Counter(complex_words)
    return word_counts.most_common(10)

def find_wordy_phrases(text):
    """Find common wordy phrases that could be simplified."""
    wordy_phrases = {
        r'\bat this point in time\b': 'now',
        r'\bdue to the fact that\b': 'because',
        r'\bin the event that\b': 'if',
        r'\bfor the purpose of\b': 'to',
        r'\bin order to\b': 'to',
        r'\bwith regard to\b': 'about',
        r'\bat the present time\b': 'now',
        r'\bprior to\b': 'before',
        r'\bsubsequent to\b': 'after',
    }
    
    found = []
    for pattern, replacement in wordy_phrases.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            found.append((match.group(), replacement))
    
    return found

def analyze_style(text):
    """Analyze text for common style issues."""
    passive_voice = find_passive_voice(text)
    long_sentences = find_long_sentences(text, threshold=20)
    complex_words = find_complex_words(text)
    wordy_phrases = find_wordy_phrases(text)
    
    # Average sentence length
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    
    return {
        'passive_voice': passive_voice,
        'long_sentences': long_sentences,
        'complex_words': complex_words,
        'wordy_phrases': wordy_phrases,
        'avg_sentence_length': avg_sentence_length,
        'total_sentences': len(sentences)
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python check-enhanced.py <markdown-file>")
        print("Example: python check-enhanced.py _chapters/01/index.md")
        return 1
    
    filepath = sys.argv[1]
    
    if not Path(filepath).exists():
        print(f"Error: File '{filepath}' not found")
        return 1
    
    text = extract_text_from_markdown(filepath)
    
    if len(text.strip()) < 100:
        print("Error: Not enough text to analyze")
        return 1
    
    filename = Path(filepath).name
    
    # Readability analysis
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
    
    # Style analysis
    style = analyze_style(text)
    
    # Print readability report
    print("=" * 70)
    print(f"Enhanced Readability & Style Analysis: {filename}")
    print("=" * 70)
    print()
    print(f"Word Count: {word_count}")
    print(f"Sentence Count: {sentence_count}")
    print(f"Avg Sentence Length: {style['avg_sentence_length']:.1f} words")
    print()
    print("Grade Level Metrics:")
    print(f"  Flesch-Kincaid Grade:     {fk_grade:.1f}")
    print(f"  Gunning Fog Index:        {fog_index:.1f}")
    print(f"  SMOG Index:               {smog_index:.1f}")
    print(f"  Coleman-Liau Index:       {cli_index:.1f}")
    print(f"  Automated Readability:    {ari:.1f}")
    print(f"  Dale-Chall Score:         {dale_chall:.1f}")
    print()
    print(f"  AVERAGE GRADE LEVEL:      {avg_grade:.1f}")
    print()
    print(f"Flesch Reading Ease: {flesch_ease:.1f}")
    print(f"  → {ease_desc}")
    print()
    
    # Style issues
    print("=" * 70)
    print("Style Analysis")
    print("=" * 70)
    print()
    
    # Passive voice
    if style['passive_voice']:
        print(f"🔴 PASSIVE VOICE: {len(style['passive_voice'])} instances")
        print("   → Use active voice for clearer, more direct writing")
        for i, sentence in enumerate(style['passive_voice'][:3], 1):
            print(f"   {i}. {sentence[:80]}...")
        if len(style['passive_voice']) > 3:
            print(f"   ... and {len(style['passive_voice']) - 3} more")
        print()
    else:
        print("✅ PASSIVE VOICE: None detected - good!")
        print()
    
    # Long sentences
    if style['long_sentences']:
        print(f"🟡 LONG SENTENCES: {len(style['long_sentences'])} over 20 words")
        print("   → Break into shorter sentences (target: 8-15 words)")
        for i, (sentence, word_count) in enumerate(style['long_sentences'][:3], 1):
            print(f"   {i}. ({word_count} words) {sentence[:70]}...")
        if len(style['long_sentences']) > 3:
            print(f"   ... and {len(style['long_sentences']) - 3} more")
        print()
    else:
        print("✅ SENTENCE LENGTH: All under 20 words - good!")
        print()
    
    # Complex words
    if style['complex_words']:
        print(f"🟡 COMPLEX WORDS: {len(style['complex_words'])} unique words with 4+ syllables")
        print("   → Consider simpler alternatives")
        for word, count in style['complex_words'][:5]:
            print(f"   • {word} (used {count} time{'s' if count > 1 else ''})")
        print()
    
    # Wordy phrases
    if style['wordy_phrases']:
        print(f"🟡 WORDY PHRASES: {len(style['wordy_phrases'])} instances")
        print("   → Simplify for conciseness")
        for phrase, replacement in set(style['wordy_phrases']):
            print(f"   • '{phrase}' → '{replacement}'")
        print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY & RECOMMENDATIONS")
    print("=" * 70)
    print()
    
    if avg_grade <= 5.5:
        print("✅ READABILITY: At target (4th-5th grade)")
    else:
        diff = avg_grade - 4.5
        print(f"⚠️  READABILITY: {diff:.1f} grades above target")
        print("   Actions:")
        print("   • Shorten sentences (target 8-15 words)")
        print("   • Replace complex words with simpler ones")
        print("   • Use more active voice")
    
    print()
    
    total_style_issues = (len(style['passive_voice']) + 
                         len(style['long_sentences']) + 
                         len(style['wordy_phrases']))
    
    if total_style_issues == 0:
        print("✅ STYLE: Excellent - clear and concise")
    elif total_style_issues < 10:
        print(f"🟡 STYLE: {total_style_issues} issues to address")
    else:
        print(f"🔴 STYLE: {total_style_issues} issues - needs significant revision")
    
    print()
    print("=" * 70)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
