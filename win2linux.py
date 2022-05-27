"""Run this script to convert Windows to Linux."""
import os
import shutil
import subprocess
from typing import Dict, List

# Conversion equivalent
# Keys: Windows cursor names + extra (Keqing Hand, Keqing Grabbing Hand)
# Value: whiteglass cursor names + some DMZ-White cursor names
equiv: Dict[str, List[str]] = {
	"Alternate Select.cur": ["center_ptr", "right_ptr"],
	"Busy.ani": ["watch"],
	"Diagonal Resize (Backward).cur": [
		"bottom_right_corner", "lr_angle", "top_left_corner", "ul_angle"
	],
	"Diagonal Resize (Forward).cur": [
		"bottom_left_corner", "ll_angle", "top_right_corner", "ur_angle"
	],
	"Handwriting.cur": ["pencil"],
	"Help Select.cur": ["question_arrow"],
	"Horizontal Resize.cur": [
		"left_side", "left_tee", "right_side", "right_tee", "sb_h_double_arrow",
		"sb_left_arrow", "sb_right_arrow"
	],
	"Keqing Grabbing Hand.cur": ["grabbing"],
	"Keqing Hand.cur": ["hand1", "hand2"],
	"Link Select.cur": ["sb_down_arrow"],
	"Move.cur": ["sizing"],
	"Normal Select.cur": ["left_ptr"],
	"Precision Select.cur": ["cross"],
	"Text Select.cur": ["xterm"],
	"Unavailable.cur": ["X_cursor"],
	"Vertical Resize.cur": [
		"base_arrow_down", "base_arrow_up", "bottom_side", "bottom_tee",
		"double_arrow", "sb_up_arrow", "sb_v_double_arrow", "top_side", "top_tee"
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
