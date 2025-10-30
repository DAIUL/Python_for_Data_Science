import datetime as dt
import time as tm

sec_since = tm.time()
now = dt.datetime.now()

print(f"Seconds since January 1, 1970: {sec_since:.4f} or {sec_since:.2e} in scientific notation")
print(f"{now.strftime('%b %d %Y')}")