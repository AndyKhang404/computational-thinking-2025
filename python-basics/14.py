def describe_person(*args, **kwargs):
    print("hobbies:", ", ".join(args))
    for k, v in kwargs.items():
        print(f"{k}: {v}")

describe_person("football","badminton","jogging",name="Khang", age=19, city="HCMC")