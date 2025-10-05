import hashlib

def crack(hash):
    for i in range(99999):
        if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash:
            return str(i).zfill(5)

if __name__ == "__main__":
    print(crack("86aa400b65433b608a9db30070ec60cd"))