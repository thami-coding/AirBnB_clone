from .engine.file_storage import FileStorage

storage = FileStorage('file.json', {})
storage.reload()
