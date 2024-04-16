from llama_index.core.tools import FunctionTool
from utils.functions import save_note

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)
