encrypted_flag = "14f6ad8f2b43d835e2ce22b79d89b7ec22ceb70a0ed81e21"

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct).hex()



