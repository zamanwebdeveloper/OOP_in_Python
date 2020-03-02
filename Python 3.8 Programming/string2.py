a = "this is a string"
print(a, " -> Is Lower ?",a.islower())# Only Small Letter
UP = a.upper()
print(UP, " -> Is Upper ?",UP.isupper())# Only Big Letter

print(a, " -> Is Alpha ?",a.isalpha())# Only Alphabetic
b = "Syed"
print(b, " -> Is Alpha ?",b.isalpha())
print(b, " -> Is AllNum ?",b.isalnum())
c  = "^*"
print(c, " -> Is AllNum ?",c.isalnum())
c = "SyedZaman125"
print(c, " -> Is AllNum ?",c.isalnum())
d = "01740301579"
print(d, " -> Is aldigit ?",d.isdigit())
