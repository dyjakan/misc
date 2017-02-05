#!/usr/bin/env ruby
#
# Hack the planet.
#

require 'digest/sha1'

def rename(file_path)
  file = File.open(file_path, 'rb')
  data = file.read
  file.close
  hashed = Digest::SHA256.hexdigest(data)
  puts "#{ARGV[0]}/#{hashed}.#{file_path.split('.')[-1]} = #{file_path}"
  File.rename(file_path, "#{ARGV[0]}/#{hashed}.#{file_path.split('.')[-1]}")
end

# Pull out all file names from directory pointed by ARGV[0]
files = Dir.entries(ARGV[0]).select { |f| !File.directory? f }

# Rename each file
files.each { |file_path| rename("#{ARGV[0]}/#{file_path}") }
