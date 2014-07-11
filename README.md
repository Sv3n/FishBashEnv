FishBashEnv
===========

Source a bash based script and retain the environmental changes in fish.

Place `bsource.fish` in ~/.config/fish/functions. `envToFish.py` should be executable and sit somewhere in your path.

## Usage
`bsource <bash script>`

## Bugs / Obvious issues
 * bsource function expects only 1 argument but does not check this.
 * possibly reorders path variable components.
 * could probably be implemented in pure fish code.
 * might not escape all variables properly, hence yielding an invalid profile.fish.
 * leaves profile.fish files behind in the current working directory.
 * overwrites existing profile.fish files in the current working directory.
