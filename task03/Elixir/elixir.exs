defmodule PrimeFinder do
  def is_prime(1), do: false
  def is_prime(2), do: true
  def is_prime(n) when rem(n, 2) == 0, do: false
  def is_prime(n) when n > 2 do
    Enum.all?(2..trunc(:math.sqrt(n)), fn x -> rem(n, x) != 0 end)
  end

  def find_primes(n) do
    Enum.filter(2..n, &is_prime/1)
  end
end

IO.puts("Enter a number: ")
input = String.trim(IO.gets(""))
n = String.to_integer(input)

IO.puts("Prime numbers up to #{n} are:")
PrimeFinder.find_primes(n) |> Enum.each(&IO.puts/1)

