import os

import qrcode
from dotenv import load_dotenv

load_dotenv()

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173",
)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000",
)


def generate_qr_code(table_id: int) -> str:
    """
    Generate a QR code for a restaurant table
    and return its public URL.
    """

    menu_url = f"{FRONTEND_URL}/menu/table/{table_id}"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )

    qr.add_data(menu_url)
    qr.make(fit=True)

    img = qr.make_image()

    os.makedirs("uploads/qr", exist_ok=True)
    file_name = f"table_{table_id}.png"
    file_path = f"uploads/qr/{file_name}"

    img.save(file_path)

    return f"{BACKEND_URL}/uploads/qr/{file_name}"