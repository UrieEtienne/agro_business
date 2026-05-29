from reportlab.pdfgen import canvas

def generate_bon(livraison):

    c = canvas.Canvas("bon_livraison.pdf")

    c.drawString(100, 750, f"Client: {livraison.client_nom}")

    c.drawString(100, 730, f"Produit: {livraison.produit}")

    c.drawString(100, 710, f"Quantité: {livraison.quantite}")

    c.save()