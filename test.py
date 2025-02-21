from autocorrect_kh import autocorrect_address_1, autocorrect_address_2

address_1_text = "ផ្ទ៤១បេ ផ្លុវ៤៤៤ ភុមិ២"
address_2_text = "សង្កាត់ទលទពូងទី ២ ខណ្ឌចំករមន ភ្នំពញ"


address_1_text = autocorrect_address_1(address_1_text)
address_2_text = autocorrect_address_2(address_2_text)

print("Autocorrected Address:", address_1_text + " " + address_2_text)
