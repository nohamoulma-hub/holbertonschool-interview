#!/usr/bin/pyhton3
def canUnlockAll(boxes):
    n = len(boxes)
    keychain = [0]
    while True:
        size_keychain_before = len(keychain)
        for j in range(len(boxes)):
            if j in keychain:
                for key in boxes[j]:
                    if key not in keychain:
                        keychain.append(key)
        size_keychain_after = len(keychain)
        if size_keychain_before == size_keychain_after:
            break
    for i in range(0, n - 1):
        if i not in keychain:
            return False
    return True
