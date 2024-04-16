# in this file you can have any function you'd like

from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("..", "data", "nba_data", "nba_notes.txt")


def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w").close()

    with open(note_file, "a") as f:
        f.write(note + "\n")

    return "Note saved."

# create a function to return a random fact


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)
