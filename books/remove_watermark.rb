#!/usr/bin/env ruby

def remove_watermark_lines(file_path)
  begin
    lines = File.readlines(file_path)
    
    # Filter out lines containing 'Michael Greenly (Order #' followed by any number and ')'
    filtered_lines = lines.reject { |line| line =~ /Michael Greenly \(Order #\d+\)/ }
    
    # Only write back if changes were made
    if filtered_lines.length < lines.length
      File.write(file_path, filtered_lines.join)
      return true
    end
    false
  rescue => e
    puts "Error processing #{file_path}: #{e}"
    false
  end
end

def main
  books_dir = '/home/mgreenly/Projects/traveller/books'
  pattern = File.join(books_dir, '**', '*.txt')
  
  files = Dir.glob(pattern)
  
  modified_count = 0
  files.each do |file_path|
    if remove_watermark_lines(file_path)
      puts "Cleaned: #{file_path}"
      modified_count += 1
    end
  end
  
  puts "\nTotal files modified: #{modified_count}"
end

main if __FILE__ == $0