def get_extension(filename):
    if "." not in filename or filename.endswith("."):
        return "none"
    return filename.split(".")[-1]
