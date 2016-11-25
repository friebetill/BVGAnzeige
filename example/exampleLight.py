from executor import execute

# To regulate the brightness
# xrandr --output LVDS1 --brightness 0.9
# You have to adjust --output to your screen
execute('xrandr', '--output', 'eDP1', '--brightness', '0.9')

# To turn off the screen
# xset dpms force off
execute('xset', 'dpms', 'force', 'off')
