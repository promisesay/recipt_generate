import pandas as pn
from fpdf import FPDF

df = pn.read_csv("articles.csv", dtype={"id": str})


class Shop:
    def __init__(self, items_id):
        self.id = items_id
        self.sos = df.loc[df["id"] == self.id]["name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def item(self):
        info = f"items name:{self.sos} price: {self.price} \n"
        return info


class Receipt:
    def __init__(self, items):
        self.article = items

    def generate(self):
        pdf = FPDF(orientation="p", format="a3", unit="mm")
        pdf.add_page()
        info = f"the receipt ny{self.article.id}"
        pdf.set_font(family="times", style="B", size=43)
        pdf.cell(w=42, h=32, txt=info, ln=1)
        pdf.set_font(family="", style="B", size=39)
        pdf.cell(w=23, h=32, ln=1, txt=f"items name: {self.article.sos}")
        pdf.cell(w=23, h=32, ln=1, txt=f"items price: {self.article.price}")
        pdf.output(name="receipt.pdf")


if __name__ == "__main__":
    print(df)
    item = input("enter the id of item:")
    shop = Shop(item)
    command = input(f"{shop.item()}do you want to purchase it")
    command = command.lower()
    if command.strip() == "yes":
        Recaipt = Receipt(shop)
        Recaipt.generate()
    else:
        pass


