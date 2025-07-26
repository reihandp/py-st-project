import qrcode  # qrcode package 

# example: https://github.com/reihandp

def qr_code_generate(target_link, img_save_as, file_name):
    """
    Generate a QR code from a given URL and save it as an image file.

    Parameters:
    - target_link (str): The URL or data to encode into the QR code.
    - img_save_as (int): Format option (1 = .jpg, 2 = .png, 3 = .gif).
    - file_name (str): Name of the saved file (without extension).
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(target_link)
    qr.make()

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    
    match img_save_as:
        case 1:
            img_save_as = '.jpg'
        case 2: 
            img_save_as = '.png'
        case 3: 
            img_save_as = '.gif'
        case _:
            img_save_as = False   
    
    if not img_save_as:
        print("\nInvalid file format selected.\n")
        return 
    try:
        img.save(file_name + img_save_as)
        print("\nSuccess! QR code file created.\n")
    except TypeError:
        print('\nSome Error!!!\n')

target_link = input('Input link: ')
print("""\nChoice Format Number:
1) jpg
2) png
3) gif           
""")
save_as = int(input('Save as file 1/2/3 : '))
file_name = input('\nFile name: ')

qr_code_generate(target_link, save_as, file_name)