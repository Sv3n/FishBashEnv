FishBashEnv
===========

Source a bash based script and retain the environmental changes in fish.

Place `bsource.fish` in ~/.config/fish/functions. `envToFish.py` should be executable and sit somewhere in your path.

## Usage
`bsource <bash script>`

## Bugs / Obvious issues
 * bsource fails if more than 1 argument is given to the function.
 * possibly reorders path variable components.
 * could probably be implemented in pure fish code.
 * might not escape all variables properly, hence yielding an invalid profile.fish.
 * leaves profile.fish files begin in the current working directory.
