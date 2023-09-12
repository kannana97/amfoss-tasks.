isPrime :: Int -> Bool
isPrime num
    | num <= 1 = False
    | num == 2 = True
    | even num = False
    | otherwise = all (\x -> num `mod` x /= 0) [3,5..isqrt num]
    where isqrt = floor . sqrt . fromIntegral

main :: IO ()
main = do
    putStrLn "Enter a number: "
    input <- getLine
    let n = read input :: Int
    putStrLn $ "Prime numbers up to " ++ show n ++ " are:"
    let primes = filter isPrime [2..n]
    putStrLn $ unwords (map show primes)

