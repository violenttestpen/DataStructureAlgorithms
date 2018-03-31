require 'benchmark'

load '../Search.rb'

TIMES = 1000000000
start = 99999
sample_space = (start..(start * 100)).to_a

Benchmark.bm do |bm|
  bm.report { binary_search(sample_space, rand() * TIMES) }
  bm.report { binary_search_recursive(sample_space, rand() * TIMES) }
  bm.report { interpolation_search(sample_space, rand() * TIMES) }
  bm.report { interpolation_search_recursive(sample_space, rand() * TIMES) }
end