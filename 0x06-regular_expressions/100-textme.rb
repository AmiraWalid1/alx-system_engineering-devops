#!/usr/bin/env ruby
SENDER = ARGV[0].match(/\[from:(\+?)(\w*)\]/)[0]
RECEIVER = ARGV[0].match(/\[to:(\+?)(\w*)\]/)[0]
FLAGS = ARGV[0].match(/\[flags:(-?\d):(-?\d):(-?\d):(-?\d):(-?\d)\]/)[0]
puts SENDER[6..(SENDER.size - 2)] + ',' + RECEIVER[4..(RECEIVER.size - 2)] + ',' + FLAGS[7..(FLAGS.size - 2)]
