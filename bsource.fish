function bsource
    bash -c "source $argv > /dev/null && envToFish.py"
    . profile.fish
end
