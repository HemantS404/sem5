data segment
    string db 99h,94h, 98h, 95h, 92h, 97h
    length db $ -string
data ends

code segment
    start:mov ax, data
    mov ds, ax
    mov ch, length
    l1:
        lea si, string
        mov cl, length
        l2:
            mov al, [si]
            mov bl, [si+1]
            cmp al, bl
            jl l3
            mov [si], bl
            mov [si+1], al
            l3:
                inc si
                dec cl
                jnz l2
                dec ch
                jnz l1 
code ends
end start