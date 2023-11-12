import qrcode

def generate_wifi_qr(ssid, password, security_type="WPA"):
    # WiFi QR code format
    wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_code = qr.make_image(fill_color="black", back_color="white")

    # Save or display the generated QR code
    qr_code.save("wifi_qr.png")
    qr_code.show()

if __name__ == "__main__":
  # Replace 'YourSSID' and 'YourPassword' with your WiFi SSID and password
  generate_wifi_qr(ssid="", password="", security_type="WPA2")