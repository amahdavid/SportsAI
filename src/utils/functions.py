import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage

note_file = os.path.join("..", "data", "notes.txt")


def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w").close()

    with open(note_file, "a") as f:
        f.write(note + "\n")

    return "Note saved."


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))

    return index

