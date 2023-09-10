

def check (st):
    if "==" in st or "<>" in st or "in" in st:
        return True
    else:
        return False


if __name__ == "__main__":
    st = """select * from table
where roll_no == 10 and name in "shyam" """
    print(check(st))