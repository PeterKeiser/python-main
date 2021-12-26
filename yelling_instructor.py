# yelling_instructor

instructor = {"name": "colt", "city": "san francisco", "colour": "purple"}
print(instructor)

yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(yelling_instructor)