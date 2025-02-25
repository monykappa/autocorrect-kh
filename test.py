from autocorrect_kh import autocorrect_address_1, autocorrect_address_2 # For address_1 and address_2
from autocorrect_kh import autocorrect_phum, autocorrect_khum, autocorrect_district, autocorrect_province # For Phum, Khum, District, Province

# ===========Autocorrect for Phum, Khum, District, Province================
phum_text = "កូមិត្រពាងថ្លង២"
khum_text = "សង្កាក់ច្បាអំពៅ២"
district_text = "ខណ្ឌចំករមន"
province_text = "កំពង់ចម"

autocorrect_phum = autocorrect_phum(phum_text)
autocorrect_khum = autocorrect_khum(khum_text)
autocorrect_district = autocorrect_district(district_text)
autocorrect_province = autocorrect_province(province_text)

print("========================Autocorrect for Phum, Khum, District, Province========================")
print(f"Original phum {phum_text} -> autocorrected phum {autocorrect_phum}")
print(f"Original khum {khum_text} -> autocorrected khum {autocorrect_khum}")
print(f"Original district {district_text} -> autocorrected district {autocorrect_district}")
print(f"Original province {province_text} -> autocorrected province {autocorrect_province}")

# =======================================================================


# ===========Autocorrect for Address for Khmer National ID================

address_1 = "ផ្ទះ៤១បេ ផ្លូវ៤៤៤ ភុមិ២"
address_2 = "សង្កាត់ទលទពូងទី ២ ខណ្ឌចំករមន ភ្នំពញ"


autocorrect_address_1= autocorrect_address_1(address_1)
autocorrect_address_2 = autocorrect_address_2(address_2)

print("========================Autocorrect for Address for Khmer National ID========================")
print(f"Original address 1 {address_1} -> autocorrected address 1 {autocorrect_address_1}")
print(f"Original address 2 {address_2} -> autocorrected address 2 {autocorrect_address_2}")


# =======================================================================