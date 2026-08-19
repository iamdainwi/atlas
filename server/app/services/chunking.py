"""
Text chunking service using LangChain's RecursiveCharacterTextSplitter.
Splits extracted text into overlapping chunks suitable for embedding.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> list[str]:
    """
    Split text into overlapping chunks using LangChain's recursive splitter.

    The splitter tries to split on natural boundaries (paragraphs → sentences →
    words) before falling back to raw characters.

    Args:
        text:          The full extracted text.
        chunk_size:    Target size in characters per chunk (default 500).
        chunk_overlap: Overlap between consecutive chunks (default 100).

    Returns:
        List of non-empty text chunks.
    """
    if not text or not text.strip():
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_text(text)
    # Filter out any empty or whitespace-only chunks
    return [c.strip() for c in chunks if c.strip()]


__all__ = ["chunk_text"]
