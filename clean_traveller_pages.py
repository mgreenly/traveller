#!/usr/bin/env python3
"""
Clean Traveller Core Rules page files by removing formatting artifacts while preserving game content.

This script processes all *-page.txt files in the core-rules-2022 directory and removes:
- Decorative single letters (T,R,A,V,E,L,L,E,R) that appear on their own lines
- Excessive blank lines
- Lines containing only whitespace
- Print/formatting artifacts
- Standalone page numbers at the bottom of pages

It preserves all legitimate game content including rules, tables, equipment lists, etc.
"""

import os
import re
import glob
from typing import List, Dict, Tuple

def is_traveller_decorative_letter(line: str, line_num: int, total_lines: int) -> bool:
    """
    Check if a line contains a decorative letter from TRAVELLER.
    These typically appear at the top or bottom of pages as single letters.
    """
    stripped = line.strip()
    
    # Single letters from TRAVELLER, usually at top of page (first 20 lines) or bottom (last 10 lines)
    if len(stripped) == 1 and stripped in 'TRAVELLER':
        # More likely to be decorative if at top or bottom of page
        if line_num <= 20 or line_num >= (total_lines - 10):
            return True
    
    return False

def is_page_number_line(line: str, line_num: int, total_lines: int) -> bool:
    """
    Check if a line is just a page number, typically at the bottom of pages.
    """
    stripped = line.strip()
    
    # Single number at bottom of page
    if stripped.isdigit() and line_num >= (total_lines - 5):
        return True
    
    return False

def is_formatting_artifact(line: str) -> bool:
    """
    Check if a line contains formatting artifacts from OCR/printing process.
    """
    stripped = line.strip()
    
    # Print layout marks
    if re.match(r'^Xavier\s*:\s*W\d+\.?\d*mm,\s*H\d+\.?\d*mm', stripped):
        return True
    
    # Other common artifacts - be conservative here
    # Empty lines or whitespace-only lines will be handled separately
    
    return False

def should_remove_line(line: str, line_num: int, total_lines: int, all_lines: List[str]) -> bool:
    """
    Determine if a line should be removed based on various criteria.
    """
    stripped = line.strip()
    
    # Empty lines and whitespace-only lines (will be handled by blank line consolidation)
    if not stripped:
        return False
    
    # Check for decorative TRAVELLER letters
    if is_traveller_decorative_letter(line, line_num, total_lines):
        return True
    
    # Check for standalone page numbers
    if is_page_number_line(line, line_num, total_lines):
        return True
    
    # Check for formatting artifacts
    if is_formatting_artifact(line):
        return True
    
    return False

def consolidate_blank_lines(lines: List[str]) -> List[str]:
    """
    Reduce multiple consecutive blank lines to single blank lines.
    """
    result = []
    prev_was_blank = False
    
    for line in lines:
        is_blank = not line.strip()
        
        if is_blank:
            if not prev_was_blank:
                result.append(line)
            prev_was_blank = True
        else:
            result.append(line)
            prev_was_blank = False
    
    return result

def clean_page_content(content: str) -> Tuple[str, Dict[str, int]]:
    """
    Clean a single page's content and return the cleaned content plus stats.
    """
    lines = content.splitlines(keepends=True)
    original_line_count = len(lines)
    
    # Statistics tracking
    stats = {
        'original_lines': original_line_count,
        'decorative_letters_removed': 0,
        'page_numbers_removed': 0,
        'formatting_artifacts_removed': 0,
        'blank_lines_before': 0,
        'blank_lines_after': 0
    }
    
    # Count original blank lines
    stats['blank_lines_before'] = sum(1 for line in lines if not line.strip())
    
    # Remove unwanted lines
    filtered_lines = []
    
    for i, line in enumerate(lines):
        if should_remove_line(line, i, len(lines), lines):
            stripped = line.strip()
            if len(stripped) == 1 and stripped in 'TRAVELLER':
                stats['decorative_letters_removed'] += 1
            elif stripped.isdigit():
                stats['page_numbers_removed'] += 1
            else:
                stats['formatting_artifacts_removed'] += 1
        else:
            filtered_lines.append(line)
    
    # Consolidate blank lines
    consolidated_lines = consolidate_blank_lines(filtered_lines)
    
    # Count final blank lines
    stats['blank_lines_after'] = sum(1 for line in consolidated_lines if not line.strip())
    stats['final_lines'] = len(consolidated_lines)
    
    return ''.join(consolidated_lines), stats

def clean_all_pages(directory: str) -> Dict[str, any]:
    """
    Clean all page files in the specified directory.
    """
    page_pattern = os.path.join(directory, "*-page.txt")
    page_files = sorted(glob.glob(page_pattern))
    
    if not page_files:
        print(f"No page files found matching pattern: {page_pattern}")
        return {}
    
    total_stats = {
        'files_processed': 0,
        'files_modified': 0,
        'total_original_lines': 0,
        'total_final_lines': 0,
        'total_decorative_letters_removed': 0,
        'total_page_numbers_removed': 0,
        'total_formatting_artifacts_removed': 0,
        'total_blank_lines_reduced': 0
    }
    
    file_details = {}
    
    print(f"Found {len(page_files)} page files to process...")
    
    for file_path in page_files:
        filename = os.path.basename(file_path)
        
        try:
            # Read original content
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Clean the content
            cleaned_content, file_stats = clean_page_content(original_content)
            
            # Check if anything actually changed
            content_changed = cleaned_content != original_content
            
            if content_changed:
                # Write cleaned content back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                total_stats['files_modified'] += 1
            
            # Update totals
            total_stats['files_processed'] += 1
            total_stats['total_original_lines'] += file_stats['original_lines']
            total_stats['total_final_lines'] += file_stats['final_lines']
            total_stats['total_decorative_letters_removed'] += file_stats['decorative_letters_removed']
            total_stats['total_page_numbers_removed'] += file_stats['page_numbers_removed']
            total_stats['total_formatting_artifacts_removed'] += file_stats['formatting_artifacts_removed']
            total_stats['total_blank_lines_reduced'] += (file_stats['blank_lines_before'] - file_stats['blank_lines_after'])
            
            # Store file details for reporting
            file_details[filename] = {
                'changed': content_changed,
                'stats': file_stats
            }
            
            if content_changed:
                removed_total = (file_stats['decorative_letters_removed'] + 
                               file_stats['page_numbers_removed'] + 
                               file_stats['formatting_artifacts_removed'])
                print(f"  {filename}: {file_stats['original_lines']} → {file_stats['final_lines']} lines "
                      f"({removed_total} artifacts removed)")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    return {
        'total_stats': total_stats,
        'file_details': file_details
    }

def print_summary(results: Dict[str, any]):
    """
    Print a summary of the cleaning operation.
    """
    if not results:
        print("No results to summarize.")
        return
    
    stats = results['total_stats']
    details = results['file_details']
    
    print("\n" + "="*60)
    print("TRAVELLER PAGE CLEANING SUMMARY")
    print("="*60)
    
    print(f"Files processed: {stats['files_processed']}")
    print(f"Files modified: {stats['files_modified']}")
    print(f"Files unchanged: {stats['files_processed'] - stats['files_modified']}")
    
    print(f"\nLine count changes:")
    print(f"  Original total lines: {stats['total_original_lines']:,}")
    print(f"  Final total lines: {stats['total_final_lines']:,}")
    print(f"  Net lines removed: {stats['total_original_lines'] - stats['total_final_lines']:,}")
    
    print(f"\nArtifacts removed:")
    print(f"  Decorative TRAVELLER letters: {stats['total_decorative_letters_removed']}")
    print(f"  Standalone page numbers: {stats['total_page_numbers_removed']}")
    print(f"  Formatting artifacts: {stats['total_formatting_artifacts_removed']}")
    print(f"  Blank lines reduced: {stats['total_blank_lines_reduced']}")
    
    total_artifacts = (stats['total_decorative_letters_removed'] + 
                      stats['total_page_numbers_removed'] + 
                      stats['total_formatting_artifacts_removed'])
    print(f"  Total artifacts removed: {total_artifacts}")
    
    # Show files with most changes
    changed_files = [(name, detail) for name, detail in details.items() if detail['changed']]
    if changed_files:
        print(f"\nTop 10 files with most changes:")
        changed_files.sort(key=lambda x: x[1]['stats']['original_lines'] - x[1]['stats']['final_lines'], reverse=True)
        for i, (filename, detail) in enumerate(changed_files[:10]):
            lines_removed = detail['stats']['original_lines'] - detail['stats']['final_lines']
            artifacts = (detail['stats']['decorative_letters_removed'] + 
                        detail['stats']['page_numbers_removed'] + 
                        detail['stats']['formatting_artifacts_removed'])
            print(f"  {i+1:2}. {filename}: {lines_removed} lines removed ({artifacts} artifacts)")

if __name__ == "__main__":
    # Directory containing the page files
    directory = "/workspace/books/core-rules-2022"
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        exit(1)
    
    print("Starting Traveller Core Rules page cleaning...")
    print(f"Processing directory: {directory}")
    
    # Run the cleaning operation
    results = clean_all_pages(directory)
    
    # Print summary
    print_summary(results)
    
    print(f"\nCleaning complete! All page files have been processed.")
    print(f"Original .raw backup files remain unchanged.")