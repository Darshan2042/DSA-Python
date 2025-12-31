import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers.phonenumberutil import NumberParseException

numbers = [
    "+919552312042",
    "+919673980875"
    
]

print("\nPhone Numbers — location, carrier and basic info\n")

for num in numbers:
    try:
        parsed = phonenumbers.parse(num)                 # parse with international prefix
        valid = phonenumbers.is_valid_number(parsed)     # basic validity check
        location = geocoder.description_for_number(parsed, "en")
        service = carrier.name_for_number(parsed, "en")
        e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

        print(f"Number: {e164}")
        print(f"  Valid: {valid}")
        print(f"  Location (approx): {location or 'Unknown'}")
        print(f"  Carrier (approx): {service or 'Unknown'}")
        print()
    except NumberParseException as e:
        print(f"Number: {num} -> Parse error: {e}\n")
