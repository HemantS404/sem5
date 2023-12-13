mov [101h], 9999h
mov [103h], 9999h

mov ax, [101h]
mov bx, [103h]
mov cl, 0h

add ax, bx
jnc l1
mov cl, 01h
l1:
    mov [105h], ax
    mov [107h], cl