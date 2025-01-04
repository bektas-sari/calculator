import math

def display_menu():
    print("\n=== Orta Seviye Hesap Makinesi ===")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Hesaplama")
    print("7. Çıkış")
    print("============================")

def get_numbers(single_input=False):
    if single_input:
        num = float(input("Bir sayı giriniz: "))
        return num, None
    else:
        num1 = float(input("Birinci sayıyı giriniz: "))
        num2 = float(input("İkinci sayıyı giriniz: "))
        return num1, num2

def calculate(choice):
    if choice == 1:  # Toplama
        num1, num2 = get_numbers()
        print(f"Sonuç: {num1} + {num2} = {num1 + num2}")
    elif choice == 2:  # Çıkarma
        num1, num2 = get_numbers()
        print(f"Sonuç: {num1} - {num2} = {num1 - num2}")
    elif choice == 3:  # Çarpma
        num1, num2 = get_numbers()
        print(f"Sonuç: {num1} * {num2} = {num1 * num2}")
    elif choice == 4:  # Bölme
        num1, num2 = get_numbers()
        if num2 != 0:
            print(f"Sonuç: {num1} / {num2} = {num1 / num2}")
        else:
            print("Hata: Sıfıra bölme yapılamaz.")
    elif choice == 5:  # Üs Alma
        num1, num2 = get_numbers()
        print(f"Sonuç: {num1} ^ {num2} = {math.pow(num1, num2)}")
    elif choice == 6:  # Karekök Hesaplama
        num, _ = get_numbers(single_input=True)
        if num >= 0:
            print(f"Sonuç: √{num} = {math.sqrt(num)}")
        else:
            print("Hata: Negatif bir sayının karekökü alınamaz.")
    elif choice == 7:  # Çıkış
        print("Hesap makinesi kapatılıyor...")
        return False
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
    return True

def main():
    running = True
    while running:
        display_menu()
        try:
            user_choice = int(input("Bir işlem seçiniz (1-7): "))
            running = calculate(user_choice)
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz.")

if __name__ == "__main__":
    main()
