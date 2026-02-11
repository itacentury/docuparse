"""
User interface functions
"""

from pathlib import Path

from PySide6.QtWidgets import QApplication, QFileDialog


def select_pdf_files() -> list[str] | None:
    """Open a file dialog to let the user select PDF files."""
    app: QApplication = QApplication([])

    file_paths, _ = QFileDialog.getOpenFileNames(
        None,
        "Select Bills to Analyze",
        str(Path.home() / "Downloads"),
        "PDF files (*.pdf)",
    )

    app.quit()

    if not file_paths:
        return None

    return file_paths
