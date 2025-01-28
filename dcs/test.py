import os
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Courier", size=10)

    def add_code_file(self, filename, content):
        self.set_font("Courier", style="B", size=12)
        self.cell(0, 10, f"File: {filename}", ln=True, align="L")
        self.set_font("Courier", size=10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def get_code_files(root_dir, extensions):
    """Traverse directory and find files with specified extensions."""
    code_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extensions):
                code_files.append(os.path.join(root, file))
    return code_files

def main():
    root_dir = "./cea2045/cea2045/"  # Replace with your root directory
    extensions = (".cpp", ".h")  # C++ source file extensions

    # Get all code files
    code_files = get_code_files(root_dir, extensions)

    # Create a PDF
    pdf = PDF()
    for file in code_files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            content = "\n".join([line for line in content.splitlines() if not line.strip().startswith("//")])
        pdf.add_code_file(file, content)

    # Save the PDF
    output_path = "source_code.pdf"
    pdf.output(output_path)
    print(f"PDF generated: {output_path}")

if __name__ == "__main__":
    main()
