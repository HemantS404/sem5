data segment
    string db 9,8,5,11,4,3,6,7
    len db $ -string
    min db ?
    max db ?
data ends

code segment
    start:mov ax, data
    mov ds, ax
    mov cl, len
    lea si, string
    mov al, [si]
    mov min, al
    mov max, al
    l1:
        mov al, [si]
        cmp min, al
        jl l2
        mov min, al
        l2:
            cmp max, al
            jg l3
            mov max, al
            l3:
                inc si
                dec cl
                jnz l1
    
code ends
end start