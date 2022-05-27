"""Run this script to convert Windows to Linux."""
import os
import shutil
import subprocess
from typing import Dict, List

# Conversion equivalent
# Keys: Windows cursor names + extra (Keqing Hand, Keqing Grabbing Hand)
# Value: DMZ-White cursor names
equiv: Dict[str, List[str]] = {
	"Alternate Select.cur": ["right_ptr", "draft_large", "draft_small"],
	"Busy.ani": ["watch"],
	"Diagonal Resize (Backward).cur": [
		"bd_double_arrow", "bottom_right_corner", "lr_angle", "top_left_corner",
		"ul_angle"
	],
	"Diagonal Resize (Forward).cur": [
		"bottom_left_corner", "fd_double_arrow", "ll_angle", "top_right_corner",
		"ur_angle"
	],
	"Handwriting.cur": ["color-picker", "copy", "pencil"],
	"Help Select.cur": ["question_arrow", "help", "left_ptr_help"],
	"Horizontal Resize.cur": [
		"left_side", "left_tee", "right_side", "right_tee", "sb_h_double_arrow",
		"h_double_arrow", "sb_left_arrow", "sb_right_arrow"
	],
	"Keqing Grabbing Hand.cur": [
		"grabbing", "fleur", "dnd-none", "dnd-link", "dnd-move", "dnd-copy",
		"dnd-ask"
	],
	"Keqing Hand.cur": [],
	"Link Select.cur": ["link", "hand", "hand1", "hand2"],
	"Move.cur": ["move"],
	"Normal Select.cur": ["left_ptr", "arrow", "top_left_arrow"],
	"Precision Select.cur": [
		"cross", "cross_reverse", "diamond_cross", "crosshair", "plus", "tcross"
	],
	"Text Select.cur": ["xterm"],
	"Unavailable.cur": ["X_cursor", "pirate", "circle", "crossed_circle"],
	"Vertical Resize.cur": [
		"bottom_side", "bottom_tee", "sb_down_arrow", "sb_up_arrow",
		"sb_v_double_arrow", "double_arrow", "v_double_arrow", "top_side", "top_tee"
	],
	"Working in Background.ani": ["left_ptr_watch"]
}

# Check Windows files
for dirname in os.listdir("Windows"):
	if dirname not in equiv:
		raise FileNotFoundError(f"'Windows/{dirname}' doesn't exist.")

# Initialize Linux directory
shutil.rmtree("Linux")
os.mkdir("Linux")

# Start the conversion
for window_cursor, linux_cursors in equiv.items():
	for linux_cursor in linux_cursors:
		subprocess.run(["win2xcur", f"Windows/{window_cursor}", "-o", "Linux"])
		
		filename = os.path.splitext(window_cursor)[0]
		os.rename(f"Linux/{filename}", f"Linux/{linux_cursor}")

print("Conversion finished.")
