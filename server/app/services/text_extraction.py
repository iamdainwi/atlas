"""
Text extraction service using LangChain document loaders.
Extracts raw text and page count from PDF, DOCX, TXT, and MD files.
"""

import io
import tempfile
import os
from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)

from app.core.storage import s3_storage


def extract_text(s3_key: str, file_type: str) -> tuple[str, int]:
    """
    Download file from S3 and extract full text using the appropriate LangChain loader.

    Returns:
        (full_text: str, page_count: int)
    """
    # Download raw bytes from S3
    file_bytes = s3_storage.download_bytes(s3_key)

    # Write to a temporary file so LangChain loaders can open it
    suffix = f".{file_type}"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    try:
        return _load_with_langchain(tmp_path, file_type)
    finally:
        os.unlink(tmp_path)


def _load_with_langchain(file_path: str, file_type: str) -> tuple[str, int]:
    """Dispatch to the correct LangChain loader based on file type."""

    if file_type == "pdf":
        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
        full_text = "\n\n".join(d.page_content for d in docs)
        page_count = len(docs)

    elif file_type == "docx":
        loader = Docx2txtLoader(file_path)
        docs = loader.load()
        full_text = "\n\n".join(d.page_content for d in docs)
        page_count = 0  # DOCX has no native page count

    elif file_type == "md":
        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()
        full_text = "\n\n".join(d.page_content for d in docs)
        page_count = 0

    elif file_type == "txt":
        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()
        full_text = "\n\n".join(d.page_content for d in docs)
        page_count = 0

    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    return _clean_text(full_text), page_count


def _clean_text(text: str) -> str:
    """Strip extra whitespace and normalize newlines."""
    import re
    # Collapse 3+ newlines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Strip trailing spaces on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip()


__all__ = ["extract_text"]
