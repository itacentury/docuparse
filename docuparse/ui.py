"""User interface functions."""

from pathlib import Path

from PySide6.QtWidgets import QApplication, QFileDialog, QWidget


def select_pdf_files() -> list[str] | None:
    """Open a file dialog to let the user select PDF files."""
    app: QApplication = QApplication([])

    # A hidden parent widget is needed to avoid a segfault in
    # PySide6 6.11's SignalManager when None is passed as parent.
    parent: QWidget = QWidget()

    file_paths, _ = QFileDialog.getOpenFileNames(
        parent,
        "Select Bills to Analyze",
        str(Path.home() / "Downloads"),
        "PDF files (*.pdf)",
    )

    app.quit()

    if not file_paths:
        return None

    return file_paths
