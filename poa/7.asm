data segment
    string1 db 84h, 98h, 45h, 64h, 73h
    length db $ -string1
data ends

extra segment
    string2 db ?
extra ends

code segment
    start:mov ax, data
    mov ds, ax
    mov ax, extra
    mov es, ax
    mov cl, length
    lea si, string1
    lea di, string2
    l1:
        mov al, ds:[si]
        mov es:[di], al
        inc si
        inc di
        dec cl
        jnz l1
code ends
end start