from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "B", 48)
        self.set_text_color(139,0,139)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    shirti(name)


def shirti(s):
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", size=26)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 210, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
