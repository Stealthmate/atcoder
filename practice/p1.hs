import Data.List

main :: IO ()
main = do
  l:n:_ <- fmap read . words <$> getLine :: IO [Int]
  trees <- sequence . replicate n $ read <$> getLine :: IO [Int]
  let lt = floor $ n / 2
      leftTrees = take lt trees
      rightTrees = reverse $ drop lt trees

  where
    go p lts rts = 
  
