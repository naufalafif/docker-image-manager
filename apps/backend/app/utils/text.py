import tarfile
import io
import base64


def shorten_uuid(uuid: str) -> str:
    """
    The function shortens a UUID string to its first 8 characters.

    :param uuid: A string representing a UUID (Universally Unique Identifier)
    :type uuid: str
    :return: The function `shorten_uuid` takes a string `uuid` as input and returns the first 8
    characters of the string.
    """
    return uuid[:8]


def string_to_tar(data: str) -> tarfile.TarFile:
    """
    This function converts a string into a tarfile object and returns it.

    :param data: The input string that needs to be converted to a tar file
    :type data: str
    :return: a `tarfile.TarFile` object.
    """
    textIO = io.TextIOWrapper(io.BytesIO(), encoding="utf8")
    textIO.write(data)
    bytesIO = textIO.detach()
    info = tarfile.TarInfo(name="check.sh")
    info.size = bytesIO.tell()
    with tarfile.open("check.tar.gz", "w:gz") as tar:
        bytesIO.seek(0)
        tar.addfile(info, bytesIO)

        return tar


def string_to_base64(data: str):
    """
    This function converts a string to its base64 representation.

    :param data: The input string that needs to be converted to base64 encoding
    :type data: str
    :return: a base64 encoded string of the input data.
    """
    base64_bytes = base64.b64encode(data.encode("ascii"))
    base64_string = base64_bytes.decode("ascii")
    return base64_string
