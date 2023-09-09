def is_prime(num)
  return false if num <= 1
  return true if num == 2
  return false if num % 2 == 0

  (3..Math.sqrt(num).to_i).step(2).each do |i|
    return false if num % i == 0
  end

  true
end

print "Enter a number: "
n = gets.chomp.to_i
puts "Prime numbers up to #{n} are:"
(2..n).each { |i| puts i if is_prime(i) }
