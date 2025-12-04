import math

AVAILABLE_PRODUCTS = [
    ["تصميم شعار احترافي", 450.00],
    ["استضافة موقع ويب (سنة)", 300.00],
    ["كتابة محتوى لصفحة واحدة", 120.00],
    ["صيانة شهرية للنظام", 650.00]
]

VAT_RATE = 0.15 

def display_products():
    """عرض قائمة المنتجات المتاحة للمستخدم."""
    print("\n==================================")
    print("      قائمة الخدمات والمنتجات      ")
    print("==================================")
    for i in range(len(AVAILABLE_PRODUCTS)):
        name = AVAILABLE_PRODUCTS[i][0]
        price = AVAILABLE_PRODUCTS[i][1]
        print(f"{i + 1} - {name:<25} | السعر: {price:.2f} ريال")
    print("==================================")

def process_invoice_item():
    """معالجة اختيار المستخدم وحساب الفاتورة."""
    display_products()

    while True:
        try:
            choice = input("الرجاء إدخال رقم المنتج أو الخدمة التي تريد فوترتها: ")
            choice_index = int(choice) - 1

            if 0 <= choice_index < len(AVAILABLE_PRODUCTS):
                break
            else:
                print("❌ خطأ: الرقم خارج نطاق الخدمات المعروضة. حاول مرة أخرى.")
        except ValueError:
            print("❌ خطأ: الرجاء إدخال رقم صحيح فقط.")

    product_name = AVAILABLE_PRODUCTS[choice_index][0]
    unit_price = AVAILABLE_PRODUCTS[choice_index][1]

    while True:
        try:
            quantity = int(input(f"أدخل الكمية المطلوبة من '{product_name}': "))
            if quantity > 0:
                break
            else:
                print("❌ خطأ: يجب أن تكون الكمية أكبر من صفر.")
        except ValueError:
            print("❌ خطأ: الرجاء إدخال رقم صحيح للكمية.")

    
    subtotal = unit_price * quantity
    
    vat_amount = subtotal * VAT_RATE
    
    total_amount = subtotal + vat_amount

    print("\n==================================")
    print("       ملخص بند الفاتورة        ")
    print("==================================")
    print(f"اسم المنتج/الخدمة:  {product_name}")
    print(f"سعر الوحدة:        {unit_price:.2f} ريال")
    print(f"الكمية:            {quantity}")
    print("----------------------------------")
    print(f"المجموع قبل الضريبة: {subtotal:.2f} ريال")
    print(f"قيمة الضريبة ({VAT_RATE * 100:.0f}%):  {vat_amount:.2f} ريال")
    print("----------------------------------")
    print(f"الإجمالي المطلوب دفعه: {total_amount:.2f} ريال")
    print("==================================\n")

if __name__ == "__main__":
    process_invoice_item()
