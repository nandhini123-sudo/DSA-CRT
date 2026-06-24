d = {"s": 1, "i": 2}

print(d.get("s"))      # 1
print(d.get("a"))      # None
print(d.get("a", "Not Found"))  # Not Found